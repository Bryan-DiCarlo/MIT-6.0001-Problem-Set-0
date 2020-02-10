# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 13:03:16 2020

@author: bryan
"""

#Write a program that does the following in order:

#1. Asks the user to enter a number “x”
#2. Asks the user to enter a number “y”
#3. Prints out number “x”, raised to the power “y”.
#4. Prints out the log (base 2) of “x”.

#I have chosen to calculate the log base2 with the Python math module
#Additionally I have added print statements to identify the user's input

import math
x = int(input('Please enter first number:>>> '))
y = int(input('Please enter second number:>>> '))
print(f'x = {x}')
print(f'y = {y}')
print(f'x**y = {x}**{y} = {x**y}')
print(f'log(base2) of x = log(base2) of {x} = {math.log2(x)}')