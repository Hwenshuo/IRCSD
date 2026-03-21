import warnings
warnings.filterwarnings("ignore")

# 数据分析模块 #
import os
import numpy as np
import pandas as pd
import xarray as xr
from scipy import signal
from scipy.interpolate import CubicSpline
from scipy.stats import chi2
from statsmodels.tsa.stattools import acf
import xskillscore as xs
import geocat.comp as gc
from joblib import Parallel, delayed

# 可视化模块 #
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import dash_uploader as du
import dash_bootstrap_components as dbc
# import dash_daq as daq
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import feffery_antd_components as fac
import webbrowser

# 自定义模块 #
from climate_indices_info_NOAA import NOAA_indices_info
from climate_indices_info_NCC import NCC_indices_info
from climate_indices_info_EXT import EXT_indices_info
indices_info = {}
indices_info.update(NOAA_indices_info)
indices_info.update(NCC_indices_info)
indices_info.update(EXT_indices_info)
from txt_load import txt_climate_indices_load, txt_input_signal_load  # 使用已有的加载函数
from preprocess_funcs import preprocess_data #导入数据预处理函数
from filtering_funcs import movingaverage_filter, butterworth_filter, lanczos_filter, fourier_filter  # 导入滤波函数
import corr_funcs
from RI_initialization import RI_init
import power_spectral_density as psd
import pyleoclim as pyleo


## for ccrc version ##
# #close flask warining if debug mode is off
# import logging
# log = logging.getLogger('werkzeug')
# log.setLevel(logging.ERROR)

# # Welcome #
# print("Welcome to use the Interactive Rapid Climate Signal Detection Software (IRCSD) ")
# print("This is the internal verison for our research group in CCRC")
# print("Please open http://172.19.108.234:8050/ in your PC browser to enjoy the journey of clmate change research~")
# print()
# print("Monitoring Information:")

# ## public version ##
# import logging
# log = logging.getLogger('werkzeug')
# log.setLevel(logging.ERROR)

# # Welcome #
# print("Welcome to use the Interactive Rapid Climate Signal Detection Software (IRCSD) ")
# print("This is the public beta version")
# print("Please open http://113.44.134.87:8050/ in your PC browser to enjoy the journey of climate change research~")
# print()
# print("Monitoring Information:")

# 创建 Dash app
app = dash.Dash(__name__)

climate_indices = list(indices_info.keys())
single_options_list = []
for index in climate_indices:
    single_options_list.append({'label': f'{index}', 'value': f'{index}'})

# 配置上传文件夹
du.configure_upload(app, folder='temp')

