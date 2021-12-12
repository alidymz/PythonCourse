#!/usr/bin/env python
# coding: utf-8

# In[4]:


import scipy.stats as stats
import wbdata
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# In[5]:


def LinearRegression(X,Y):
   
    X = pd.DataFrame(X)
    Y = pd.DataFrame(Y)
    Y = Y.to_numpy()
    Y = Y.reshape((-1,1))
    Y = pd.DataFrame(Y)
    merge_col = [X,Y]
    result = pd.concat(merge_col,axis=1, keys=["x_values","targets"])
    result = result.dropna()
    X = result['x_values'].to_numpy()
    Y = result['targets'].to_numpy()
    
    print(f'Y shape{Y.shape}')
    
    n , k = X.shape
    print(f'n:{n} and k:{k}')
    ones = np.ones((n,1))
    print(f'intercept shape{ones.shape}')
    X = np.concatenate((ones,X),axis=1)
    print(f'X shape{X.shape}')
    X_ = np.linalg.inv(np.matmul(np.transpose(X),X))
    print(f'X_ shape{X_.shape}')
    
    β1 = np.matmul(X_,np.transpose(X))
    print(f'β1 shape{β1.shape}')
    β = np.matmul(β1,Y)
    print(f'β shape{β.shape}')
    y_hat = np.matmul(X,β)
    print(f'y_hat shape{y_hat.shape}')
    e = Y-y_hat
    print(f'e shape{e.shape}')
    σ_square = np.matmul(np.transpose(e),e)/(n-k-1)
    print(f'σ_square shape{σ_square.shape}')
    var_β = np.diag(np.multiply(σ_square,X_))
    
    standart_error = np.sqrt(var_β)
    standart_error = standart_error.reshape(-1,1)
    print(f'standart_error shape{standart_error.shape}')
    
    alfa = 0.05
    
    t_critical = stats.t.ppf(q = 1-alfa/2, df= n-k-2)  # Get the t-critical value*

    print("t-critical value:")                  # Check the t-critical value
    print(t_critical)                        

    sigma = standart_error # std 
    margin_of_error = t_critical * sigma

    confidence_interval = (np.subtract(β , margin_of_error),
                           np.add(β , margin_of_error)) 
    
    return β, standart_error, confidence_interval,y_hat

