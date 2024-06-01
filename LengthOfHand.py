# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 09:16:39 2023

@author: miram
"""

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    
    LLetters = []
    LLetters = hand.values()
    return sum(LLetters)
    
    
hand = {'r': 2, 'a': 1, 'p': 2, 'e': 1, 't': 1, 'u': 1}   
print(calculateHandlen(hand))    
    