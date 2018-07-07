# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 20:55:18 2018

@author: Administrator
"""

import os
import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
import glob
from pandas.compat import StringIO
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from ast import literal_eval


dataframe = pd.read_csv('bkpserv_daemon.raw',sep='\s*\n')
firstword = dataframe.apply(lambda x: x.str.split().str[0:12])
dataframeneeded = firstword.rename(columns={'0 1515417025 1 5 0 3004389184 64447 0 bkpserv nsrexecd NSR notice 2 %s 1 0 28 @(#) Product:      NetWorker':'MSG_Needed'}, inplace=True)

line1 = firstword.iloc[1].tolist()
linenecessary = line1[0]

line_msgid = linenecessary[0]
line_time = linenecessary[1]
line_msgtype = linenecessary[10] + linenecessary[11]

nsrlog = []
for i in firstword:
    nsrlog = firstword.iloc[i].tolist()
    
    len(line1)
Out[13]: 1

len(line1[0])
Out[14]: 12
len(line1[0])



    





