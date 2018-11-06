# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 14:03:35 2018

@author: tancr
"""

def linear (lst, num):
    for i in range(len(lst)):
        if lst[i]==num:
            return i 
    return None


def hello ():
    name = input('what is your name? ')
    print ('hello ' + name)
