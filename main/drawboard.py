from .boggle import *
import random
import os
from bogglegame import settings

def generate_words():
    '''
    Returns a list of dictionery words.
    by generating words from file of word list.
    '''
    dict = []   
    #reading file containing words in the projectfile
    file_path = os.path.join(settings.BASE_DIR, 'words.txt')

    with open(file_path) as file:
        min_len = 0
        max_len = 6
        length = 4
        dict = []
        word_list = file.readlines()
        while True:
            r_word = random.choice(word_list)
            if len(r_word) >= 4 and len(r_word) <= 6:
                dict.append(r_word.strip('\n').upper())
            if len(dict) == 5:
                break        
    return dict

def drawBoard (randomLetters):

    '''Takes a randomList of 16 characters
    Prints out a 4 x 4 grid'''
    
    board = [[randomLetters [0], randomLetters [1], randomLetters [2], randomLetters [3]],
            [randomLetters [4], randomLetters [5], randomLetters [6], randomLetters [7]],
            [randomLetters [8], randomLetters [9], randomLetters [10], randomLetters [11]],
            [randomLetters [12], randomLetters [13], randomLetters [14], randomLetters [15]]]
    
    return board

def randomLetters (d):
    letters = []
    strings = ''
    for i in d:
        strings+=i

    alphabet = [i for i in strings]
    # alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','w','x','y','z']
    for i in range (0,16,1):
        letters.append((random.choice(alphabet)).upper())
    return letters

def get_boogle(d):
    # root Node of trie
    t = Boogle()

    # insert all words of dictionary into trie
    n = len(d)
    for i in range(n):

        t.insert(d[i])
    root = t.root
        # demo_boggle = [['G', 'I', 'Z', 'F'],
        #         ['U', 'E', 'K', 'O'],
        #         ['Q', 'E', 'R', 'O'],
        #         ['Y', 'M', 'C', 'L']]

    letterList = randomLetters(d)
    boggle = drawBoard(letterList)

    return boggle,root



    


