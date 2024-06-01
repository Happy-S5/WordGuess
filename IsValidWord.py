# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 13:00:21 2023

@author: miram
"""
import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList


def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    #print(wordList)
    word = word.lower()
    LHandCopy = []
    LHand = []
    print (word)
    handCopy = {}
    if word in wordList: 
        for i in word: 
            print(i)
            if i not in hand:
                return False
            try: 
                handCopy[i] += 1 
            except KeyError: 
                handCopy[i] = 1
                
        shared_items = {k: handCopy[k] for k in handCopy if k in hand and handCopy[k] <= hand[k]} 
        print(f'The shared items is {shared_items}')
        if shared_items == handCopy: 
            return True
        else:
            return False
            
        print (f'The hand is {hand}, and the handCopy is {handCopy}')
        #return result
    else: 
        return False
    


wordList = loadWords()
hand = {'r': 2, 'a': 1, 'p': 2, 'e': 1, 't': 1, 'u': 1}

word = 'rapture' 
print(isValidWord(word, hand, wordList))    
    
    
    
    
    
    
    
    
    
    







