# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 18:12:20 2019
Convert Plain Text file output to CSV for MMINFO output.
@author: dhirp
"""

import pandas as pd
import numpy as np

df = pd.read_csv('mminfoCE.LOG',sep='\s*\n')

firstword = df.apply(lambda x: x.str.split().str[0:12])

# Create the actual dataset with the necessary colums 'msgid','nsavetime','msg1','msg2'
nsr_dataset = pd.DataFrame()


for i in range(len(firstword)):
    nsr_dataset = nsr_dataset.append(pd.DataFrame({'volume':firstword.iloc[i][0][0],'type':firstword.iloc[i][0][1],'msg1':firstword.iloc[i][0][10],'msg2':firstword.iloc[i][0][11]}, index=[0]), ignore_index=True)


for i in range(len(firstword)):
    nsr_dataset = nsr_dataset.append(pd.DataFrame({'volume':firstword.iloc[i][0][0],'Type':" ".join(firstword.iloc[i][0][1:3]),'Client':firstword.iloc[i][0][3:4],'date_time':" ".join(firstword.iloc[i][0][4:6]),'size':" ".join(firstword.iloc[i][0][6:8]),'ssid':firstword.iloc[i][0][8:9],'sumflag':firstword.iloc[i][0][9:10],'Level':firstword.iloc[i][0][10:11],'Name':" ".join(firstword.iloc[i][0][11:])}, index=[0]), ignore_index=True)

# Save dataset to CSV file    

nsr_dataset.to_csv('nsr_dataset.csv')
