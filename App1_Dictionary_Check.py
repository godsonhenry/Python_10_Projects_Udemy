# Project 1 Translate English Word

import json
import time
from difflib import get_close_matches
import pdb

# Read in Dictionary File
with open('data.json') as ds:
    data=json.load(ds)

# Correct wrong input words:
def correct(word, data):
    if word not in data.keys() and word.title() not in data.keys() and word.upper() not in data.keys():
        lst=get_close_matches(word,data.keys())
        for i in lst:
            s='Do you mean '+i+'? [y/n]'
            judge=input(s)
            if judge=='y':
#                pdb.set_trace()
                return(i)
                break
            elif judge!='n':
                pdb.set_trace()
                print('please input "y" or "n" as your choice')
                correct()
        print('Didn\'t found matching result')
        return word
    elif word in data.keys():
        return word
    elif word.title() in data.keys():
        return word.title()
    elif word.upper() in data.keys():
        return word.upper()

# Search on Dictionary and return result
def word_search(data):
    word=input('Input Word:')
    word=word.lower()
    word=correct(word,data)
    print('Searching ', word, '........')
    time.sleep(2)
    if word in data.keys():
        print(word, ' found!')
        print('Explanation in Disctionary:')
        for a in data[word]:
            print(a)
    else:
        print('Not found ', word, '.......')

word_search(data=data)

# Let user to decide whehther to go?
def again():
    print('\n\n')
    check=input('Do you want to try again? [y/n]:')
    if check.lower()=='y':
        word_search(data=data)
        again()
    elif check.lower()=='n':
        print('Thanks for using this app!')
    else:
        print('please input "y" or "n" as your choice')
        again()
again()


