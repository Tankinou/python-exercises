# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 13:47:39 2018

@author: tancr
"""

#%%
                
def bubble(lst):
    for j in range(0, len(lst) - 1):
        for i in range(0, len(lst) - j - 1):
            if lst[i] > lst[i + 1]:
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp
                