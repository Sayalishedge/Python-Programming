# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 19:03:13 2023

@author: anilk
"""

def myf1():
    global count
    #count=0
    count=count+1
    print("in function",count)
    
    

count=1
myf1()
print("outside function",count)