### import modules ###
import os 
import pandas as pd
import xarray as xr
import sys
xr.set_options(display_expand_data=False)
# Custom modules
from climate_indices_info_NOAA import NOAA_indices_info
from climate_indices_info_NCC import NCC_indices_info
from climate_indices_info_EXT import EXT_indices_info
indices_info = {}
indices_info.update(NOAA_indices_info)
indices_info.update(NCC_indices_info)
indices_info.update(EXT_indices_info)

def txt_climate_indices_load(indices_name):
    """
    load origin txt climate indices to xarray
    """
    # climate_indices_dir = "/home/huangwenshuo/Program/RCSD/data/climate_indices" #linux
    climate_indices_dir = "../data/climate_indices" #windows
    path_list = []
    # 递归获得文件夹和子文件夹下所有文件名
    for root,dirs,files in os.walk(climate_indices_dir):
        for file in files:
            path = os.path.join(root,file)
            # print(path)
            path_list.append(path)
    def find_file_path_by_indices(indices_name, file_list):
        # 创建一个匹配的文件名
        target_file_name = f"{indices_name}.txt"  # 根据你的文件命名规则调整
        for file_path in file_list:
            if target_file_name in file_path:
                return file_path
        return None  # 如果没有找到返回 None
    file_name = indices_info["%s"%indices_name]['file_name']
    full_path = find_file_path_by_indices(file_name, path_list)
    # full_path = os.path.join(climate_indices_dir+"/"++".txt")
    #read time coverage
    years = pd.read_csv(full_path, nrows=1, sep='\s+')
    start_year = int(years.columns[0])
    end_year = int(years.columns[-1])
    print("Loading %s, time coverage: %s-%s"%(indices_name, start_year,end_year))
    #read data value 
    ds = pd.read_csv(full_path,header=None,sep='\s+', skiprows=1,index_col=False,on_bad_lines='skip')
    # ds.set_index(0,inplace=True)
    ds = ds.loc[0:end_year-start_year].iloc[:,1:13].astype(float)
    ds
    #flatten the data
    CItime = xr.cftime_range(start="%s-01-01"%start_year,freq="MS",periods=(end_year+1-start_year)*12)
    climate_indice = xr.DataArray(ds.values.flatten(), dims="time", coords={"time": CItime})
    climate_indice = climate_indice.rename(indices_info["%s"%indices_name]['short_name'])
    return climate_indice

def txt_input_signal_load(file_path, RI_frequeny):
    """
    load origin txt input signal to xarray
    """
    #read time coverage
    years = pd.read_csv(file_path, nrows=1, sep='\s+')
    start_year = int(years.columns[0])
    end_year = int(years.columns[-1])
    #read data value 
    ds = pd.read_csv(file_path, header=None,sep='\s+', skiprows=1,index_col=False)
    if RI_frequeny == 'month':
        ds = ds.loc[0:end_year-start_year].iloc[:,1:13].astype(float)
        RItime = xr.cftime_range(start=f"{start_year}-01-01", freq="MS", periods=(end_year - start_year + 1) * 12) # monthly
    else:#RI_frequeny == 'year':
        ds = ds.loc[0:end_year-start_year].iloc[:,1].astype(float)
        #flatten the data
        RItime = xr.cftime_range(start="%s-01-01"%start_year, freq="YE",periods=(end_year - start_year + 1))
    RI = xr.DataArray(ds.values.flatten(), dims="time", coords={"time": RItime}).rename("Input Singal")
    # ds.set_index(0,inplace=True)
    return RI
