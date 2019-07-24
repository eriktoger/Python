#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 19:17:34 2019

@author: erik
"""

#seens to work, but need more testing

def insert(word1,word2):
    if len(word1) == len(word2):
        return False
    else:
        if len(word1) < len(word2):
            tempWord = word1
            word1 = word2
            word2 = tempWord
        
        counterWord2 = 0
        insertCount = 0
        for c1 in word1:
            if c1 == word2[counterWord2]:
                #if no insert ins needed we look at the next char
                counterWord2 = counterWord2 + 1
                if counterWord2 == len(word2):
                    break
            else:
                #simulate an insert.
                insertCount = insertCount + 1
        # its okey to insert once 
        return insertCount < 2
    
def replace(word1,word2):
    #maximum one off
    if len(word1) != len(word2):
        return False
    counter = 0
    for c1,c2 in zip(word1,word2):
        if c1 != c2:
            counter = counter + 1
    return counter < 2

def remove (word1,word2):
     if len(word1) == len(word2):
        return False
     else:
        if len(word1) < len(word2):
            tempWord = word1
            word1 = word2
            word2 = tempWord
        counterWord1 = 0
        
        removeCount = 0
        for c2 in word2:
            if c2 == word1[counterWord1]:
                #if no remove is needed we look at the next char
                counterWord1 = counterWord1 + 1
                if counterWord1 == len(word1):
                    break
            else:
                #simulate an insert.
                removeCount = removeCount + 1
        # its okey to insert once 
        return removeCount < 2
    
while(True):
    word1 = input("enter word nr 1 (QUIT to quit): ")
    if word1 == "QUIT":
        break
    word2 = input("enter word nr 2 (QUIT to quit): ")
    answer = False
    if word2 == "QUIT":
        break
    if abs( (len(word1) - len(word2) ) > 1 ):
       answer = False
    else:
        
        #insert 1
        answer = insert(word1,word2)
        
        # replace 1
        if(not answer):
            answer = replace(word1,word2)
        
        #remove 1
        if(not answer):
            answer = remove(word1,word2)
        
    print(answer)