# 预定义 Dash 应用的布局
app.layout = html.Div([
    html.Img(src='./assets/IRCSD.png', style={'display': 'block', 'margin': '0 auto', 'width': '120px', 'marginBottom': '5px'}),
    html.H1('Interactive Rapid Climate Signal Detection Software (IRCSD)', style={'textAlign': 'center', 'fontSize': '30px', 'marginTop': '0'}),
    html.P([
        html.Strong('Author: '),
        html.Span('Wenshuo Huang (huangwenshuo21@mails.ucas.ac.cn)',
                style={'marginRight': '20px'}),

        html.Strong('Version: '),
        html.Span('2.0 (Last updated: 2026.03.18)',
                style={'marginRight': '20px'}),

        html.Strong('Repository: '),
        html.A(
            html.Img(
                src='assets/github-mark.png',
                style={'height': '20px', 'width': 'auto'}
            ),
            href='https://github.com/Hwenshuo/IRCSD'
        )
    ], style={'textAlign': 'center'}),
    html.B("0. README", style={'color':"#de420d"}),
    html.P('The Interactive Rapid Climate Signal Detection Software (IRCSD) is a fast climate signal detection tool developed using Dash and Python. For unknown climate signals as input, IRCSD integrates various climate statistical methods, including selecting time ranges, data preprocessing, detrending, and applying different filtering methods and types, to compute the correlation between the signal and about 260 common climate indices (such as atmospheric, oceanic, and sea ice indices, etc.). It utilizes parallel computing to accelerate detection speed and outputs interactive detection results (including signal time series, power spectrum, correlation coefficients, lead-lagged correlation coefficients, sliding correlation coefficient, and Liang-Kleeman Information Flow). IRCSD is designed for researchers in atmospheric science and the public interested in climate change. The goal of IRCSD is to assist in quickly identifying potential source regions of anomalous signals and to enhance the efficiency of climate change research.',
            style={
                'backgroundColor': '#f0f0f0',  # 背景颜色
                'border': '2px solid #ccc',    # 边框样式
                'padding': '10px',              # 内边距
                'borderRadius': '5px',          # 圆角边框
            }),
    # html.P([html.Strong('Author: '),'Wenshuo Huang (huangwenshuo21@mails.ucas.ac.cn) ', html.Strong('Version: '), '1.0 (Last updated: 2024.11.05) ', html.Strong('Source Code/Indices Infos: '), html.A('Repository',href='https://github.com/Hwenshuo/IRCSD')]),

    html.B("1. Upload your signal", style={'color':"#de420d"}),
    html.Br(),
    html.Label('Declare Input Signal Frequency:  '),  # RI时间分辨率声明 
    fac.AntdRadioGroup(
        id='RI_frequeny_dropdown',
        options=[
            {'label': 'Annually', 'value': 'year'},
            {'label': 'Monthly', 'value': 'month'}
        ],
        value='year'
        ),
    html.Br(),

    du.Upload(
        id='uploader',
        text='Click or drag the file here to upload it! (Only support .nc and .txt file. Input Signal frequency must be annually or monthly)',
        text_completed='Signal has been uploaded: ',
        cancel_button=True,
        pause_button=True,
        filetypes=['nc','txt'],
        upload_id='mydata',
    ),

    dcc.Graph(id='xy-plot'), # 图表输出
    dcc.Store(id='stored-data'),  # 存储 RI 数据
    dcc.Store(id='stored-signal_yearST0'), 
    dcc.Store(id='stored-signal_yearED0'), 
    html.Div(id='RI_output'), # 输出xarray

    dcc.Graph(id='psd-plot'), #功率谱

    html.B("2. Select time coverage", style={'color':"#de420d"}),
    html.Br(),
    dcc.Checklist(id='RI_time_sel',
                  options=[{'label': 'Use Original Time Coverage', 'value': 'orgin'}],
                  value=['orgin']),  # 默认原时间范围
    # 时间范围选择
    html.Div(id='time-range-container', style={'display': 'none'}, children=[
        fac.AntdRow(
            [
                fac.AntdCol(
                    html.Div([
                        html.Label('Select Start Year:', style={'fontSize': '16px'}),
                        fac.AntdInputNumber(id='signal_yearST', value=1980, style={'width': 300})
                    ]),
                    flex=5
                ),
                fac.AntdCol(
                    html.Div([
                        html.Label('Select End Year:', style={'fontSize': '16px'}),
                        fac.AntdInputNumber(id='signal_yearED', value=2019, style={'width': 300})
                    ]),
                    flex=5
                )
            ]
        )
    ]),

    html.B("3. Select analyzing time", style={'color':"#de420d"}), # 数据预处理方式选择
    html.Br(),
    fac.AntdRow([fac.AntdCol(
        html.Div([
                html.Label('Input Signal Time:'),  # RI时间尺度选择
                dcc.Dropdown(
                    id='RI_time_scale_dropdown',
                    options=[
                        {'label': 'Annual Average', 'value': 'year'},
                        {'label': 'Seasonal Average (MAM)', 'value': 'MAM'},
                        {'label': 'Seasonal Average (JJA)', 'value': 'JJA'},
                        {'label': 'Seasonal Average (SON)', 'value': 'SON'},
                        {'label': 'Seasonal Average (DJF)', 'value': 'DJF'},
                        {'label': 'Original Time', 'value': 'origin'}
                    ],
                    value='year',
                )
            ]),flex=5), 
            fac.AntdCol(
                html.Div([
                html.Label('Climate Indices Time:'),  # CI时间尺度选择
                dcc.Dropdown(
                    id='CI_time_scale_dropdown',
                    options=[
                        {'label': 'Annual Average', 'value': 'year'},
                        {'label': 'Seasonal Average (MAM)', 'value': 'MAM'},
                        {'label': 'Seasonal Average (JJA)', 'value': 'JJA'},
                        {'label': 'Seasonal Average (SON)', 'value': 'SON'},
                        {'label': 'Seasonal Average (DJF)', 'value': 'DJF'},
                        {'label': 'Original Time', 'value': 'origin'}
                    ],
                    value='year',
                )
            ]) ,flex=5), 
        ], gutter=10),

    html.B("4. Select data preprocessing method", style={'color':"#de420d"}), # 数据预处理方式选择

    fac.AntdRow([fac.AntdCol(
        html.Div([
                html.Label('Input Signal:'),  # RI时间尺度选择
                dcc.Dropdown(id='RI_preprocess_dropdown',
                 options=[
                     {'label': 'Standardization', 'value': 'Standardization'},
                     {'label': 'Min-Max Normalization', 'value': 'MinNormalization'},
                     {'label': 'Mean Normalization', 'value': 'MeanNormalization'},
                     {'label': 'Centralization', 'value': 'Centralization'},
                     {'label':'Remove the annual cycle (monthly data)','value':'RmMonAnnCycle'},
                     {'label':'No preprocess data','value':"nopreprecess"}
                 ],
                 value='Standardization')
            ]),flex=5), 
            fac.AntdCol(
                html.Div([
                html.Label('Climate Indices:'),  # CI时间尺度选择
                dcc.Dropdown(id='CI_preprocess_dropdown',
                 options=[
                     {'label': 'Standardization', 'value': 'Standardization'},
                     {'label': 'Min-Max Normalization', 'value': 'MinNormalization'},
                     {'label': 'Mean Normalization', 'value': 'MeanNormalization'},
                     {'label': 'Centralization', 'value': 'Centralization'},
                     {'label':'Remove the annual cycle (monthly data)','value':'RmMonAnnCycle'},
                     {'label':'No preprocess data','value':"nopreprecess"}
                 ],
                 value='Standardization')
            ]) ,flex=5), 
        ], gutter=10),

    html.B("5. Remove the data trend", style={'color':"#de420d"}),# 去趋势选择

    fac.AntdRow([
    dcc.Checklist(id='RI_detrend_checklist',
                  options=[{'label': 'Remove Input Signal Trend', 'value': 'detrend'}],
                  value=[]),  # 默认不去趋势
    dcc.Checklist(id='CI_detrend_checklist',
                  options=[{'label': 'Remove Climate Indices Trend', 'value': 'detrend'}],
                  value=[])
    ]),  # 默认不去趋势

    html.B("6. Filter the data", style={'color':"#de420d"}),# 滤波选择
    html.Br(),
    html.Label('Whether Both Filter: '),
    fac.AntdRadioGroup(id='same_filter_method',
                 options=[
                     {'label': 'Both Same Method (Including both no filter)', 'value': 'Samefilter'},
                     {'label': 'No Filter for Input Signal', 'value': 'Notsamefilter'}
                 ],
                 value='Samefilter'),
    html.Br(),

    html.Div(id='Nosame_filter_components', style={'display': 'block'},children=[           
    html.Label('Input signal already filter cutoff='),
    fac.AntdInputNumber(id='Cutoff_already', placeholder='请输入数值', style={'width': 100}, value=9)
    ]),

    html.Label('Select Filter Method (only support no filter and butterworth now):  '),
    fac.AntdRadioGroup(id='filter_method_dropdown',
                 options=[
                     {'label': 'No Filter', 'value': 'nofilter'},
                     {'label': 'Moving Average', 'value': 'movingaverage'},
                     {'label': 'Butterworth', 'value': 'butterworth'},
                     {'label': 'Lanczos', 'value': 'lanczos'},
                     {'label': 'Fourier', 'value': 'fourier'}
                 ],
                 value='movingaverage'),
    html.Div(id='filter_components', style={'display': 'block'},children=[  # 用于放置后面的组件
    html.Label('Select Filter Type:  '),  
    fac.AntdRadioGroup(id='filter_type_dropdown',
                 options=[
                     {'label': 'Low Pass', 'value': 'low'},
                     {'label': 'High Pass', 'value': 'high'},
                     {'label': 'Band Pass', 'value': 'band'}
                 ],
                 value='low'),
    html.Br(),             
    html.Label('Default sample signal frequency=1, Cutoff frequency 1='),
    fac.AntdInputNumber(id='Cutoff1', placeholder='请输入数值', style={'width': 100}, value=9),          
    html.Label(' ,Cutoff frequency 2='),
    fac.AntdInputNumber(id='Cutoff2', placeholder='请输入数值', style={'width': 100}, value=0),
    html.Label('(For band pass only)')
    ]),
    html.Br(id='conditional_break'),

    html.B("7. Select correlation coefficient", style={'color':"#de420d"}), # 数据预处理方式选择
    dcc.Dropdown(id='Corr_dropdown',
                 options=[
                     {'label': 'Correlation', 'value': 'Corr'},
                     {'label': 'Lead-lagged Correlation', 'value': 'Llr'},
                     {'label': 'Sliding Correlation', 'value': 'Slc'}
                 ],
                 value='Corr'),
    # 延迟时间标签和输入框，默认隐藏
    html.Div([
        html.Label('Lag time=', id='lag-time-label', style={'display': 'none'}),
        fac.AntdInputNumber(
            id='lag_time',
            placeholder='请输入数值',
            style={'width': 100},
            value=0
        )
    ], style={'display': 'flex', 'alignItems': 'center'}),

    html.Div([
        html.Label('Sliding window=', id='window-time-label'),
        fac.AntdInputNumber(
            id='window_time',
            placeholder='请输入数值',
            style={'width': 100},
            value=0
        )
    ], style={'display': 'flex', 'alignItems': 'center'}),

    html.B("8. Select output format", style={'color':"#de420d"}), # 数据预处理方式选择
    html.Div([
    dcc.RadioItems(
        id='output-type',
        options=[
            {'label': 'All Indices', 'value': 'batch'},
            {'label': 'Single Index', 'value': 'single'}
        ],
        value='batch',  # 默认选择批量输出
        labelStyle={'display': 'inline-block'}
    ),
    dcc.Dropdown(
        id='climate-index-dropdown',
        options=single_options_list,
        placeholder='Search and choose a climate index',
        style={'display': 'none'}  # 默认隐藏
    )
    ]),

    dcc.Loading(id="loading-indicator",type="circle",children=[
    html.Button('Detect Input Signal', id='submit_button', n_clicks=0, style={'font-size': '15px', 'width': '200px', 'display': 'inline-block', 'margin-bottom': '10px', 'margin-top': '10px','margin-right': '5px', 'height':'35px', 'verticalAlign': 'top'}),
    html.Div(id='output-container', style={'marginTop': 10})
    ]),
    # 提交按钮
    # html.Button('Update', id='submit_button', n_clicks=0, style={'font-size': '15px', 'width': '140px', 'display': 'inline-block', 'margin-bottom': '10px', 'margin-right': '5px', 'height':'35px', 'verticalAlign': 'top'}),
    # 动态生成图表区域
    # html.Div(id='output-container', style={'marginTop': 20}), #输出文字状态
    html.Div(id='graphs-container')
])

# 回调函数，根据 RI_time_sel 更新时间范围选择框的显示状态
@app.callback(
    Output('time-range-container', 'style'),
    Input('RI_time_sel', 'value')
)
def update_time_range_display(selected_values):
    if 'orgin' in selected_values:
        return {'display': 'none'}  # 隐藏时间范围选择框
    else:
        return {'display': 'block'}  # 显示时间范围选择框

