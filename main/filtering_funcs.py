import pandas as pd
import xarray as xr
import numpy as np
import geocat.comp as gc
from scipy import signal
from typing import Union

# Filter a dataset by frequency #

def movingaverage_filter(time_series, wdw, filter_type="low"):

    # Low-pass filter implementation
    if filter_type == 'low':
        filtered_signal = time_series.rolling(time=wdw, center=True).mean()#.dropna(dim="time")
    # High-pass filter implementation
    elif filter_type == 'high':
        # constrcut Lanczos filter weights
        low_pass_signal = time_series.rolling(time=wdw, center=True).mean()#.dropna
        filtered_signal = time_series - low_pass_signal
    # Band-pass filter implementation
    elif filter_type == 'band': 
        raise ValueError("Band pass in moving average filter is disabled now.")
        # low_pass_signal = time_series.rolling(time=wdw[0], center=True).mean()#.dropna(dim="time")
        # high_pass_signal = time_series - time_series.rolling(time=wdw[1], center=True).mean()#.dropna(dim="time")
        # filtered_signal = (time_series - low_pass_signal) - low_pass_signal
    else:
        raise ValueError("Unsupported filter type. Choose 'low', 'high', or 'band'.")
    return filtered_signal

def butterworth_filter(time_series, order=3, filter_type='low',cutoff=None):
    if filter_type in ['high', 'low'] and cutoff is None:
        raise ValueError("Cutoff frequency must be provided for highpass and lowpass filters.")
    if filter_type == 'band' and (cutoff is None or len(cutoff) != 2):
        raise ValueError("A tuple of two cutoff frequencies must be provided for bandpass filters.")  
    # Low-pass filter implementation
    if filter_type == 'low':
        b, a = signal.butter(order, cutoff, btype='lowpass')
    # High-pass filter implementation
    elif filter_type == 'high':
        b, a = signal.butter(order, cutoff, btype='highpass')
    # Band-pass filter implementation
    elif filter_type == 'band':
        lowcut = cutoff[0]
        highcut = cutoff[1]
        b, a = signal.butter(order, [lowcut, highcut], btype='bandpass')
    else:
        raise ValueError("Unsupported filter type. Choose 'low', 'high', or 'band'.")
    filtered_signal = signal.filtfilt(b, a, time_series, axis=0)
    return filtered_signal

def lanczos_filter(time_series, window, filter_type='low', cutoff=None):
    if filter_type in ['high', 'low'] and cutoff is None:
        raise ValueError("Cutoff frequency must be provided for highpass and lowpass filters.")
    if filter_type == 'band' and (cutoff is None or len(cutoff) != 2):
        raise ValueError("A tuple of two cutoff frequencies must be provided for bandpass filters.")  
    def low_pass_weights(window, cutoff):
        order = ((window - 1) // 2 ) + 1
        nwts = 2 * order + 1
        w = np.zeros([nwts])
        n = nwts // 2
        w[n] = 2 * cutoff
        k = np.arange(1., n)
        sigma = np.sin(np.pi * k / n) * n / (np.pi * k)
        firstfactor = np.sin(2. * np.pi * cutoff * k) / (np.pi * k)
        w[n-1:0:-1] = firstfactor * sigma
        w[n+1:-1] = firstfactor * sigma
        # Ensure the cutoff is set for appropriate filter types
        return w[1:-1]
    # Low-pass filter implementation
    if filter_type == 'low':
        # constrcut Lanczos filter weights
        lfw = low_pass_weights(window,cutoff)
        weight_low = xr.DataArray(lfw, dims = ['window'])
        filtered_signal = time_series.rolling(time = len(lfw), center = True).construct('window').dot(weight_low)
    # High-pass filter implementation
    elif filter_type == 'high':
        # constrcut Lanczos filter weights
        lfw = low_pass_weights(window,cutoff)
        weight_low = xr.DataArray(lfw, dims = ['window'])
        low_pass_signal = time_series.rolling(time = len(lfw), center = True).construct('window').dot(weight_low)
        filtered_signal = time_series - low_pass_signal
    # Band-pass filter implementation
    elif filter_type == 'band':
    # apply the filters using the rolling method with the weights
        lfw = low_pass_weights(window, cutoff[0])
        hfw = low_pass_weights(window, cutoff[1])
        weight_high = xr.DataArray(hfw, dims = ['window'])
        weight_low = xr.DataArray(lfw, dims = ['window'])
        lowpass_lf = time_series.rolling(time = len(lfw), center = True).construct('window').dot(weight_low)
        lowpass_hf = time_series.rolling(time = len(hfw), center = True).construct('window').dot(weight_high)
        # the bandpass is the difference of two lowpass filters
        filtered_signal = lowpass_hf - lowpass_lf
    else:
        raise ValueError("Unsupported filter type. Choose 'low', 'high', or 'band'.")
    # Return the filtered signal
    return filtered_signal

def fourier_filter(time_series, freq, filter_type='low', cutoff=None):
    if filter_type in ['high', 'low'] and cutoff is None:
        raise ValueError("Cutoff frequency must be provided for highpass and lowpass filters.")
    if filter_type == 'band' and (cutoff is None or len(cutoff) != 2):
        raise ValueError("A tuple of two cutoff frequencies must be provided for bandpass filters.")
    # Low-pass filter implementation
    if filter_type == 'low':
        filtered_signal = gc.fourier_low_pass(time_series,frequency=freq,cutoff_frequency_low=cutoff)
    # High-pass filter implementation
    elif filter_type == 'high':
        filtered_signal = gc.fourier_high_pass(time_series,frequency=freq,cutoff_frequency_high=cutoff)
    # Band-pass filter implementation
    elif filter_type == 'band':
        filtered_signal = gc.fourier_band_pass(time_series,freq,cutoff_frequency_low=cutoff[0],cutoff_frequency_high=cutoff[1])
    return filtered_signal