# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 16:06:40 2018

@author: dhirp
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 20:55:18 2018

@author: Administrator
"""
""" Introduced Data visualiazation using MATPLOTLIB"""
## Import Libraries
import os
import numpy as np
import pandas as pd
import csv
import glob
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from operator import itemgetter

# Read the Daemon RAW file and create a Dataframe
dataframe = pd.read_csv('daemon_1.txt',sep='\s*\n',header=None,error_bad_lines=False)
#Save a copy of the dataframe 
dataframe.to_csv('dataframe.csv')
#Split the dataframe, Seperate the Messages from the rest of the information.

# firstword: Everything other than the actual message
firstword = dataframe.apply(lambda x: x.str.split().str[0:14])

# secondword: The message logged
secondword = dataframe.apply(lambda x: x.str.split().str[14:])

# The two resulting dataframes will be lists, We need to concat them 
# processed_df : Has two columns one has Message and the other info.
processed = [firstword,secondword]
processed_df = pd.concat(processed,axis=1)
processed_df.columns = ['Info','Message']

# Saving to csv file for reference
processed_df.to_csv('processed_df.csv')

# Some rows are blank or have un-necessary characters. We need to count the no of elements 
# If the size is below a threshold, We need to ignore them. 
#to_ignore is a Dataframe that has the actual index and the contents of the rows that have un-necessary values
to_ignore = processed_df[processed_df['Info'].map(len) < 2]

#Create a CSV of the to_ignore values to make sure we are not omitting important stuff
to_ignore.to_csv('to_ingore.csv')
## Collect the list of index to be dropped from processed_df

index_toignore = to_ignore.index.tolist()

#Remove the unwanted rows and create a new dataframe, Also reset the index again for better analysis.
processed_df_unique = processed_df.drop(index_toignore).reset_index(drop=True)

###<<<<< Not Used >>>>>>
filter = [0,1,2,3,11,12,13]
msgid = [0]
date = [1]
time = [2,3]
process = [11]
msg_comp = [12]
msg_level = [13]
print(itemgetter(*filter)(processed_df['Info'][56]))
##print(itemgetter(*b)(a))
####<<<<< Not Used Complete >>>>>

# Create the actual dataset with the necessary colums 'msgid','nsavetime','msg1','msg2'
#nsr_dataset: name of the dataset with unique values of info
nsr_dataset = pd.DataFrame()

for i in range(len(processed_df_unique['Info'])):
    try:
        nsr_dataset = nsr_dataset.append(pd.DataFrame({'msgid':processed_df_unique['Info'].iloc[i][0],'Date':processed_df_unique['Info'].iloc[i][1],'Time':processed_df_unique['Info'].iloc[i][2],'Am-Pm''Date':processed_df_unique['Info'].iloc[i][3],'Process':processed_df_unique['Info'].iloc[i][11],'NSR_COMP':processed_df_unique['Info'].iloc[i][12],'MSG_LEVEL':processed_df_unique['Info'].iloc[i][13]}, index=[0]), ignore_index=True)
    except IndexError:
        pass
        #continue
		
# Concat the seperated Info (nsr_dataset) with just the messages (nsr_dataset1)
nsr_dataset1 = pd.DataFrame()
nsr_dataset1 = processed_df_unique['Message']
combined = [nsr_dataset,nsr_dataset1]
# Final Dataframe processed_df_final
processed_df_final = pd.concat(combined,axis=1)

