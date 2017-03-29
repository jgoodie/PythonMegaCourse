#!/usr/local/bin/python3

import random, string
# Version 1
# def gen():
#     l1 = random.choice(string.ascii_lowercase)
#     l2 = random.choice(string.ascii_lowercase)
#     l3 = random.choice(string.ascii_lowercase)
#     name = l1 + l2 + l3
#     return(name)
# 
# for x in range(5):
#     print(gen())

# Version 2
vowels = 'aeiouy'
consonants = 'bcdfghjklmnpqrstvwxz'
letters = vowels + consonants

l1 = input("Enter v for vowels, c for consonants, l for any letter: ")
l2 = input("Enter v for vowels, c for consonants, l for any letter: ")    
l3 = input("Enter v for vowels, c for consonants, l for any letter: ")

def gen():
    # Letter 1
    if l1 == 'v':
        n1 = random.choice(vowels)
    elif l1 == 'c':
        n1 = random.choice(consonants)
    elif l1 == 'l':
        n1 = random.choice(letters)
    else:
        n1 = l1
    
    # Letter 2
    if l2 == 'v':
        n2 = random.choice(vowels)
    elif l2 == 'c':
        n2 = random.choice(consonants)
    elif l2 == 'l':
        n2 = random.choice(letters)
    else:
        n2 = l2   
        
    # Letter 3
    if l3 == 'v':
        n3 = random.choice(vowels)
    elif l3 == 'c':
        n3 = random.choice(consonants)
    elif l3 == 'l':
        n3 = random.choice(letters)
    else:
        n3 = l3
    
    return(n1+n2+n3) 

for x in range(5): 
    print(gen())
    


