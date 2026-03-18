import numpy as np
import xarray as xr
# from scipy import special
from scipy import stats
from statsmodels.tsa.stattools import acf
import xskillscore as xs


# test autocorrelation function #
def autocorrelation(x, lag):
    """Calculate the autocorrelation of a time series at a given lag."""
    n = len(x)
    if lag >= n:
        return 0
    mean = np.mean(x)
    c0 = np.sum((x - mean) ** 2) / n
    ct = np.sum((x[:n-lag] - mean) * (x[lag:] - mean)) / n
    return ct / c0
# print(autocorrelation(x,5))
# print(acf(x,nlags=5)[-1])

# calculate effective sample size from Davis (1976) and Chen (1982) #
def ESS_DS1976(x, y, max_lag=None):
    """
    Calculate the effective sample size using Davis (1976) and Chen (1982) method.
    
    Args:
    x (array-like): First time series
    y (array-like): Second time series
    max_lag (int): Maximum lag to consider. If None, use n/2.
    
    Returns:
    float: Effective sample size
    """
    x = np.array(x)
    y = np.array(y)
    n = len(x)
    
    if len(y) != n:
        raise ValueError("Both time series must have the same length.")
    
    if max_lag is None:
        max_lag = n // 2

    T = 0
    for tau in range(-max_lag, max_lag + 1):
        # Rxx = autocorrelation(x, abs(tau))
        # Ryy = autocorrelation(y, abs(tau))
        Rxx = acf(x, nlags=abs(tau))[-1]
        Ryy = acf(y, nlags=abs(tau))[-1]
        T += Rxx * Ryy 
    
    Neff = n / T
    return Neff

# Neff0 = ESS_DS1976(x, y)
# print(f"Sample Size: {Neff0:.2f}")
# Neff1 = ESS_DS1976(x_filter, y_filter)
# print(f"Effective Sample Size: {Neff1:.2f}")

# calculate effective sample size from Bretherton (1999) #
def ESS_BN1999(x, y):
    # x = np.array(x)
    # y = np.array(y)
    x = xr.DataArray(x,dims="time")
    y = xr.DataArray(y,dims="time")
    return xs.effective_sample_size(x,y,dim="time")

# Neff0 = ESS_BN1999(x, y)
# print(f"Sample Size: {Neff0:.2f}")
# Neff1 = ESS_BN1999(x_filter, y_filter)
# print(f"Effective Sample Size: {Neff1:.2f}")

# calculate effective sample size from Metz (1991) #
import numpy as np
import pandas as pd
from statsmodels.tsa.stattools import acf
def ESS_MZ1991(x, y, max_lag=None):
    x = np.array(x)
    y = np.array(y)
    n = len(x)
    
    if len(y) != n:
        raise ValueError("Both time series must have the same length.")
    
    if max_lag is None:
        max_lag = n // 2
    # 数据长度
    n = len(x)

    # 计算最大滞后 τ_max
    if max_lag is None:
        max_lag = n // 2

    # 计算 X 和 Y 的自相关系数
    r_X = acf(x, nlags=max_lag)
    r_Y = acf(y, nlags=max_lag)

    # 计算有效自由度 N_eff
    sum_term = 0
    for tau in range(1, max_lag + 1):
        sum_term += (1 - tau / n) * r_X[tau] * r_Y[tau]

    N_eff = n / max(1, 1 + 2 * sum_term)
    return N_eff

# Neff0 = ESS_MZ1991(x, y)
# print(f"Sample Size: {Neff0:.2f}")
# Neff1 = ESS_MZ1991(x_filter, y_filter)
# print(f"Effective Sample Size: {Neff1:.2f}")

# calculate effective sample size from Pyper and Peterman (1998) #
def ESS_PR1998(x, y, max_lag=None):
    x = np.array(x)
    y = np.array(y)
    n = len(x)
    
    if len(y) != n:
        raise ValueError("Both time series must have the same length.")
    
    if max_lag is None:
        max_lag = n // 2

    # 计算 X 和 Y 的自相关系数
    r_X = acf(x, nlags=max_lag)
    r_Y = acf(y, nlags=max_lag)

    # 计算有效自由度 N_eff
    sum_term = 0
    for k in range(1, max_lag+1):
        sum_term += (n - k) / n * r_X[k] * r_Y[k]
    # for tau in range(1, max_lag + 1):
    #     sum_term += (1 - tau / n) * r_X[tau] * r_Y[tau]

    N_eff = n / (1 + 2 * sum_term)
    return N_eff

# Neff0 = ESS_PR1998(x, y)
# print(f"Sample Size: {Neff0:.2f}")
# Neff1 = ESS_PR1998(x_filter, y_filter)
# print(f"Effective Sample Size: {Neff1:.2f}")

# def ESS_to_p_value(Neff,r):
#     dof = Neff - 2
#     t_squared = r ** 2 * (dof / ((1.0 - r) * (1.0 + r)))
#     _x = dof / (dof + t_squared)
#     _x = np.asarray(_x)
#     _x = np.where(_x < 1.0, _x, 1.0)
#     _a = 0.5 * dof
#     _b = 0.5
#     res = special.betainc(_a, _b, _x)
#     return res

def ESS_to_p_value(Neff, r):
    # 计算自由度
    dof = Neff - 2
    # 计算t-value
    t_value = r * np.sqrt((Neff - 2) / (1 - r**2))
    # 计算双尾 p 值
    p_value = 2 * (1 - stats.t.cdf(np.abs(t_value), df=dof))
    return p_value