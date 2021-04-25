from INI import *
import pygame
messi = pygame.image.load('messi-.png')  
class player2_:
    def __init__(self, window):
        self.window = window
        self.X = 600
        self.Y = 235
        self.radius = 30
        window.blit(messi, (self.X, self.Y))
    def move2 (self,dir):
        newX2 = self.X + dir[0]*4
        newY2 = self.Y + dir[1]*4
        if (newX2  < win_width-60 and newX2 > 0):
            self.X = newX2
        if (newY2  < win_height-60 and newY2 > 0):
            self.Y = newY2
        window.blit(messi, (self.X, self.Y))
    
        
