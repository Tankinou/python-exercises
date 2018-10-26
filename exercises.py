# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 14:03:35 2018

@author: tancr
"""

def linear (lst, number):
    for i in range(len(lst)):
        if lst[i]==number:
            return i 
    return None

