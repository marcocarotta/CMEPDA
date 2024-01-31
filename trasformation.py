import numpy as np
from sklearn import preprocessing

def prep(original,input, dir, index_log, range_quantile, n_quantiles):
    
    if dir == 'forward':
        
        for i in index_log:
            input[:,i] = np.log(10 + input[:,i])
        
        scaler = preprocessing.StandardScaler().fit(input)
        input = scaler.transform(input)

        quantile = preprocessing.QuantileTransformer(n_quantiles=n_quantiles,output_distribution='normal').fit(input[range_quantile])
        for j in range_quantile:
            print(j)
            input[:,j] = quantile.transform(input[:,j])
    
    elif dir == 'backward':
        quantile = preprocessing.QuantileTransformer(n_quantiles=n_quantiles,output_distribution='normal').fit(original[range_quantile])
        for j in range_quantile:
            print(j)
            input[:,j] = quantile.inverse_transform(input[:,j])
        
        scaler = preprocessing.StandardScaler().fit(original)
        input = scaler.inverse_transform(input)
        
        for i in index_log:
            input[:,i] = np.exp(input[:,i]) - 10

    return input    