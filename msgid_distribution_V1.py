# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 13:18:10 2018

@author: dhirp
"""

## Objective to Identify the distribution of different types of messages
## Encode the message ids based on Priority, to enable better CLASSIFICATION

import os
import pandas as pd
import csv
import glob
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import numpy as np

path = r'C:\Users\dhirp\Documents\EncodingTests'
allFiles = glob.glob(path +"/*.csv")

frame = pd.DataFrame()
list_ = []

for file_ in allFiles:
    df = pd.read_csv(file_,index_col=None,header=0)
    list_.append(df)
    
frame = pd.concat(list_)
frame = frame.reset_index(drop=True)

frame.to_csv('Test_Data_Distribuition.csv')

## Type of Message we see.
#NOTICE,CRITICAL,ERROR,SEVERE,WARNING,INFO,NOTICE

frame_for_analysis = frame[['msg2','msgid']]
frame_unique = frame_for_analysis.drop_duplicates()
#Create the Distribution plot
%matplotlib qt
sns.lmplot(x='msg2',y='msgid',data=frame_unique,hue='msg2',fit_reg=False)

#Encode the variables into a certain limit so that the classifier works
## Change the contents of msg2 into features

categorical_no = frame_unique.pivot(columns='msg2',values='msgid')
categorical_no.to_csv('categorical_no.csv')

## Limit the values
# Notice 0-1 
notice = categorical_no.filter(['notice'],axis=1).dropna()

scaler_notice = MinMaxScaler(feature_range=(0,1))
notice_a = np.array(notice.astype('int64'))
rescaled_notice = scaler_notice.fit_transform(notice_a.reshape(-1,1)).tolist()

#INFO 2-3
info = categorical_no.filter(['info'],axis=1).dropna()

scaler_info = MinMaxScaler(feature_range=(2,3))
info_a = np.array(info.astype('int64'))
rescaled_info = scaler_info.fit_transform(info_a.reshape(-1,1)).tolist()

#Warning 4-5
warning = categorical_no.filter(['warning'],axis=1).dropna()

scaler_warning = MinMaxScaler(feature_range=(4,5))
warning_a = np.array(warning.astype('int64'))
rescaled_warning = scaler_warning.fit_transform(warning_a.reshape(-1,1)).tolist()

#Critical 6-7
critical = categorical_no.filter(['critical'],axis=1).dropna()

scaler_critical = MinMaxScaler(feature_range=(6,7))
critical_a = np.array(critical.astype('int64'))
rescaled_critical = scaler_critical.fit_transform(critical_a.reshape(-1,1)).tolist()

#Severe 8-9
severe = categorical_no.filter(['severe'],axis=1).dropna()

scaler_severe = MinMaxScaler(feature_range=(8,9))
severe_a = np.array(severe.astype('int64'))
rescaled_severe = scaler_severe.fit_transform(severe_a.reshape(-1,1)).tolist()

# Error 10-11
error = categorical_no.filter(['error'],axis=1).dropna()

scaler_error = MinMaxScaler(feature_range=(10,11))
error_a = np.array(error.astype('int64'))
rescaled_error = scaler_error.fit_transform(error_a.reshape(-1,1)).tolist()

## Recreate the dataframe and plot
## Problem is that the number of rows are not similar
#myplot_reqmt_rescaled = pd.DataFrame(dict(notice=rescaled_notice,info=rescaled_info,warning=rescaled_warning,critical=rescaled_critical,severe=rescaled_severe,error=rescaled_error,index['0'])).fillna(0)



