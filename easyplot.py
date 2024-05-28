#!/usr/bin/env python3 
import json
from matplotlib import pyplot as plt  
import sys,os
from time import sleep
import numpy as np

if sys.argv[1]:
    filename = sys.argv[1]
else:
	filename = data.json


with open(filename, 'r') as file:
    data = json.load(file)

datasets = data['data']

#plt.figure(figsize=(9,7))
fig,ax = plt.subplots(figsize=(9,7))

for dataset in datasets:
    x_data = dataset['xdata']
    y_data = dataset['ydata']
    if 'label' in dataset:
        mylabel = dataset['label']
        plt.plot(x_data, y_data,'o-',label=mylabel)
    else:
        plt.plot(x_data, y_data,'o-')

plt.legend()
if 'xscale' in data:
    x_scale = data['xscale']
    plt.xscale(x_scale)
if 'yscale' in data:
    y_scale = data['yscale']
    plt.yscale(y_scale)
if 'xlabel' in data:
    x_label = data['xlabel']
    plt.xlabel(x_label)
if 'ylabel' in data:
    y_label = data['ylabel']
    plt.ylabel(y_label)
if 'title' in data:
    mytitle = data['title']
    plt.title(mytitle)

if 'xlimit' in data:
    xmin = data['xlimit'][0]
    xmax = data['xlimit'][1]
    plt.xlim(xmin,xmax)
    
if 'ylimit' in data:
    ymin = data['ylimit'][0]
    ymax = data['ylimit'][1]
    plt.ylim(ymin,ymax)


if 'grid' in data:
	plt.grid()

plt.show()

