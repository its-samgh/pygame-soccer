from INI import *
import pygame
ronaldo = pygame.image.load('ronaldo-.png')  
class player:
    def __init__(self, window):
        self.window = window
        self.X = 140#200
        self.Y = 235
        self.radius = 30
        window.blit(ronaldo, (self.X, self.Y))
    def move (self,dir):
        newX = self.X + dir[0]*4
        newY = self.Y + dir[1]*4
        if (newX  < win_width-60 and newX > 0):
            self.X = newX
        if (newY  < win_height-60 and newY > 0):
            self.Y = newY
        window.blit(ronaldo, (self.X, self.Y))
    
        
