#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 19:04:46 2022

@author: rdchlmtr
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import glob
import xml.etree.ElementTree as et


os.chdir('/Users/rdchlmtr/Documents/Projects/swan_island/data/levellogger/final')

dat = {}
dat_short = {}
for k in [1, 2, 3, 4, 5]:
    filelist = sorted(glob.glob('swan{}*.xle'.format(k)))
    
    times = []
    pressures = []
    temps = []
    
    for j in filelist:
        tree = et.parse(j)
        root = tree.getroot()
    
    
        
        for i in range(len(root[5])):
            time = root[5][i][0].text + ' '  + root[5][i][1].text
            pressure = float(root[5][i][3].text)
            temp = float(root[5][i][4].text)
            
            times.append(time)
            pressures.append(pressure)
            temps.append(temp)
            
    #%%
            
    dat[k] = pd.DataFrame(list(zip(pressures, temps)), 
                       columns=['Pressure', 'Temp'], index=pd.to_datetime(times))
    
    dat_short[k] = dat[k].resample('H').mean()
    
#%%

plt.plot(dat_short[1].Pressure, 'r.')
plt.plot(dat_short[2].Pressure, 'g.')
plt.plot(dat_short[3].Pressure, 'b.')
plt.plot(dat_short[4].Pressure, 'k.')
# plt.plot(dat_short[5].Pressure, 'c.')

#%%

dat_short[1].to_csv('swan1_baro.csv', index=True, header=True, index_label=False)
