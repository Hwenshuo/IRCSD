import cftime
import numpy as np
import xarray as xr
from txt_load import txt_climate_indices_load, txt_input_signal_load  # 使用已有的加载函数
import pandas as pd

def RI_init(file_path, file_name, RI_frequeny):
    if file_name.endswith('.nc'): 
        RI = xr.open_dataarray(file_path).rename("Input Signal")
    elif file_name.endswith('.txt'):
        RI = txt_input_signal_load(file_path, RI_frequeny).rename("Input Signal")
    elif file_name.endswith('.csv'): 
        RI = pd.read_csv(file_path) #此功能待开发
    # 提取开始和结束年份
    if np.issubdtype(RI['time'].dtype, np.datetime64): #datetime
        get_yearST = int(RI['time'].dt.year.min().values)
        get_yearED = int(RI['time'].dt.year.max().values)
    elif isinstance(RI['time'][0].item(), int):
        get_yearST = int(RI['time'][0].values)
        get_yearED = int(RI['time'][-1].values)
    elif isinstance(RI['time'][0].item(), cftime.DatetimeGregorian):
        get_yearST = RI['time'][0].item().year
        get_yearED = RI['time'][-1].item().year
    else: #datetime
        get_yearST = None
        get_yearED = None
    # 如果频率为年或月，按该频率重新生成时间轴
    if RI_frequeny == 'year':
        RI['time'] = xr.date_range(start=f'{get_yearST}-01-01', periods=len(RI), freq='YE')
    elif RI_frequeny == 'month':
        RI['time'] = xr.date_range(start=f'{get_yearST}-01-01', periods=len(RI), freq='MS')
    return RI, get_yearST, get_yearED
