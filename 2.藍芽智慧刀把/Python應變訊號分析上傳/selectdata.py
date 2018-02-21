# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 14:27:01 2018

@author: KunXunLee
"""
import pandas as pd
import numpy as np 



def select(data,column):
    
    sdata=data.iloc[0:,column]            #iloc通過行列數字索引取值，[列，行]
    sdata=sdata.dropna(axis=0,how='any')

    out_df = data[data.iloc[:,column] == 0]
    for i in range(len(out_df)):
        sdata =sdata.drop(out_df.index[i])

    sdata = sdata.tolist()
    sdata=pd.Series(sdata)

    for i in range(0,len(sdata),288):
        select1=sdata.iloc[i:288+i]         #切割288
        sdata_max=select1.max(axis=0)
        sdata_min=select1.min(axis=0)
        sub=sdata_max-sdata_min
        A=np.argmax(select1)               #找出分割第一個最大值的索引值
        if sub > 0.000017 :            #判斷是否大於3bit,超過視為加工開始段
            break
        i=i+288   

    for i in range(A,len(sdata),288):
        select1=sdata.iloc[i:288+i]         #切割288
        sdata_max=select1.max(axis=0)
        sdata_min=select1.min(axis=0)
        sub=sdata_max-sdata_min
        A1=np.argmin(select1)               #找出分割第一個最大值的索引值
        if sub < 0.000015 :            #判斷是否大於3bit,超過視為加工開始段
            break
        i=i+288

    select1=sdata.iloc[A:A1]

    
    return select1
    