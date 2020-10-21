# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 14:48:56 2020

@author: littl
"""


import random
r = random.randint(1, 100)
count = 0
while True:
    count = count + 1 # can also be written as count += 1 
    num = int(input("Please guess a number between 1 and 100: "))
    if r == num:
        print ("Congratulations. You guessed it right!")
        print ("This is the", count, "time(s) you tried")
        break
    elif r > num:
        print("It's smaller than the answer.")
    elif r < num:
        print("It's bigger than the answer.")
    print ("This is the", count, "time(s) you tried")
 