# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 09:51:05 2023

@author: miram
"""

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    
    handCopy = hand.copy()
        
    for i in word:
        #print (f'The handCopy for loop i is {i}')
        if i in handCopy: 
            #print(f'The i value is : {i}')
            handCopy[i] = handCopy.get(i, 0)-1 
            #print(f'This is the inner handCopy {handCopy}')
            
            
word = "hello"
hand = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
updateHand(hand, word)           