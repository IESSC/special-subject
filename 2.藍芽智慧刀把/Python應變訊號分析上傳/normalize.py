# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 14:40:38 2018

@author: KunXunLee
"""
import pandas as pd


def nsdata(st1,a,b):
    
    nst1=[]
    stdata=st1.iloc[0:,0]
    for index in range(len(stdata)):
        st1.loc[index]
        x_min=st1.min(axis=0)
        normalize=(st1.loc[index] - x_min) / (a - b)
        nst1.append(normalize)
        # 正規化訊號
    nst1=pd.DataFrame(nst1)
        
 
    return nst1
    
    
    
    
    
    
    