import pygame
from INI import *
ball = pygame.image.load('ball.png')
disp_x = win_width
disp_y = win_height
dist = 22
class Ball:
    def __init__(self, window):
        self.window = window
        self.X = int(ball_pos[x])
        self.Y = int(ball_pos[y])
        self.radius = 15
        self.speed = [0 , 0]
        self.goal = [0 , 0]
        window.blit(ball, (self.X, self.Y))
    def move (self):
        self.X = self.X + self.speed[0]
        self.Y = self.Y + self.speed[1]
        k = 0.9#0.7
        self.speed[0] = int(k * self.speed[0])
        self.speed[1] = int(k * self.speed[1])
        
        if (self.X > (disp_x - 30 )): #22px is the line distance
            if (self.Y > 217  and self.Y  < 312 ):
                self.goal = [0 , 1]
            else: 
                self.speed[0] *= -1
                self.X = disp_x - 30  # 770
        if (self.X < 0):
            if (self.Y > 217  and self.Y  < 312 ):
                self.goal = [1 , 0]

            else: 
                self.speed[0] *= -1
                self.X = 0
        if (self.Y > win_height-30 - dist) :
            self.speed[1] *= -1
            self.Y = win_height-30 - dist
        if (self.Y < 0 + dist) :
            self.speed[1] *= -1
            self.Y = 0 + dist
        
        window.blit(ball, (self.X, self.Y))
