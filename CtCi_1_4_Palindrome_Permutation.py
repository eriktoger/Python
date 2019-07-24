#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 18:55:39 2019

@author: erik
"""
while(True):
    word = input("enter word (QUIT to quit): ")
    alphabet = {}
    if word == "QUIT":
        break
    
    for c in word:
        c = c.lower()
        if c != ' ':
            if c not in alphabet:
                alphabet[c] = 1;
            else:
                alphabet[c] = alphabet[c] +1
    
    counterOdd = 0
    for item in alphabet.values():
        if item %2 ==1:
            counterOdd = counterOdd +1
    
    if counterOdd >1:
        print('false')
    else:
        print('true')