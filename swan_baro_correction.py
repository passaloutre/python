#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 17:36:23 2022

@author: rdchlmtr
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import glob
from scipy import io

os.chdir('/Users/rdchlmtr/Documents/Projects/swan_island/data/outputs')

site = 4

vec = {}

vec['time'] = io.loadmat('swan{}_time.mat'.format(site))['time_string']
vec['pressure'] = io.loadmat('swan{}_pressure.mat'.format(site))['pressure_station'].squeeze()
vec['u'] = io.loadmat('swan{}_u.mat'.format(site))['u_station'].squeeze()
vec['v'] = io.loadmat('swan{}_v.mat'.format(site))['v_station'].squeeze()
vec['w'] = io.loadmat('swan{}_w.mat'.format(site))['w_station'].squeeze()
vec['amp'] = io.loadmat('swan{}_amp.mat'.format(site))['amp_station'].squeeze()
vec['corr'] = io.loadmat('swan{}_corr.mat'.format(site))['corr_station'].squeeze()
vec['snr'] = io.loadmat('swan{}_snr.mat'.format(site))['snr_station'].squeeze()
vec['height'] = io.loadmat('swan{}_height.mat'.format(site))['height_station'].squeeze()
vec['period'] = io.loadmat('swan{}_period.mat'.format(site))['period_station'].squeeze()
vec['msg'] = io.loadmat('swan{}_msg.mat'.format(site))['msg_station'].squeeze()
vec['coord'] = np.array(list(*io.loadmat('swan{}_coord.mat'.format(site))['coord_station']))

vec['time'] = pd.to_datetime(vec['time'], errors='coerce')
vec['amp1'] = vec['amp'][:,0]
vec['amp2'] = vec['amp'][:,1]
vec['amp3'] = vec['amp'][:,2]
vec['corr1'] = vec['corr'][:,0]
vec['corr2'] = vec['corr'][:,1]
vec['corr3'] = vec['corr'][:,2]
vec['snr1'] = vec['snr'][:,0]
vec['snr2'] = vec['snr'][:,1]
vec['snr3'] = vec['snr'][:,2]
vec.pop('amp')
vec.pop('corr')
vec.pop('snr')
vec = pd.DataFrame(data=vec, index=vec['time'])
vec.pop('time')

baro = pd.read_csv('swan1_baro.csv')
baro = baro.rename(columns={'Pressure':'baro', 'Temp':'temp'})
baro = baro.set_index('Unnamed: 0')
baro.index.name = None


#%%
dat = pd.concat([vec, baro])
dat.index.dropna()
dat.sort_index(inplace=True)
