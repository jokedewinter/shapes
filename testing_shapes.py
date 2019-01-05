#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 09:51:17 2018

@author: joke
"""

from functionsMove import *
frame = Frame(300, 300)

# All the shapes
amount = 2
shapes = []

for i in range(amount):
    #shapes.append(Square(frame, ((i+1) * 50)))
    shapes.append(Square(frame, 60))
    
    shapes.append(Diamond(frame, 73))
    shapes.append(Circle(frame, 30))

for i in range(100):
    for shape in shapes:
        shape.moveTick()


# More shapes
'''
amount = 3
shapes = []

for i in range(amount):
    #shapes.append(Square(frame, ((i+1) * 50)))
    shapes.append(Square(frame, 50))

for i in range(500):
    for shape in shapes:
        shape.moveTick()
'''

# One shape
'''
vierkant = Square(frame, 100)

for i in range(100):
    vierkant.moveTick()
'''

 