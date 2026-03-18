import numpy as np
import geocat.comp as gc
def preprocess_data(data, method):
    if method == 'Standardization':
        outdata = (data - np.mean(data)) / np.std(data)
        return outdata
    elif method == 'MeanNormalization':
        outdata = (data - np.mean(data)) / (np.max(data) - np.min(data))
        return outdata
    elif method == 'MinNormalization':
        outdata = (data - np.min(data)) / (np.max(data) - np.min(data))
        return outdata
    elif method == 'Centralization':
        outdata = data - np.mean(data, axis=0)
        return outdata
    elif method == 'RmMonAnnCycle':
        outdata = gc.climate_anomaly(data, freq="month")
        return outdata
    elif method == 'nopreprecess':
        return data
    else:
        raise ValueError("Invalid method.")
