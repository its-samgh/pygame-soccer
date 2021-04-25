import pygame
import math

from INI import *
from Ball import *
from Player import *
from Player2 import *



pygame.init()
pygame.font.init()
pygame.display.set_caption('Fifa League')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
myfont = pygame.font.Font("EASPORTS15.ttf",30)
mybfont = pygame.font.Font("EASPORTS15.ttf",60)
#my2font = pygame.font.SysFont('Comic Sans MS', 30)

window = pygame.display.set_mode((win_width, win_height + 30))

BackGround = pygame.image.load('Field.jpg')  

done = False

points = [0 , 0]
player1 = player(window)
player2 = player2_(window)
ball1 = Ball(window)

def zarbe (x1, y1, r1, x2, y2, r2):
    if ((x1-x2)**2 + (y1-y2)**2) <= (r1 + r2)**2:

        return True
    else:
        return False

counter = 30 #.rjust(3)
text = '30'
minu = 3 
text_mn =  '3'#.rjust(3)

pygame.time.set_timer(pygame.USEREVENT, 1000)

game_status = 1

while not done :
    
    if game_status == 1:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:        
            pygame.quit()
        if counter == 0 and minu == 0:
            game_status = 2
        if event.type == pygame.USEREVENT: 
                counter -= 1
                text = str(counter)#.rjust(3) #if counter + minu > 0 else 'Golden Goal!'
        if counter == 0:
            if minu == 0 :
                game_status = 2
            minu -= 1
            if game_status == 2:
                minu = 0
            text_mn = str(minu)#.rjust(3)
            
            counter = 60
        
        dirX = 0
        dirY = 0
        dirX2 = 0
        dirY2 = 0
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w] : 
            dirY += -2
        if pressed[pygame.K_s]  : 
            dirY += 2
        if pressed[pygame.K_a]                      : 
            dirX += -2
        if pressed[pygame.K_d]                     : 
            dirX += 2

        playerDir = [dirX , dirY]

        if pressed[pygame.K_UP] : 
            dirY2 += -2
        if pressed[pygame.K_DOWN]                      : 
            dirY2 += 2
        if pressed[pygame.K_LEFT]                      : 
            dirX2 += -2
        if pressed[pygame.K_RIGHT]                     : 
            dirX2 += 2

        playerDir2 = [dirX2 , dirY2]
        mpx = (player1.X + dirX) - (player2.X + dirX2)
        mpy = (player1.Y + dirY) - (player2.Y + dirY2)
        distance = (mpx ** 2 )+ (mpy ** 2)

        distance = math.sqrt(distance)
          
        window.fill([255, 255, 255])
        window.blit(BackGround, [0,0])
        if distance >= 60:
            player1.move(playerDir)
            player2.move2(playerDir2)
        else:
            player1.move([1,1])
            player2.move2([-1,-1])
        if zarbe(player1.X + 30,player1.Y+30,player1.radius,ball1.X+15,ball1.Y+15,ball1.radius):
            dirX = int((ball1.X - player1.X - 15))
            dirY = int((ball1.Y - player1.Y - 15))
        
            ball1.speed = [dirX, dirY]

        if zarbe(player2.X+30,player2.Y+30,player2.radius,ball1.X+15,ball1.Y+15,ball1.radius):
            dirX = int((ball1.X - player2.X - 15))
            dirY = int((ball1.Y - player2.Y - 15))

        
            ball1.speed = [dirX, dirY]
        ball1.move()
        if (ball1.goal != [0 , 0]):
            points[0] += ball1.goal[0]
            points[1] += ball1.goal[1]
            
            player1 = player(window)
            player2 = player2_ (window)
            ball1 = Ball(window)

        
        player1PointsText = myfont.render(str(points[1]), False, (0, 0, 0))
        player2PointsText = myfont.render(str(points[0]), False, (0, 0, 0))
        real_time = text_mn + ':' + text
        #print(real_time)
        timer = myfont.render(real_time, True, (0, 0, 0))
        
        window.blit(player1PointsText,(int(win_width/2) - int(win_width/10),530))
        window.blit(player2PointsText,(int(win_width/2) + int(win_width/10 - 25),530))

        window.blit(timer, (2 ,530))
        
        pygame.display.update()
        
        clock = pygame.time.Clock().tick(60)

        
    if game_status == 2:
        if points[0] > points[1]:
            rest = 'Ronaldo Won!'
        elif points[0] < points[1]:
            rest = 'Messi Won!'
        else:
            rest = 'Draw!'
            
        event = pygame.event.poll()
        if event.type == pygame.QUIT:        
            pygame.quit()
            
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_q] :
            #done = True
            pygame.quit()
        prs = myfont.render('Press Q to Quit', False, (0, 0, 0))
        res = mybfont.render(rest, False, (0, 0, 0))
        
        window.blit(res, (300 ,225))

        window.blit(prs, (300 ,465))
        
        pygame.display.update()
        
        clock = pygame.time.Clock().tick(60)

        
#pygame.quit()



        
