#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 09:41:10 2018

@author: joke
"""

from Shapes import *
from pylab import random as r


class MovingShape:
    def __init__(self, frame, shape, diameter):

        self.shape = shape
        self.diameter = diameter
        self.figure = Shape(shape, diameter)

        # Initialising X and Y
        '''
        The initial state is half the diameter to have them 
        positioned inside the frame.
        '''
        self.x = self.diameter / 2
        self.y = self.diameter / 2

        # Random moving direction and velocity
        self.dx = 10 #* r()
        self.dy = 10 #* r()
        
        if (r() < 0.5):
            self.dx = self.dx * -1 
        else:
            self.dy = self.dy * -1
        
        # Start position
        self.minx = self.diameter / 2
        self.maxx = frame.width - self.minx

        self.miny = self.diameter / 2
        self.maxy = frame.height - self.miny

        # X and Y
        self.x = self.minx + r() * (self.maxx - self.minx)
        self.y = self.miny + r() * (self.maxy - self.miny)
        
        self.goto(self.x, self.y)
        
    def goto(self, x, y):
        self.figure.goto(x, y)
    
    def moveTick(self):
#        pass
     
        self.x += self.dx
        self.y += self.dy
        
        # if x is neg and x < xmin : x becomes pos
        if (self.x < self.minx):
            self.x = self.minx + self.dx
            self.dx = abs(self.dx)
            
        # if x is pos and x > xmax : x becomes neg
        elif (self.x >= 0) and (self.x > self.maxx):
            self.x = self.maxx - self.dx
            self.dx = self.dx * -1
      
        # if y is neg and y < ymin : y becomes pos
        if (self.y < self.miny):
            self.y = self.miny + self.dy
            self.dy = abs(self.dy)
            
        # if y is pos and y > ymax : y becomes neg
        elif (self.y >= 0) and (self.y > self.maxy):
            self.y = self.maxy - self.dy
            self.dy = self.dy * -1
          
        self.figure.goto(self.x, self.y)
        
class Square(MovingShape):
    def __init__(self, frame, diameter):
        MovingShape.__init__(self, frame, 'square', diameter)
        
class Diamond(MovingShape):
    def __init__(self, frame, diameter):
        MovingShape.__init__(self, frame, 'diamond', diameter)
        
        # Start position
        '''
        The 0.7 is 50 / 71
        A square with a diameter of 50px turned into a diamond
        will create a surface square of 71px
        '''
        self.minx = self.diameter * 0.7
        self.maxx = frame.width - self.minx

        self.miny = self.diameter * 0.7
        self.maxy = frame.height - self.miny

        # X and Y
        self.x = self.minx + r() * (self.maxx - self.minx)
        self.y = self.miny + r() * (self.maxy - self.miny)

        
class Circle(MovingShape):
    def __init__(self, frame, diameter):
        MovingShape.__init__(self, frame, 'circle', diameter)