# 回调函数，no same filter时,确认Input Signal已存在的滤波频率
@app.callback(
    Output('Nosame_filter_components', 'style'),
    Input('same_filter_method', 'value')
)
def update_nosame_filter_components(same_selected_method):
    if same_selected_method == 'Samefilter':
        return {'display': 'none'}  # 隐藏组件
    else:
        return {'display': 'block'} # 显示组件

# 回调函数，no filter时隐藏滤波器种类选择    
@app.callback(
    [Output('filter_components', 'style'),
     Output('conditional_break', 'style')],
    Input('filter_method_dropdown', 'value')
)
def update_filter_components(selected_method):
    if selected_method == 'nofilter':
        return {'display': 'none'} , {'display': 'block'} # 隐藏组件
    else:
        return {'display': 'block'} ,{'display': 'none'}  # 显示组件

# 回调函数，根据选项更新lag-time输入框的显示状态
@app.callback(
    Output('lag-time-label', 'style'),
    Output('lag_time', 'style'),
    Input('Corr_dropdown', 'value')
)
def update_lag_time_display(selected_value):
    if selected_value == 'Llr':
        return {'display': 'block'}, {'display': 'block'}  # 显示标签和输入框
    else:
        return {'display': 'none'}, {'display': 'none'}  # 隐藏标签和输入框

# 回调函数，根据选项更新window-time输入框的显示状态
@app.callback(
    Output('window-time-label', 'style'),
    Output('window_time', 'style'),
    Input('Corr_dropdown', 'value')
)
def update_window_time_display(selected_value):
    if selected_value == 'Slc':
        return {'display': 'block'}, {'display': 'block'}  # 显示标签和输入框
    else:
        return {'display': 'none'}, {'display': 'none'}  # 隐藏标签和输入框

# 回调函数，根据选项气候指数选择框的显示状态
@app.callback(
    Output('climate-index-dropdown', 'style'),
    Input('output-type', 'value')
)
def update_dropdown_visibility(output_type):
    if output_type == 'single':
        return {'display': 'block'}  # 显示下拉框
    return {'display': 'none'}  # 隐藏下拉框

@app.callback(
    [Output('xy-plot', 'figure'),
     Output('stored-data', 'data'),
     Output('stored-signal_yearST0', 'data'),
     Output('stored-signal_yearED0', 'data'),
     Output('psd-plot', 'figure')],
    [Input('uploader', 'isCompleted')],
    [State('uploader', 'fileNames'),
     State('RI_frequeny_dropdown', 'value')]
)
def RI_self_check(is_completed, file_names, RI_frequeny):
    if not is_completed or not file_names:
        xy_fig = go.Figure()
        xy_fig.add_annotation(
            x=0.5,  # 正中央
            y=0.5,  # 正中央
            xref="paper",  # 相对于画布
            yref="paper",  # 相对于画布
            text="No Input Signal Now",
            showarrow=False,  # 不显示箭头
            font=dict(family="harding", size=46)
        )
        xy_fig.update_layout(
            title={
                'text': "Input Signal",
                'y': 0.97,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            },
            title_font=dict(family="harding", size=24, weight='bold'),
            margin=dict(t=40,b=30),
            template="simple_white",
            font=dict(family="Arial", size=18)
        )  

        psd_fig = go.Figure()
        psd_fig.add_annotation(
            x=0.5,  # 正中央
            y=0.5,  # 正中央
            xref="paper",  # 相对于画布
            yref="paper",  # 相对于画布
            text="No Input Signal Now",
            showarrow=False,  # 不显示箭头
            font=dict(family="harding", size=46)
        )
        psd_fig.update_layout(
            title={
            'text': "Power Spectrum",
            'y': 0.97,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
            },
            title_font=dict(family="harding", size=24, weight='bold'),
            margin=dict(t=35, b=30),
            template="simple_white",
            font=dict(family="Arial", size=18)
        )
        return xy_fig, None, None, None, psd_fig
    else:
        file_path = os.path.join('./temp/mydata', file_names[0])
        # 读取数据并获取开始和结束年份
        RI, signal_yearST0, signal_yearED0 = RI_init(file_path, file_names[0], RI_frequeny)

    # 绘制 xy 折线图
        xy_fig = go.Figure()
        xy_fig.add_trace(go.Scatter(x=RI['time'], y=RI, line=dict(color='red', width=2),mode='lines', name='Signal'))
        xy_fig.update_layout(
            title={
                'text': f"Input Signal (Start: {signal_yearST0} End: {signal_yearED0})",
                'y': 0.97,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            },
            title_font=dict(family="harding", size=24, weight='bold'),
            xaxis_title='Time',
            yaxis_title='Signal Values',
            margin=dict(t=40,b=30),
            template="simple_white",
            font=dict(family="Arial", size=18),
            hovermode='x unified'
            )
        
        RI_psd = RI.copy()
        if RI_psd.isnull().any():
            RI_psd = RI_psd.dropna(dim="time")  # 删除缺失值
        else:
            RI_psd = RI_psd
        #计算功率谱
        x_detrended_data = signal.detrend(RI_psd)
        n  = len(x_detrended_data)
        print('the length of time serise:',n)
        m = n // 4
        print('max_lag number is :',m)
        
        autocorr = acf(x_detrended_data, nlags = m) 
        spe = psd.compute_spectrum(autocorr, m) # 计算粗谱 
        smoothed_values = psd.hanning_smoothing(spe) # 计算平滑谱=
        fre,_ = psd.compute_frequency_and_period(m) # 计算频率周期
        red_noise, _, _ = psd.significance_test(smoothed_values, autocorr, m) # 计算显著性检验

        # 如果RI_frequeny是"year"就使用年周期，否则使用月周期
        if RI_frequeny == "year":
            cycle_list = [70, 40, 20, 10, 7, 4, 2]
            xticks = 1 / np.array(cycle_list)
            xticklabels = cycle_list
        else:
            cycle_list = [70*12, 40*12, 20*12, 10*12, 7*12, 4*12, 2*12, 12, 6, 3]
            xticks = 1 / np.array(cycle_list)
            xticklabels = [70, 40, 20, 10, 7, 4, 2, 1, 0.5, 0.25]

        v        = (2*n-m/2)/m
        CL95_red = red_noise*chi2.ppf(1 - 0.05, v) / v
        psd_fig = go.Figure()

        # 添加估算的谱
        psd_fig.add_trace(go.Scatter(x=fre, y=smoothed_values, mode='lines', name='Estimated spectrum', line=dict(width=2, color='blue')))

        # 添加95%红噪声置信度限制
        psd_fig.add_trace(go.Scatter(x=fre, y=CL95_red, mode='lines', name='95% red-noise confidence limit', line=dict(width=2, dash='dash', color='red')))
            
        # 设置图形属性
        psd_fig.update_layout(
            title={
            'text': "Power Spectrum",
            'y': 0.97,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
            },
            title_font=dict(family="harding", size=24, weight='bold'),
            xaxis=dict(
                title='Period (Years)',
                type='log',
                tickmode='array',
                tickvals=xticks,
                ticktext=xticklabels
            ),
            yaxis=dict(
                title='Power'
            ),
            legend=dict(yanchor="top", y=0.96, xanchor="right", x=0.96,bgcolor='rgba(0,0,0,0)',font = dict(family = "Arial", size = 17)),
            margin=dict(l=40, r=40, t=35, b=30),
            template="simple_white",
            font=dict(family="Arial", size=18),
            hovermode='x unified'
            )
    return xy_fig, RI.to_dict(), signal_yearST0, signal_yearED0, psd_fig

