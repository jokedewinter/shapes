#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 11:00:04 2019

@author: joke
"""

#####------------------TASK 3----------
from Shapes import *

from pylab import random as r
class MovingShape:
    def __init__(self,frame,shape,diameter):
        self.shape = shape
        self.diameter = diameter
        self.figure = Shape(shape,diameter)
#####-------------TASK 5---------------
####----TASK 8 CONTINUED----------------
        self.x = self.minx + r() * (self.maxx - self.minx)
        self.y = self.miny + r() * (self.maxy - self.miny)
        self.dx = 5 + 10 * r() < 0.5
        self.dy = 5 + 10 * r() < 0.5

       # self.goto(self.x, self.y)
        
####-------TASK 5 & 7 ABOVE-------------
    def goto(self,x,y):
        self.figure.goto(x,y)
    def moveTick(self):
        pass
        
        
class Square(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'square',diameter)
        
class Diamond(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'diamond',diameter)
  
class Circle(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'circle',diameter)