#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 20:49:11 2018

@author: joke
"""

from functionsMove import *

frame = Frame(300,300)
vierkant = Square(frame, 60)
#cirkel = Circle(frame, 75)
diamant = Diamond(frame, 73)

for i in range(100):
    vierkant.moveTick()
    #cirkel.moveTick()
    diamant.moveTick()
