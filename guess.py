# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 14:48:56 2020

@author: littl
"""


import random
r = random.randint(1, 100)
while True:
    num = int(input("Please guess a number between 1 and 100: "))
    if r == num:
        print ("Congratulations. You guessed it right!")
        break
    elif r > num:
        print("Too bad, it's smaller than the answer.")
    elif r < num:
        print("Too bad, it's bigger than the answer.")
    
