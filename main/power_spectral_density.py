import numpy as np

def compute_spectrum(autocorr, m):
    """
    计算粗谱
    
    参数:
    autocorr (numpy array): 自相关系数数组，长度为 m+1
    m (int): 最大滞后数
    
    返回:
    spectrum (numpy array): 粗谱数组，包含 k=0 到 k=m 的粗谱值
    """
    spectrum = np.zeros(m + 1)

    # 计算 S_0 (k=0)
    spectrum[0] = (1 / (2 * m)) * (autocorr[0] + autocorr[m]) + (1 / m * np.sum(autocorr[1:m]))

    # 计算 S_k (1 <= k <= m-1)
    for k in range(1, m):
        sum_term = np.sum([autocorr[j] * np.cos(k * np.pi * j / m) for j in range(1, m)])
        spectrum[k] = (1 / m) * (autocorr[0] + 2 * sum_term + (-1)**k * autocorr[m])

    # 计算 S_m (k=m)
    sum_term_m = np.sum([(-1)**j * autocorr[j] for j in range(1, m)])
    spectrum[m] = (1 / (2 * m)) * (autocorr[0] + (-1)**m * autocorr[m]) + (1 / m * sum_term_m)

    return spectrum

def hanning_smoothing(spectrum):
    """
    对粗谱进行 Hanning 平滑处理

    参数:
    spectrum (numpy array): 粗谱数组，包含 k=0 到 k=m 的粗谱值

    返回:
    smoothed_spectrum (numpy array): 平滑后的谱数组
    """
    m = len(spectrum) - 1
    smoothed_spectrum = np.zeros(m + 1)

    # 计算 S_0
    smoothed_spectrum[0] = 0.5 * spectrum[0] + 0.5 * spectrum[1]

    # 计算 S_k (1 <= k <= m-1)
    for k in range(1, m):
        smoothed_spectrum[k] = 0.25 * spectrum[k-1] + 0.5 * spectrum[k] + 0.25 * spectrum[k+1]

    # 计算 S_m
    smoothed_spectrum[m] = 0.5 * spectrum[m-1] + 0.5 * spectrum[m]

    return smoothed_spectrum

def compute_frequency_and_period(m):
    # 确定频率和周期 
    # 虽然k=0,1,2,3,...,m .但是由于python左闭右开的原因，这里m+1
    frequencies = np.array([k / (2 * m) for k in range(m + 1)])
    periods = np.array([2 * m / k if k != 0 else np.inf for k in range(m + 1)])  # 防止 k = 0 的情况
    return frequencies, periods

def significance_test(S, r_1, m):
    # 显著性检验
    # mean_S 为m+1个谱估计值的均值
    """
    numpy.fromiter(iter, dtype, count=-1, *, like=None)
    Create a new 1-dimensional array from an iterable object.
    """

    mean_S = (1 / (2 * m)) * (S[0] + S[m]) + (1 / m) * np.sum(np.fromiter((S[k] for k in range(1, m)), float))
    print('mean_S.shape:',mean_S)
    red_noise = np.array([(1 - r_1[1]**2) / (1 + r_1[1]**2 - 2 * r_1[1] * np.cos(np.pi * k / m)) * mean_S for k in range(m + 1)])
    print('red_noise.shape:',red_noise.shape)
    white_noise = np.full(m + 1, mean_S)
    print('white_noise.shape:',white_noise.shape)
    return red_noise, white_noise, mean_S
