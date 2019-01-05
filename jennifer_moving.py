#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 11:00:55 2019

@author: joke
"""
'''
from Shapes import *
import time

#frame = shape.Frame()

frame = Frame()

s1 = Shape('square', 100)
s1.goto(200,100)
 
x = 0
y = 0

#####--------------TASK TWO--------------------

for i in range(100):
        s1.goto(x,y)
        x = x + 5
        y = y + 5
        time.sleep(0.03)
'''  

from jennifer_functions import *    
frame = Frame()

numshapes = 3

shapes = []
for i in range(numshapes):
    shapes.append(Square(frame,100))
for i in range(100):
    for shape in shapes:
        shape.moveTick()
        