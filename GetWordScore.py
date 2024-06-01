# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 08:44:01 2023

@author: miram
"""
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}

def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    
    summation = 0
    word = word.lower()
    
    length = len(word)
    
       
    if length == 0:
        return 0 
    else: 
        for i in word:
            summation += SCRABBLE_LETTER_VALUES[i]
        if length == n: 
            score = summation*length + 50
            return score
        else: 
            score = summation*length
            return score
            
        
    

n = HAND_SIZE

word = "Waybill"

score = getWordScore(word, n)   
print(f'The word {word} has a score of {score}!')
 
    
    
    
    
    
    
    
