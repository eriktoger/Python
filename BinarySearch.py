#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 08:53:04 2019

@author: erik
"""

import math

def binarySearch(target, listOfNumbers, start,end):
    
    index = math.floor( (end+start) /2)
  
    if(target < listOfNumbers[index] and (index > start)):
        index = binarySearch(target,listOfNumbers,start,index-1)
        
    elif (listOfNumbers[index] < target) and (end > index ):
        index = binarySearch(target,listOfNumbers,index + 1,end)
    
    if(listOfNumbers[index] == target and index != -1):
        return index
    else:
        return -1
    

listOfNumbers = list(range(0,21,2))
target = 0
index = binarySearch(target, listOfNumbers, 0 , len(listOfNumbers) ) 
print(target)
if(index != -1):
    print(listOfNumbers[index])
else:
    print("didnt find")