import pygame
import sys
import os
import random
from pygame.locals import *

pygame.init()

clock=pygame.time.Clock()
screen=pygame.display.set_mode((400,400))

side1=[]
side2=[]
n=0

for i in range(0,20):
    side1.append(0)
    side2.append(0)

pos1=False
pos2=False

def empty(x,y):
    pygame.draw.rect(screen, (128,0,0), pygame.Rect(0+x, 0+y, 10, 20))
    pygame.draw.rect(screen, (128,0,0), pygame.Rect(190+x, 0+y, 10, 20))

def right(x,y):
    empty(x,y)
    pygame.draw.rect(screen, (0,128,0), pygame.Rect(10+x, 10+y, 40, 10))

def left(x,y):
    empty(x,y)
    pygame.draw.rect(screen, (0,128,0), pygame.Rect(150+x, 10+y, 40, 10))

def play1(ch):
    global pos1
    if ch==1:
        pos1 = not pos1
        if pos1==True:
            pygame.draw.rect(screen, (0,0,128), pygame.Rect(170, 380, 20, 20))
        if pos1==False:
            pygame.draw.rect(screen, (0,0,128), pygame.Rect(10, 380, 20, 20))
    if ch==2:
        if pos1==True:
            pygame.draw.rect(screen, (0,0,128), pygame.Rect(170, 380, 20, 20))
        if pos1==False:
            pygame.draw.rect(screen, (0,0,128), pygame.Rect(10, 380, 20, 20))

def play2(ch):
    global pos2
    if ch==1:
        pos2 = not pos2
        if pos2==True:
            pygame.draw.rect(screen, (0,0,128), pygame.Rect(370, 380, 20, 20))
        if pos2==False:
            pygame.draw.rect(screen, (0,0,128), pygame.Rect(210, 380, 20, 20))
    if ch==2:
        if pos2==True:
            pygame.draw.rect(screen, (0,0,128), pygame.Rect(370, 380, 20, 20))
        if pos2==False:
            pygame.draw.rect(screen, (0,0,128), pygame.Rect(210, 380, 20, 20))


def crash():
    screen.fill((0,0,0))
    image = pygame.image.load('go.png')
    screen.blit(image,(60,30))

    while True:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #gameDisplay.fill(white)


        #button("Play Again",150,450,100,50,green,bright_green,game_loop)
        #button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)


def disp():
    screen.fill((0,0,0))
    for i in range(0,20):
        if side1[i]==0:
            empty(0,i*20)
        elif side1[i]==1:
            right(0,i*20)
        elif side1[i]==2:
            left(0,i*20)

        if side2[i]==0:
            empty(200,i*20)
        elif side2[i]==1:
            right(200,i*20)
        elif side2[i]==2:
            left(200,i*20)

class MainPart:
    while 1:
        clock.tick(3)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif (event.type == KEYDOWN and event.key == K_a):
                play1(1)
            elif (event.type == KEYDOWN and event.key == K_l):
                play2(1)

        num1=random.randrange(1, 300)%3
        num2=random.randrange(1, 300)%3

        for i in range(0,19):
            side1[19-i]=side1[18-i]
            side2[19-i]=side2[18-i]

        if n%4==0:
            side1[0]=num1
            side2[0]=num2
        else:
            side1[0]=0
            side2[0]=0

        n=n+1

        disp()
        play1(2)
        play2(2)
        global pos1
        if ((side1[19]==1 and pos1==False) or (side1[19]==2 and pos1==True) or (side2[19]==1 and pos2==False) or side2[19]==2 and pos2==True):
            crash()



        pygame.display.flip()


if __name__ == "__main__":
    MainWindow = MainPart()
    MainWindow.MainLoop()
