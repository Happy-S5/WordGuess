# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 10:01:07 2023

@author: miram
"""

import random
import string


def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    VOWELS = "aeiouy"
    alphebet = "abcdefghijklmnopqrstuvwxyz"
    
    CONSONANTS = ''.join([x for x in alphebet if x not in VOWELS])
    
    
    hand={}
    numVowels = n // 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

print(f'The dealt hand is {dealHand(7)}')


hand = dealHand(7)