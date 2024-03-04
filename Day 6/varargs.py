# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 18:53:07 2023

@author: anilk
"""

def addition(x,y,*t,**kwarg):
    print(x,y)
    print(t)
    print(kwarg)
    ans=x+y
    for num in t:
        ans=ans+num
    for v in kwarg.values():
        ans=ans+v
    return ans
    
    
result=addition(1,2,5,3,4,5,6,a=100,b=200,c=300)
print(result)
    