# 定义回调函数，根据用户选择更新图表
@app.callback([Output('graphs-container', 'children'),
               Output('output-container', 'children')
               ],
            Input('submit_button', 'n_clicks'),
            [State('stored-data', 'data'),
            State('stored-signal_yearST0', 'data'),
            State('stored-signal_yearED0', 'data'),
            State('RI_time_sel', 'value'),
            State('RI_frequeny_dropdown', 'value'),
            State('RI_preprocess_dropdown', 'value'),
            State('CI_preprocess_dropdown', 'value'),
            State('RI_detrend_checklist', 'value'),
            State('CI_detrend_checklist', 'value'),
            State('signal_yearST', 'value'),
            State('signal_yearED', 'value'),
            State('RI_time_scale_dropdown', 'value'),
            State('CI_time_scale_dropdown', 'value'),
            State('same_filter_method', 'value'),
            State('filter_method_dropdown', 'value'),
            State('filter_type_dropdown', 'value'),
            State('Cutoff1', 'value'),
            State('Cutoff2', 'value'),
            State('Cutoff_already', 'value'),
            State('Corr_dropdown','value'),
            State('lag_time', 'value'),
            State('window_time', 'value'),
            State('output-type','value'),
            State('climate-index-dropdown','value')
            ] 
)
def update_graphs(n_clicks, stored_data, signal_yrST0, signal_yrED0, RI_time_sel_options, RI_frequeny, RI_preprocess_method, CI_preprocess_method, RI_detrend_options, CI_detrend_options, signal_yearST, signal_yearED, RI_time_scale, CI_time_scale, same_filter, fil_method, fil_type, Cutoff1, Cutoff2, RI_already_cutoff, Corr_Coeff, mLAG, sliding_window, output_type,index_sel):
    if stored_data is None:
        return "", "Status: No input signal now!"
    elif n_clicks > 0:
        # 从字典转换回 xarray DataArray
        RI = xr.DataArray.from_dict(stored_data)
        # 重新赋值时间维度
        if RI_frequeny == 'year':
            RItime = xr.cftime_range(start=f"{signal_yrST0}-01-01",freq="YE", periods= (signal_yrED0 - signal_yrST0 + 1)) # yearly
        else:
            RItime = xr.cftime_range(start=f"{signal_yrST0}-01-01", freq="MS", periods=(signal_yrED0 - signal_yrST0 + 1) * 12) # monthly
        RI['time'] = RItime

        if 'orgin' in RI_time_sel_options:
            RI_sel = RI 
        else: #截取自定义时间
            RI_sel = RI.sel(time=slice(str(signal_yearST),str(signal_yearED)))

        climate_indices = list(indices_info.keys())
        correlation_results = {}

        # 遍历所有气候指数
        def process_index(selected_index):
            # 加载选定的气候指数
            CI = txt_climate_indices_load(indices_info[selected_index]['short_name'])
            if 'orgin' in RI_time_sel_options:
                if same_filter == "Samefilter":  
                    CI_sel = CI.sel(time=slice(str(signal_yrST0), str(signal_yrED0)))
                else:
                    runave_time = int((RI_already_cutoff-1)/2)
                    CI_sel = CI.sel(time=slice(str(signal_yrST0-runave_time), str(signal_yrED0+runave_time)))
            else: #截取自定义时间
                if same_filter == "Samefilter":  
                    CI_sel = CI.sel(time=slice(str(signal_yearST), str(signal_yearED)))
                else:
                    runave_time = int((RI_already_cutoff-1)/2)
                    CI_sel = CI.sel(time=slice(str(signal_yearST-runave_time), str(signal_yearED+runave_time)))

            # 处理RI时间尺度选择的逻辑
            if RI_time_scale == 'year':
                RI_freq = gc.calendar_average(RI_sel, freq="year")
            elif RI_time_scale == 'MAM':
                RI_freq = gc.climatologies.month_to_season(RI_sel, 'MAM')
            elif RI_time_scale == 'JJA':
                RI_freq = gc.climatologies.month_to_season(RI_sel, 'JJA')
            elif RI_time_scale == 'SON':
                RI_freq = gc.climatologies.month_to_season(RI_sel, 'SON')
            elif RI_time_scale == 'DJF':
                RI_freq = gc.climatologies.month_to_season(RI_sel, 'DJF')
            elif RI_time_scale == 'origin':
                RI_freq = RI_sel

            # print(CI_sel)
            # 处理CI时间尺度选择的逻辑
            if CI_time_scale == 'year':
                CI_freq = gc.calendar_average(CI_sel, freq="year")
            elif CI_time_scale == 'MAM':
                CI_freq = gc.climatologies.month_to_season(CI_sel, 'MAM')
            elif CI_time_scale == 'JJA':
                CI_freq = gc.climatologies.month_to_season(CI_sel, 'JJA')
            elif CI_time_scale == 'SON':
                CI_freq = gc.climatologies.month_to_season(CI_sel, 'SON')
            elif CI_time_scale == 'DJF':
                CI_freq = gc.climatologies.month_to_season(CI_sel, 'DJF')
            elif CI_time_scale == 'origin':
                CI_freq = CI_sel
            # print(CI_freq.time)
            # print(RI_freq.time)
            if same_filter == "Samefilter":  
                if len(CI_freq.time) != len(RI_freq):
                    print(f"Time coverage not same for {indices_info[selected_index]['short_name']}, skip1!")
                    return None # 输出None，继续下一个  
            
            if np.any(np.isnan(CI_freq)) or np.any(CI_freq == -999): ##排除包含缺测数据的气候指数
                return None
            
            # 数据预处理
            CI_preprocessed = preprocess_data(CI_freq, CI_preprocess_method)
            RI_preprocessed = preprocess_data(RI_freq, RI_preprocess_method)

            # 去趋势
            if 'detrend' in RI_detrend_options:
                RI_preprocessed = signal.detrend(RI_preprocessed)
            if 'detrend' in CI_detrend_options:
                CI_preprocessed = signal.detrend(CI_preprocessed)

            if same_filter == "Samefilter":
                # 滤波filter method
                if fil_method == 'nofilter':
                    CI_filtered = CI_preprocessed
                    RI_filtered = RI_preprocessed
                elif fil_method == 'butterworth':
                    if fil_type in ['high', 'low']:
                        CI_filtered = butterworth_filter(CI_preprocessed, order=3, filter_type=fil_type, cutoff=2/Cutoff1)
                        RI_filtered = butterworth_filter(RI_preprocessed, order=3, filter_type=fil_type, cutoff=2/Cutoff1)
                    else: # band 
                        CI_filtered = butterworth_filter(CI_preprocessed, order=3, filter_type=fil_type, cutoff=[2/Cutoff2, 2/Cutoff1])
                        RI_filtered = butterworth_filter(RI_preprocessed, order=3, filter_type=fil_type, cutoff=[2/Cutoff2, 2/Cutoff1])
                elif fil_method == 'movingaverage':
                    CI_preprocessed = xr.DataArray(CI_preprocessed, dims="time", coords={"time": RI_freq['time'].values})
                    RI_preprocessed = xr.DataArray(RI_preprocessed, dims="time", coords={"time": RI_freq['time'].values})
                    CI_filtered = movingaverage_filter(CI_preprocessed, Cutoff1, filter_type=fil_type)
                    RI_filtered = movingaverage_filter(RI_preprocessed, Cutoff1, filter_type=fil_type)
                elif fil_method == 'lanczos':
                    CI_filtered = lanczos_filter(CI_preprocessed, window=121, filter_type=fil_type, cutoff=1/Cutoff1)
                    RI_filtered = lanczos_filter(RI_preprocessed, window=121, filter_type=fil_type, cutoff=1/Cutoff1)
                elif fil_method == 'fourier':
                    CI_filtered = fourier_filter(CI_preprocessed, freq=1, filter_type=fil_type, cutoff=1/Cutoff1)
                    RI_filtered = fourier_filter(RI_preprocessed, freq=1, filter_type=fil_type, cutoff=1/Cutoff1)

                if len(CI_filtered) != len(RI_filtered):
                    print(f"Time coverage not same for {indices_info[selected_index]['short_name']}, skip2!")
                    return None # 输出None，继续下一个   

                #如果为滑动平均的还需要再对时间维度去除NaN值
                if fil_method == 'movingaverage':
                    RI_filtered = RI_filtered.dropna(dim="time")
                    CI_filtered = CI_filtered.dropna(dim="time") 
                else:
                    RI_filtered = xr.DataArray(RI_filtered, dims="time", coords={"time": RI_freq['time'].values})
                    CI_filtered = xr.DataArray(CI_filtered, dims="time", coords={"time": RI_freq['time'].values}) ### 在上述检查长度相等情况下，赋予同一个时间序列，避免相同年份月份不一致的情况

            else: #no same filter, only consider climate indices
                RI_filtered = RI_preprocessed #Input Signal不滤波
                if fil_method == 'nofilter':
                    CI_filtered = CI_preprocessed
                elif fil_method == 'butterworth':
                    if fil_type in ['high', 'low']:
                        CI_filtered = butterworth_filter(CI_preprocessed, order=3, filter_type=fil_type, cutoff=2/Cutoff1)
                    else: # band 
                        CI_filtered = butterworth_filter(CI_preprocessed, order=3, filter_type=fil_type, cutoff=[2/Cutoff2, 2/Cutoff1])
                elif fil_method == 'movingaverage':
                    CI_preprocessed = xr.DataArray(CI_preprocessed, dims="time", coords={"time": CI_freq['time'].values})
                    CI_filtered = movingaverage_filter(CI_preprocessed, Cutoff1, filter_type=fil_type)
                elif fil_method == 'lanczos':
                    CI_filtered = lanczos_filter(CI_preprocessed, window=121, filter_type=fil_type, cutoff=1/Cutoff1)
                elif fil_method == 'fourier':
                    CI_filtered = fourier_filter(CI_preprocessed, freq=1, filter_type=fil_type, cutoff=1/Cutoff1)

                if fil_method == 'movingaverage':
                    RI_filtered = RI_filtered.dropna(dim="time")
                    CI_filtered = CI_filtered.dropna(dim="time") 
                    CI_filtered['time'] = RI_filtered['time']
                    # print(CI_filtered.time)
                    # print(RI_filtered.time)
                else:
                    RI_filtered = xr.DataArray(RI_filtered, dims="time", coords={"time": RI_freq['time'].values})
                    CI_filtered = xr.DataArray(CI_filtered, dims="time", coords={"time": RI_freq['time'].values}) ### 在上述检查长度相等情况下，赋予同一个时间序列，避免相同年份月份不一致的情况           
                if len(CI_filtered) != len(RI_filtered):
                    print(f"Time coverage not same for {indices_info[selected_index]['short_name']}, skip!")
                    return None # 输出None，继续下一个   
                
            if Corr_Coeff == "Corr":  # 计算相关系数
                pearson_r = xs.pearson_r(CI_filtered, RI_filtered)
                if fil_type in ['low','band']:
                    Eeff = corr_funcs.ESS_DS1976(CI_filtered, RI_filtered)
                    p = corr_funcs.ESS_to_p_value(Eeff,pearson_r) 
                else: # high
                    p = xs.pearson_r_p_value(CI_filtered, RI_filtered)

                correlation_results[indices_info[selected_index]['short_name']] = {
                'CI':CI_filtered,
                'RI':RI_filtered,
                'Pearson_r': pearson_r.data,
                'p':p
                }    
            elif Corr_Coeff == "Llr":
                # if LAG > len(CI_filtered)/2:# 设置最大滞后
                lags, lagged_corrs = corr_funcs.lagged_correlation(CI_filtered, RI_filtered, mLAG)
                correlation_results[indices_info[selected_index]['short_name']] = {
                'LLR': lagged_corrs
                # 'DS1976_p':DS1976_p
                }
            elif Corr_Coeff == "Slc":
                sliding_corrs = corr_funcs.sliding_correlation(CI_filtered, RI_filtered, sliding_window)
                r_value = corr_funcs.sig_to_r_value(len(RI_filtered), alpha=0.05)
                correlation_results[indices_info[selected_index]['short_name']] = {
                'SLC': sliding_corrs,
                'r_value': r_value
                }
            return correlation_results
        
        ### 单个绘图 ###
        if output_type == "single":
            correlation_result = process_index(index_sel)
            if correlation_result == None:
                return "", f"Status: The {index_sel} index does not match the time coverage of input signal!"
            else:
                fig = go.Figure()
                if same_filter == "Samefilter": 
                    if fil_method == 'movingaverage':
                        if 'orgin' in RI_time_sel_options:
                            ma_yearST, ma_myearED = int(signal_yrST0+(Cutoff1-1)/2),int(signal_yrED0-(Cutoff1-1)/2)
                            if RI_frequeny == 'month' and RI_time_scale == "origin":
                                xTrue = np.arange(ma_yearST, ma_myearED + 1, 1/12)
                            else:
                                xTrue = np.arange(ma_yearST, ma_myearED + 1, 1)
                        else:
                            ma_yearST, ma_myearED = int(signal_yearST+(Cutoff1-1)/2),int(signal_yearED-(Cutoff1-1)/2)
                            if RI_frequeny == 'month' and RI_time_scale == "origin":
                                xTrue = np.arange(ma_yearST, ma_myearED + 1, 1/12)
                            else:
                                xTrue = np.arange(ma_yearST, ma_myearED + 1, 1)      
                    else:
                        if 'orgin' in RI_time_sel_options:
                            if RI_frequeny == 'month' and RI_time_scale == "origin":
                                xTrue = np.arange(signal_yrST0, signal_yrED0 + 1, 1/12)
                            else:
                                xTrue = np.arange(signal_yrST0, signal_yrED0 + 1, 1)
                        else:
                            if RI_frequeny == 'month' and RI_time_scale == "origin":
                                xTrue = np.arange(signal_yearST, signal_yearED + 1, 1/12)
                            else:
                                xTrue = np.arange(signal_yearST, signal_yearED + 1, 1)
                else: 
                    if 'orgin' in RI_time_sel_options:
                        if RI_frequeny == 'month' and RI_time_scale == "origin":
                            xTrue = np.arange(signal_yrST0, signal_yrED0 + 1, 1/12)
                        else:
                            xTrue = np.arange(signal_yrST0, signal_yrED0 + 1, 1)
                    else:
                        if RI_frequeny == 'month' and RI_time_scale == "origin":
                            xTrue = np.arange(signal_yearST, signal_yearED + 1, 1/12)
                        else:
                            xTrue = np.arange(signal_yearST, signal_yearED + 1, 1)
                
                if Corr_Coeff == "Corr":  # 根据 Pearson_r 的绝对值从大到小排序
                    pearson_r = np.round(correlation_result[index_sel]['Pearson_r'], 3)
                    p_value = np.round(correlation_result[index_sel]['p'], 3)
                    cs_RI = CubicSpline(xTrue, correlation_result[index_sel]['RI'])
                    cs_CI = CubicSpline(xTrue, correlation_result[index_sel]['CI'])

                    IFa = pyleo.utils.causality.liang_causality(correlation_result[index_sel]['RI'].data, correlation_result[index_sel]['CI'].data, npt=1, signif_test='isospec', nsim=1000, qs=[0.95])

                    IFb = pyleo.utils.causality.liang_causality(correlation_result[index_sel]['CI'].data, correlation_result[index_sel]['RI'].data, npt=1, signif_test='isospec', nsim=1000, qs=[0.95])

                    if same_filter == "Samefilter": 
                        if fil_method == 'movingaverage':
                            if 'orgin' in RI_time_sel_options:
                                ma_yearST, ma_myearED = int(signal_yrST0+(Cutoff1-1)/2),int(signal_yrED0-(Cutoff1-1)/2)
                                xCubic = np.arange(ma_yearST, ma_myearED + 0.1, 0.2)    
                            else:
                                ma_yearST, ma_myearED = int(signal_yearST+(Cutoff1-1)/2),int(signal_yearED-(Cutoff1-1)/2)
                                xCubic = np.arange(ma_yearST, ma_myearED + 0.1, 0.2)    
                        else:
                            if 'orgin' in RI_time_sel_options:
                                xCubic = np.arange(signal_yrST0, signal_yrED0 + 0.1, 0.2)    
                            else:
                                xCubic = np.arange(signal_yearST, signal_yearED + 0.1, 0.2)    
                    else:
                        if 'orgin' in RI_time_sel_options:
                            xCubic = np.arange(signal_yrST0, signal_yrED0 + 0.1, 0.2)    
                        else:
                            xCubic = np.arange(signal_yearST, signal_yearED + 0.1, 0.2)    

                    fig.add_trace(go.Scatter(x=xCubic, y=cs_CI(xCubic), mode='lines', name=index_sel, line=dict(color='blue', width=3)))
                    fig.add_trace(go.Scatter(x=xCubic, y=cs_RI(xCubic), mode='lines', name='RI', line=dict(color='red', width=3)))
                    fig.add_trace(go.Scatter(
                        x=[xCubic[0], xCubic[-1]],
                        y=[0, 0],
                        mode='lines',
                        line=dict(color='black', width=0.45, dash='dash'),
                        showlegend=False
                    )),

                    IFa_T = np.round(IFa['T21'],3)
                    IFb_T = np.round(IFb['T21'],3)                  
                    IFa_T_sig = IFa['T21'] > IFa['T21_noise'][0]
                    IFb_T_sig = IFb['T21'] > IFb['T21_noise'][0]
                    IFa_tau = np.round(IFa['tau21'],3)
                    IFb_tau = np.round(IFb['tau21'],3)
                    IFa_tau_sig = IFa['tau21'] > IFa['tau21_noise'][0]
                    IFb_tau_sig = IFb['tau21'] > IFb['tau21_noise'][0]

                    fig.update_layout(
                        height=600,
                        title={
                            'text': f"Correlation <br> Input Signal [{RI_time_scale}] VS {index_sel} [{CI_time_scale}] <br> Pearson-r={pearson_r} p-value={p_value} <br>" + "IF→: T=%s[%s] tau=%s[%s] IF←: T=%s[%s] tau=%s[%s]"%(IFb_T,IFb_T_sig,IFb_tau,IFb_tau_sig,IFa_T,IFa_T_sig,IFa_tau,IFa_tau_sig),
                            'y': 0.97,
                            'x': 0.5,
                            'xanchor': 'center',
                            'yanchor': 'top'
                        },
                        title_font=dict(size=24, weight='bold'),
                        xaxis_title='Year',
                        yaxis_title='Correlation',
                        showlegend=False,
                        template="simple_white",
                        font=dict( family="Arial", size=18),
                        hovermode='x unified'
                        )

                elif Corr_Coeff == "Llr":
                    lags = np.arange(-mLAG, mLAG + 1)
                    LLR_cubic = CubicSpline(lags, correlation_result[index_sel]['LLR'])
                    xCubic = np.arange(-mLAG, mLAG + 0.2, 0.2)

                    # 添加原始 LLR 曲线
                    fig.add_trace(go.Scatter(x=lags,y=correlation_result[index_sel]['LLR'],
                        mode='lines',line=dict(color='blue', width=2),name='Original LLR'))
                    # 添加平滑后的 LLR 曲线
                    fig.add_trace(go.Scatter(x=xCubic,y=LLR_cubic(xCubic),
                        mode='lines', line=dict(color='red', width=3),name='Smoothed LLR'))
                    # 添加垂直线和水平线
                    fig.add_trace(go.Scatter(
                        x=[0, 0],
                        y=[-1, 1],
                        mode='lines',
                        line=dict(color='black', width=1.5),
                        showlegend=False
                    ))
                    fig.add_trace(go.Scatter(
                        x=[-mLAG, mLAG],
                        y=[0, 0],
                        mode='lines',
                        line=dict(color='black', width=1, dash='dash'),
                        showlegend=False
                    ))

                    fig.update_layout(
                        height=600,
                        title={
                            'text': f"Lead-lagged Correlation <br> Input Signal ({RI_time_scale}) VS {index_sel} [{CI_time_scale}]",
                            'y': 0.92,
                            'x': 0.5,
                            'xanchor': 'center',
                            'yanchor': 'top'
                        },
                        title_font=dict(size=24, weight='bold'),
                        xaxis_title='Lag (Years)',
                        yaxis_title='Correlation',
                        showlegend=False,
                        yaxis_range=[-1,1],
                        template="simple_white",
                        font=dict( family="Arial", size=18),
                        hovermode='x unified'
                        )
                    
                elif Corr_Coeff == "Slc":
                    critical_r = correlation_result[index_sel]['r_value']
                    # 添加原始 SLC 曲线
                    print(xTrue)
                    fig.add_trace(go.Scatter(x=xTrue,y=correlation_result[index_sel]['SLC'],
                        mode='lines',line=dict(color='#2CA02C', width=3),name='Sliding Corr',
                        showlegend=False
                    ))
                    #添加显著性检验（未考虑有效自由度）
                    fig.add_trace(go.Scatter(
                        x=[xTrue[0], xTrue[-1]],
                        y=[critical_r, critical_r],
                        mode='lines',
                        line=dict(color='black', width=1, dash='dash'),
                        showlegend=False
                    ))
                    fig.add_trace(go.Scatter(
                        x=[xTrue[0], xTrue[-1]],
                        y=[-critical_r, -critical_r],
                        mode='lines',
                        line=dict(color='black', width=1, dash='dash'),
                        showlegend=False
                    ))

                    pdo_phase_change_years = [1895, 1912, 1922, 1945, 1976, 1998, 2014]
                    amo_phase_change_years = [1892, 1926, 1962, 1998]
                    # iobm_phase_change_years = [1946, 1976]

                    # 使用列表推导式筛选出在 xTrue 范围内的年份
                    pdo_filtered = [year for year in pdo_phase_change_years if xTrue[0] <= year <= xTrue[-1]]
                    amo_filtered = [year for year in amo_phase_change_years if xTrue[0] <= year <= xTrue[-1]]

                    # 获取 correlation_result[index_sel]['SLC'] 中的最大值和最小值
                    max_corr = max(correlation_result[index_sel]['SLC'].dropna(dim="time"))
                    min_corr = min(correlation_result[index_sel]['SLC'].dropna(dim="time"))

                    # 比较最大值和最小值与 critical_r 和 -critical_r 的大小
                    max_value = max(max_corr, critical_r, -critical_r)
                    min_value = min(min_corr, critical_r, -critical_r)

                    for year in pdo_filtered:
                        fig.add_trace(go.Scatter(
                            x=[year, year],
                            y=[min_value, max_value],  # 使用CI曲线的最小和最大值作为参考线的上下限
                            mode='lines',
                            opacity=0.5,
                            line=dict(color='aqua', width=15, dash='dot'),  # 铅直线的样式
                            name="PDO-PC",  # 设置图例名称，便于控制是否显示
                            legendgroup="PDO-PC",  # 共享同一个图例
                            showlegend=(year == pdo_filtered[0])  # 仅显示第一条线的图例
                        ))
                    for year in amo_filtered:
                        fig.add_trace(go.Scatter(
                            x=[year, year],
                            y=[min_value, max_value], 
                            mode='lines',
                            opacity=0.5,
                            line=dict(color='coral', width=15, dash='dot'),  # 铅直线的样式
                            name="AMO-PC",  # 设置图例名称，便于控制是否显示
                            legendgroup="AMO-PC",  # 共享同一个图例
                            showlegend=(year == amo_filtered[0])  # 仅显示第一条线的图例
                        ))

                    fig.update_layout(
                        height=600,
                        title={
                            'text': f"Sliding Correlation <br> Input Signal ({RI_time_scale}) VS {index_sel} [{CI_time_scale}]",
                            'y': 0.92,
                            'x': 0.5,
                            'xanchor': 'center',
                            'yanchor': 'top'
                        },
                        title_font=dict(size=24, weight='bold'),
                        xaxis_title='Year',
                        yaxis_title='Correlation',
                        showlegend=True,
                        legend=dict(orientation="h", yanchor="top", y=-0.2, xanchor="center", x=0.5,bgcolor='rgba(0,0,0,0)',font = dict(family = "Arial", size = 18)),
                        template="simple_white",
                        font=dict(family="Arial", size=18),
                        hovermode='x unified'
                        )

                return dcc.Graph(figure=fig), f"Status: Detecting and analyzing the input signal with {index_sel} is done!"

        ### 批量绘图 ###
        elif output_type == "batch":

            # 定义一个辅助函数，用于处理单个指数并捕获异常
            def safe_process_index(index):
                try:
                    # 调用实际的处理函数 process_index
                    return process_index(index)
                except Exception as e:
                    # 如果遇到错误，返回错误信息和出错的指数
                    print(f"Error processing index {index}: {e}")
                    return None  # 可以返回 None 或其他占位符，表示该指数处理失败

            # 使用并行计算，跳过有缺测值的指数
            correlation_results = Parallel(n_jobs=-1)(delayed(safe_process_index)(index) for index in climate_indices)    
            # 
            # correlation_results = Parallel(n_jobs=-1)(delayed(process_index)(index) for index in climate_indices) 

            # 移除 None 值 与 过滤掉处理失败的结果（None 值）
            filtered_results = [result for result in correlation_results if result is not None]
            # 将列表转换为字典供作图时筛选
            dict_result = {key: value for item in filtered_results for key, value in item.items()}
            # 转换格式并提取数据
            formatted_results = [(list(d.keys())[0], d[list(d.keys())[0]]) for d in filtered_results]
            if Corr_Coeff == "Corr":  # 根据 Pearson_r 的绝对值从大到小排序  
                sorted_indices = sorted(formatted_results, key=lambda x: abs(x[1]['Pearson_r']), reverse=True) 
            elif Corr_Coeff == "Llr":
                sorted_indices = sorted(formatted_results,key=lambda x: abs(np.array(x[1]['LLR'])[mLAG])) # 
            #   sorted_indices = sorted(formatted_results,key=lambda x: max(abs(np.array(x[1]['LLR']))), reverse=True)
            elif Corr_Coeff == "Slc":
                sorted_indices = formatted_results

            subplot_titles = []
            for i, (index_name, results) in enumerate(sorted_indices):
                if Corr_Coeff == "Corr":  # 根据 Pearson_r 的绝对值从大到小排序
                    pearson_r = np.round(dict_result[index_name]['Pearson_r'], 3)
                    p_value = np.round(dict_result[index_name]['p'], 3)
                    subplot_titles.append(f"{index_name}<br>Pearson_r={pearson_r}   p-value={p_value}")
                elif Corr_Coeff == "Llr":
                    subplot_titles.append(f'Positive: Input Signal leads {index_name}')
                elif Corr_Coeff == "Slc":
                    subplot_titles.append(f'Sliding_r with {index_name}')
                    # sliding_r = np.round(dict_result[index_name]['Sliding_r'], 3)

            num_indices = len(sorted_indices)
            print(f"Detected {num_indices} climate indices")
            if num_indices == 0:
                print("No climate indices match the time coverage of input signal!")
                return "", "Status: No climate indices match the time coverage of input signal!"
            
            n_rows = (num_indices + 2) // 3  # 每行三个子图，向下取整
            fig = make_subplots(rows=n_rows, cols=3, shared_xaxes=False,subplot_titles=subplot_titles)

            if same_filter == "Samefilter": 
                if fil_method == 'movingaverage':
                    if 'orgin' in RI_time_sel_options:
                        ma_yearST, ma_myearED = int(signal_yrST0+(Cutoff1-1)/2),int(signal_yrED0-(Cutoff1-1)/2)
                        if RI_frequeny == 'month' and RI_time_scale == "origin":
                            xTrue = np.arange(ma_yearST, ma_myearED + 1, 1/12)
                        else:
                            xTrue = np.arange(ma_yearST, ma_myearED + 1, 1)
                    else:
                        ma_yearST, ma_myearED = int(signal_yearST+(Cutoff1-1)/2),int(signal_yearED-(Cutoff1-1)/2)
                        if RI_frequeny == 'month' and RI_time_scale == "origin":
                            xTrue = np.arange(ma_yearST, ma_myearED + 1, 1/12)
                        else:
                            xTrue = np.arange(ma_yearST, ma_myearED + 1, 1)      
                else:
                    if 'orgin' in RI_time_sel_options:
                        if RI_frequeny == 'month' and RI_time_scale == "origin":
                            xTrue = np.arange(signal_yrST0, signal_yrED0 + 1, 1/12)
                        else:
                            xTrue = np.arange(signal_yrST0, signal_yrED0 + 1, 1)
                    else:
                        if RI_frequeny == 'month' and RI_time_scale == "origin":
                            xTrue = np.arange(signal_yearST, signal_yearED + 1, 1/12)
                        else:
                            xTrue = np.arange(signal_yearST, signal_yearED + 1, 1)
            else: 
                if 'orgin' in RI_time_sel_options:
                    if RI_frequeny == 'month' and RI_time_scale == "origin":
                        xTrue = np.arange(signal_yrST0, signal_yrED0 + 1, 1/12)
                    else:
                        xTrue = np.arange(signal_yrST0, signal_yrED0 + 1, 1)
                else:
                    if RI_frequeny == 'month' and RI_time_scale == "origin":
                        xTrue = np.arange(signal_yearST, signal_yearED + 1, 1/12)
                    else:
                        xTrue = np.arange(signal_yearST, signal_yearED + 1, 1)

            # 标记PDO和AMO图例是否已显示
            pdo_legend_shown = True
            amo_legend_shown = True

            for i, (index_name, results) in enumerate(sorted_indices):
                CI_name = index_name    
                if Corr_Coeff == "Corr":  # 根据 Pearson_r 的绝对值从大到小排序
                    
                    cs_RI = CubicSpline(xTrue, dict_result[CI_name]['RI'])
                    cs_CI = CubicSpline(xTrue, dict_result[CI_name]['CI'])

                    if same_filter == "Samefilter": 
                        if fil_method == 'movingaverage':
                            if 'orgin' in RI_time_sel_options:
                                ma_yearST, ma_myearED = int(signal_yrST0+(Cutoff1-1)/2),int(signal_yrED0-(Cutoff1-1)/2)
                                xCubic = np.arange(ma_yearST, ma_myearED + 0.1, 0.2)    
                            else:
                                ma_yearST, ma_myearED = int(signal_yearST+(Cutoff1-1)/2),int(signal_yearED-(Cutoff1-1)/2)
                                xCubic = np.arange(ma_yearST, ma_myearED + 0.1, 0.2)    
                        else:
                            if 'orgin' in RI_time_sel_options:
                                xCubic = np.arange(signal_yrST0, signal_yrED0 + 0.1, 0.2)    
                            else:
                                xCubic = np.arange(signal_yearST, signal_yearED + 0.1, 0.2)    
                    else:
                        if 'orgin' in RI_time_sel_options:
                            xCubic = np.arange(signal_yrST0, signal_yrED0 + 0.1, 0.2)    
                        else:
                            xCubic = np.arange(signal_yearST, signal_yearED + 0.1, 0.2)    

                    nrow = i // 3 + 1  # 当前子图的行
                    ncol = i % 3 + 1   # 当前子图的列        

                    fig.add_trace(go.Scatter(x=xCubic, y=cs_CI(xCubic), mode='lines', name=CI_name, line=dict(color='blue')), row=nrow, col=ncol)
                    fig.add_trace(go.Scatter(x=xCubic, y=cs_RI(xCubic), mode='lines', name='RI', line=dict(color='red')), row=nrow, col=ncol)
                    fig.add_trace(go.Scatter(
                        x=[xCubic[0], xCubic[-1]],
                        y=[0, 0],
                        mode='lines',
                        line=dict(color='black', width=0.45, dash='dash'),
                        showlegend=False
                    ), row=nrow, col=ncol),
                    # 更新图形布局，设置大标题的样式
                    fig.update_layout(
                    height=300 * n_rows,
                    title_text=f"Input Signal [{RI_time_scale}] VS Climate Indices [{CI_time_scale}] (Avail: {len(sorted_indices)}/{len(indices_info)})",
                    title_font=dict(family="harding", size=24, weight='bold'),  # 设置标题字号和加粗
                    title_x=0.5,  # 使标题居中
                    showlegend=False,
                    template="simple_white",
                    hovermode='x unified')


                elif Corr_Coeff == "Llr":
                    lags = np.arange(-mLAG, mLAG + 1)
                    LLR_cubic = CubicSpline(lags, dict_result[CI_name]['LLR'])
                    xCubic = np.arange(-mLAG, mLAG + 0.2, 0.2)

                    nrow = i // 3 + 1  # 当前子图的行
                    ncol = i % 3 + 1   # 当前子图的列 

                    # 添加原始 LLR 曲线
                    fig.add_trace(go.Scatter(x=lags,y=dict_result[CI_name]['LLR'],
                        mode='lines',line=dict(color='blue', width=2),name='Original LLR'), row=nrow, col=ncol)
                    # 添加平滑后的 LLR 曲线
                    fig.add_trace(go.Scatter(x=xCubic,y=LLR_cubic(xCubic),
                        mode='lines', line=dict(color='red', width=3),name='Smoothed LLR'), row=nrow, col=ncol)
                    # 添加垂直线和水平线
                    fig.add_trace(go.Scatter(
                        x=[0, 0],
                        y=[-1.2, 1.2],
                        mode='lines',
                        line=dict(color='black', width=1.5),
                        showlegend=False
                    ), row=nrow, col=ncol)
                    fig.add_trace(go.Scatter(
                        x=[-mLAG, mLAG],
                        y=[0, 0],
                        mode='lines',
                        line=dict(color='black', width=1, dash='dash'),
                        showlegend=False
                    ), row=nrow, col=ncol)

                    fig.update_yaxes(range=[-1.1,1.1])
                    fig.update_layout(
                    height=300 * n_rows,
                    title_text=f"Input Signal [{RI_time_scale}] VS Climate Indices [{CI_time_scale}] (Avail: {len(sorted_indices)}/{len(indices_info)})",
                    title_font=dict(family="harding", size=24, weight='bold'),  # 设置标题字号和加粗
                    title_x=0.5,  # 使标题居中
                    showlegend=False,
                    template="simple_white",
                    hovermode='x unified')
            
                elif Corr_Coeff == "Slc":
                    critical_r = dict_result[index_name]['r_value']
                    # print(critical_r)
                    nrow = i // 3 + 1  # 当前子图的行
                    ncol = i % 3 + 1   # 当前子图的列 

                    # 添加原始 SLC 曲线
                    fig.add_trace(go.Scatter(x=xTrue,y=dict_result[CI_name]['SLC'],
                        mode='lines',line=dict(color='#2CA02C', width=2.5),name='Sliding Corr',
                        showlegend=False), row=nrow, col=ncol)
                    #添加显著性检验（未考虑有效自由度）
                    fig.add_trace(go.Scatter(
                        x=[xTrue[0], xTrue[-1]],
                        y=[critical_r, critical_r],
                        mode='lines',
                        line=dict(color='black', width=1, dash='dash'),
                        showlegend=False
                    ), row=nrow, col=ncol)
                    fig.add_trace(go.Scatter(
                        x=[xTrue[0], xTrue[-1]],
                        y=[-critical_r, -critical_r],
                        mode='lines',
                        line=dict(color='black', width=1, dash='dash'),
                        showlegend=False
                    ), row=nrow, col=ncol)

                    pdo_phase_change_years = [1895, 1912, 1922, 1945, 1976, 1998, 2014]
                    amo_phase_change_years = [1892, 1926, 1962, 1998]
                    # iobm_phase_change_years = [1946, 1976]

                    # 使用列表推导式筛选出在 xTrue 范围内的年份
                    pdo_filtered = [year for year in pdo_phase_change_years if xTrue[0] <= year <= xTrue[-1]]
                    amo_filtered = [year for year in amo_phase_change_years if xTrue[0] <= year <= xTrue[-1]]

                    # 获取 dict_result[CI_name]['SLC']中的最大值和最小值
                    max_corr = max(dict_result[CI_name]['SLC'].dropna(dim="time"))
                    min_corr = min(dict_result[CI_name]['SLC'].dropna(dim="time"))

                    # 比较最大值和最小值与 critical_r 和 -critical_r 的大小
                    max_value = max(max_corr, critical_r, -critical_r)
                    min_value = min(min_corr, critical_r, -critical_r)

                    # 添加PDO位相转换年的铅直参考线
                    for year in pdo_filtered:
                        fig.add_trace(go.Scatter(
                            x=[year, year],
                            y=[min_value, max_value],
                            mode='lines',
                            opacity=0.4,
                            line=dict(color='aqua', width=8, dash='dot'),
                            name="PDO-PC",
                            legendgroup="PDO-PC",
                            showlegend=pdo_legend_shown  # 如果未显示过图例，则显示
                        ), row=nrow, col=ncol)
                        pdo_legend_shown = False  # 标记PDO图例已显示

                    # 添加AMO位相转换年的铅直参考线
                    for year in amo_filtered:
                        fig.add_trace(go.Scatter(
                            x=[year, year],
                            y=[min_value, max_value],
                            mode='lines',
                            opacity=0.4,
                            line=dict(color='coral', width=8, dash='dot'),
                            name="AMO-PC",
                            legendgroup="AMO-PC",
                            showlegend=amo_legend_shown  # 如果未显示过图例，则显示
                        ), row=nrow, col=ncol)
                        amo_legend_shown = False  # 标记AMO图例已显示

                    # 更新布局
                    fig.update_layout(
                        height=300 * n_rows,
                        title_text=f"Input Signal [{RI_time_scale}] VS Climate Indices [{CI_time_scale}] (Avail: {len(sorted_indices)}/{len(indices_info)})",
                        title_font=dict(family="harding", size=24, weight='bold'),
                        title_x=0.5,
                        title_y=0.995,
                        legend=dict(
                            orientation="h",
                            yanchor="top",
                            y=1.016,
                            xanchor="center",
                            x=0.5,
                            bgcolor='rgba(0,0,0,0)',
                            font=dict(family="Arial", size=18)
                        ),
                        template="simple_white",
                        hovermode='x unified'
                        )

            if Corr_Coeff == "Corr":  # 根据 Pearson_r 的绝对值从大到小排序
                fig.update_xaxes(title_text='Year')
                fig.update_yaxes(title_text='Correlation')
            elif Corr_Coeff == "Llr":
                fig.update_xaxes(title_text='Lag (Years)')
                fig.update_yaxes(title_text='Correlation')
            elif Corr_Coeff == "Slc":
                fig.update_xaxes(title_text='Year')
                fig.update_yaxes(title_text='Correlation')

            return dcc.Graph(figure=fig), "Status: Detecting and analyzing the input signal is done!"

# 运行 Dash 应用
if __name__ == '__main__':  
    webbrowser.open("http://127.0.0.1:8050")# 自动打开web
    app.run(debug=True, port=8050) #本地离线运行
    # app.run(debug=True, host='0.0.0.0', port=8050) #服务器在线运行
