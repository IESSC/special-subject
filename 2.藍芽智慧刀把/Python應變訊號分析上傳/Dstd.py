# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 14:35:49 2018

@author: KunXunLee
"""
import numpy as np 
import matplotlib.pyplot as plt

def Dstd(a):

    std_1=[]
    for i in range(0,len(a),72):
        std1=a.iloc[i:72+i,0]
        rstd=np.std(std1)
        std_1.append(rstd)
        i=i+72
    
 #When working with paths that contain backslashes,
                                        #you either need to use two backslashes, or use the r'' form to prevent interpreting of escape sequences. 
                                                   #For example, 'C:\\Program Files\\...' or r'C:\Program Files\...'. 

    return std_1