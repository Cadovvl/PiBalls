# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 15:28:55 2014

@author: pasukhov
"""
import pygame
from pygame.locals import *


class AnimationMachine:
    l = []
    
    def addAction(self,x):
        self.l.append(x)
    
    def do(self):
        self.l = [i for i in self.l if i.isAlife()]

    # returns list of (x,y,img) tuple, with coordinates x,y and image
    def getImages(self):
        return [i.getCoordinatesAndImage() for i in self.l]
        

class BasicAnimation:
    
    def isAlife(self):
        return False
    
    def getCoordinatesAndImage(self):
        pass

default_stars = [pygame.image.load("img/star{0}.png".format(i)) for i in range(1,6)]
default_stars = [pygame.transform.scale(i[0], (40 - i[1] * 5,40 - i[1] * 5)) for i in zip(default_stars,range(len(default_stars)))]

class Star(BasicAnimation):
    
    state = 0
    
    def __init__(self, x,y, image_list = default_stars, speed = 0.3):
        self.x = x
        self.y = y
        self.img = image_list
        self.speed = speed
    
    def isAlife(self):
        self.state += 1
        if int(self.state*self.speed) >= len(self.img):
            return False
        else:
            return True
            
    def getCoordinatesAndImage(self):
        return (self.x,self.y,self.img[int(self.state*self.speed)])
        
