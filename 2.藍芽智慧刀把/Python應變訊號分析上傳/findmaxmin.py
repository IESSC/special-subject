# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 12:05:43 2018

@author: KunXunLee
"""
from numpy import mean, sqrt, square
def findmax(a,b,c,d):
    if a>b and a>c and a>d:        
        return a
    elif b>a and b>c and b>d:        
        return b
    elif c>a and c>b and c>d:        
        return c
    elif d>a and d>b and d>c:        
        return d

def findmin(a,b,c,d):
    if a<b and a<c and a<d:
        return a
    elif b<a and b<c and b<d:
        return b
    elif c<a and c<b and c<d:
        return c
    elif d<a and d<b and d<c:
        return d
    
def rms(a):
    s=sqrt(mean(square(a-mean(a))))
    return s