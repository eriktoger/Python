#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 11:28:11 2019

@author: erik
"""

def merge(firstHalf,secondHalf):
    
    indexFH = 0
    indexSH = 0
    mergedList = []
    
    #adding the smallest item of each list
    while ( (indexFH < len(firstHalf) ) and ( indexSH < len(secondHalf) ) ):
        if firstHalf[indexFH] < secondHalf[indexSH]:
            mergedList.append(firstHalf[indexFH])
            indexFH = indexFH +1
        else:
            mergedList.append(secondHalf[indexSH])
            indexSH = indexSH +1
    
    #adding any left overs         
    while indexFH < len(firstHalf):
         mergedList.append(firstHalf[indexFH])
         indexFH = indexFH +1
    
    while indexSH < len(secondHalf):
         mergedList.append(secondHalf[indexSH])
         indexSH = indexSH +1

    return mergedList
    

def mergeSort(listOfIntegers):
    
    
    if len(listOfIntegers) > 1:
        
        middle = int (len(listOfIntegers)/2)
        firstHalf = listOfIntegers[:middle ]
        secondHalf = listOfIntegers[middle: ]
        firstHalf = mergeSort(firstHalf)
        secondHalf = mergeSort(secondHalf)
    else:
        return listOfIntegers
    
    return merge(firstHalf,secondHalf)
        

import random
randomIntegers = []

for _ in range(100):
    randomIntegers.append(random.randint(1,100))

print(randomIntegers)
randomIntegers = mergeSort(randomIntegers)
print(randomIntegers)
    