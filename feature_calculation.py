# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 11:33:04 2017

@author: adamguo
"""
import csv
import os
import numpy as np
os.chdir('/Users/adamguo/Desktop')

label = '0'
endData = [['second', 'mean_x', 'std_x', 'min_x', 'max_x', 'mean_y', 'std_y', 'mix_y', 'max_y', 'mean_z', 'std_z', 'min_z', 'max_z', 'Activity']]
time = 0

xList = []
yList = []
zList = []
with open('sensor_value_10-28-26(accel).csv', 'r', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        if(float(row[7]) >= time+1):
            endData.append([time,np.mean(xList),np.std(xList),np.min(xList),np.max(xList),np.mean(yList),np.std(yList),np.min(yList),np.max(yList),np.mean(zList),np.std(zList),np.min(zList),np.max(zList),label])
            xList = []
            yList = []
            zList = []
            time += 1;
        elif(label != row[8]):
            endData.append([time,np.mean(xList),np.std(xList),np.min(xList),np.max(xList),np.mean(yList),np.std(yList),np.min(yList),np.max(yList),np.mean(zList),np.std(zList),np.min(zList),np.max(zList),label])
            xList = []
            yList = []
            zList = []
            label = row[8]
        else:
            xList.append(float(row[3]))
            yList.append(float(row[4]))
            zList.append(float(row[5]))
            label = row[8]
        

print(endData)

with open("features.csv", "w", newline='') as outFile:
    writer = csv.writer(outFile)
    writer.writerows(endData)    