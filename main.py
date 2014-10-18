# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import sys
import copy
import time
import animation

pygame.init()

size=[1000,640]
font = pygame.font.Font(pygame.font.get_default_font(), 12)
screen=pygame.display.set_mode(size)
pygame.display.set_caption('I\'m PAVEEEEEEL')
clock=pygame.time.Clock()
am = animation.AnimationMachine()

def on_animation():
    am.do()
    for i in am.getImages():
        screen.blit(i[2], (i[0], i[1]))

done = False

am.addAction(animation.Star(50,50, speed=0.05))

while done==False:
    for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop
                forceQuit = True
    # ОБРАБОТКА ВСЕХ СОБЫТИЙ ДОЛЖНА БЫТЬ ПОД ЭТИМ КОММЕНТАРИЕМ
    
    # ОБРАБОТКА ВСЕХ СОБЫТИЙ ДОЛЖНА НАХОДИТЬСЯ НАД ЭТИМ КОММЕНТАРИЕМ
     
    # ВСЯ ИГРОВАЯ ЛОГИКА ДОЛЖНА НАХОДИТЬСЯ ПОД ЭТИМ КОММЕНТАРИЕМ
     
    
    # ВСЯ ИГРОВАЯ ЛОГИКА ДОЛЖНА НАХОДИТЬСЯ НАД ЭТИМ КОММЕНТАРИЕМ
    
    	
    # ВЕСЬ КОД ДЛЯ РИСОВАНИЯ ДОЛЖЕН НАХОДИТЬСЯ ПОД ЭТИМ КОММЕНТАРИЕМ

    on_animation()    
    
    # ВЕСЬ КОД ДЛЯ РИСОВАНИЯ ДОЛЖЕН НАХОДИТЬСЯ НАД ЭТИМ КОММЕНТАРИЕМ
    
    # Ограничить до 20 кадров в секунду
    clock.tick(20)	

    
pygame.quit()
