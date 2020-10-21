# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 14:48:56 2020

@author: littl
"""


import random
start = int(input("Please decide a starting point (a number) of the range: "))
end = int(input("please decide an ending point (a number) of the range: "))
r = random.randint(start, end)
count = 0
while True:
    count = count + 1 # can also be written as count += 1 
    num = int(input("Please guess a number within the range:"))
    if r == num:
        print ("Congratulations. You guessed it right!")
        print ("This is the", count, "time(s) you tried")
        break
    elif r > num:
        print("It's smaller than the answer.")
    elif r < num:
        print("It's bigger than the answer.")
    print ("This is the", count, "time(s) you tried")
 