# -*- coding: utf-8 -*-

# def adcp(filename):
    
filename = '/Users/rdchlmtr/Documents/Projects/scour_hole/BURAS ADCP DATA/BURAS_0_000_ASC.TXT'

import numpy as np
 
f = open(filename, 'r')
g = f.readlines()

'''read the file header'''
    
dat = {}
dat['comment1'] = g[0]
dat['comment2'] = g[1]
    
h = g[2].split()
dat['binsize'] =   float(h[0])
dat['blank'] =     float(h[1])
dat['firstbin'] =  float(h[2])
dat['numcells'] =  int(h[3])
dat['numpings'] =  int(h[4])
dat['tpe'] =       int(h[5])
dat['watermode'] = int(h[6])

m = int(dat['numcells'])
n = int((len(g)-3)//(6+dat['numcells']))

'''set up empty variable lists'''

dat['year'] =    []
dat['month'] =   []
dat['day'] =     []
dat['hour'] =    []
dat['minute'] =  []
dat['second'] =  []
dat['hunsec'] =  []
dat['ensnum'] =  []
dat['numens'] =  []
dat['pitch'] =   []
dat['roll'] =    []
dat['heading'] = []
dat['temp'] =    []

dat['btvel_x'] =      []
dat['btvel_y'] =      []
dat['btvel_z'] =      []
dat['btvel_err'] =    []
dat['depthsounder'] = []
dat['ggaalt'] =       []
dat['ggadeltaalt'] =  []
dat['ggahdop'] =      []
dat['depth'] =        []

dat['elapdist'] =     []
dat['elaptime'] =     []
dat['distnorth'] =    []
dat['disteast'] =     []
dat['distmadegood'] = []

dat['lat'] = []
dat['lon'] = []

dat['qmid'] = []
dat['qtop'] = []
dat['qbot'] = []

dat['binstofollow'] = []
dat['measunit'] =     []
dat['velref'] =       []
dat['intensunits'] =  []
dat['intensscale'] =  []
dat['soundabsorp'] =  []

dat['z'] = np.zeros((m, n))
dat['spd'] = np.zeros((m, n))
dat['dir'] = np.zeros((m, n))
dat['east'] = np.zeros((m,n))
dat['north'] = np.zeros((m, n))
dat['up'] = np.zeros((m, n))
dat['err'] = np.zeros((m, n))
dat['echo'] = np.zeros((m, n, 3))
dat['percgood'] = np.zeros((m, n))
dat['q'] = np.zeros((m, n))


'''iterate through the file'''

i = 3

while i < len(g):
    
    '''first row'''
    h = g[i].split()
    dat['year'].append(int(h[0]))
    dat['month'].append(int(h[1]))
    dat['day'].append(int(h[2]))
    dat['hour'].append(int(h[3]))
    dat['minute'].append(int(h[4]))
    dat['second'].append(int(h[5]))
    dat['hunsec'].append(int(h[6]))
    dat['ensnum'].append(int(h[7]))
    dat['numens'].append(int(h[8]))
    dat['pitch'].append(float(h[9]))
    dat['roll'].append(float(h[10]))
    dat['heading'].append(float(h[11]))
    dat['temp'].append(float(h[12]))
    
    '''second row'''
    h = g[i+1].split()
    dat['btvel_x'].append(float(h[0]))
    dat['btvel_y'].append(float(h[1]))
    dat['btvel_z'].append(float(h[2]))
    dat['btvel_err'].append(float(h[3]))
    dat['depthsounder'].append(float(h[4]))
    dat['ggaalt'].append(float(h[5]))
    dat['ggadeltaalt'].append(float(h[6]))
    dat['ggahdop'].append(float(h[7]))
    dat['depth'].append([float(j) for j in h[8:]])
    
    '''third row'''
    h = g[i+2].split()
    dat['elapdist'].append(float(h[0]))
    dat['elaptime'].append(float(h[1]))
    dat['distnorth'].append(float(h[2]))
    dat['disteast'].append(float(h[3]))
    dat['distmadegood'].append(float(h[4]))
    
    '''fourth row'''
    h = g[i+3].split()
    dat['lat'].append(float(h[0]))
    dat['lon'].append(float(h[1]))
                    
    '''fifth row'''                        
    h = g[i+4].split()
    dat['qmid'].append(float(h[0]))
    dat['qtop'].append(float(h[1]))
    dat['qbot'].append(float(h[2]))
    
    '''sixth row'''
    h = g[i+5].split()
    dat['binstofollow'].append(int(h[0]))
    dat['measunit'].append(h[1])
    dat['velref'].append(h[2])
    dat['intensunits'].append(h[3])
    dat['intensscale'].append(float(h[4]))
    dat['soundabsorp'].append(float(h[5]))
    
    '''several rows'''
    h = g[i+6:i+6+dat['numcells']]
    h = np.asarray([j.split() for j in h], dtype=float)
    dat['z'] = h[:,0]
    dat['spd'] = h[:,1]
    dat['dir'] = h[:,2]
    dat['east'] = h[:,3]
    dat['north'] = h[:,4]
    dat['up'] = h[:,5]
    dat['err'] = h[:,6]
    # dat['echo'] = [h[:,k] for k in [7,8,9]]
    
    



f.close()

#return dat
