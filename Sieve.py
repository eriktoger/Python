#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 20:53:22 2019

@author: erik
"""

# Simple sieve
upperLimit = 10**4
primeList = list( range(2,upperLimit+1))

primeIndex = 0;
while(primeIndex < len(primeList)):
    currentPrime = primeList[primeIndex]
    sieveNr = currentPrime*2
    compsiteNrSet = set()
    
    while(sieveNr <= upperLimit):
        compsiteNrSet.add(sieveNr)
        sieveNr += currentPrime
    
    primeList = list ( set(primeList) - compsiteNrSet)
    primeList.sort()
    primeIndex = primeIndex + 1
    

print(len(primeList) )
    
    
    
    
    
