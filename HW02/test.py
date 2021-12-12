#!/usr/bin/env python
# coding: utf-8

# In[123]:


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
import LinearRegression


# In[124]:


a=np.array([1,2,np.nan,5,1,3,5,9,np.nan,2,3,4,1,2,3,7,8,5])
a=a.reshape((9,2))
a = pd.DataFrame(a)
target_a = np.array([2,1,4,5,1,3,3,1,2])


# In[125]:


a,b,c,d = LinearRegression.LinearRegression(a,target_a)

