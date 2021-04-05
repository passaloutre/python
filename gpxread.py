#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 14:20:25 2019

@author: rdchlmtr
"""

from tkinter import filedialog
from tkinter import Tk
import numpy as np

root = Tk()
root.withdraw()

infile = filedialog.askopenfilename(parent=root, title='Select file to convert')

with open(infile) as fp:
    d = []
    t = []
    x = []
    y = []
    z = []
    dat = fp.readlines()
    for i in range(len(dat)):
        if dat[i].startswith('                        <gpxtpx:depth>'):
            if dat[i-4].startswith('                <time>'):
                if dat[i-5].startswith('            <trkpt '):
                    z.append(dat[i].replace('<', '>').split('>')[2])
                    d.append(dat[i-4].replace('<', '>').split('>')[2][:10])
                    t.append(dat[i-4].replace('<', '>').split('>')[2][11:-1])
                    x.append(dat[i-5].replace('"', ',').split(',')[3])
                    y.append(dat[i-5].replace('"', ',').split(',')[1])

outfile = filedialog.asksaveasfilename(parent=root, title='Save output file as', defaultextension='*.txt')

np.savetxt(outfile, np.column_stack((d, t, x, y, z)), delimiter=',', fmt='%s')