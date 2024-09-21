import pygame
from pygame.locals import *
import sys
import time

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("nave space")

bg = 'space.webp'
bg1 = pygame.image.load(bg).convert()
bg1 = pygame.transform.scale(bg1, (850, 650))

nave = 'nave.png'
token = pygame.image.load(nave)
token = pygame.transform.scale(token, (120, 120))

nave1 = 'nave_x1.png'
token1 = pygame.image.load(nave1)
token1 = pygame.transform.scale(token1, (200, 200))

token2 = pygame.image.load(nave1)
token2 = pygame.transform.scale(token2, (200, 200))


bala_1 = 'bala.png'
bala_2 = 'bala.png'
bala1 = pygame.image.load(bala_1)
bala2 = pygame.image.load(bala_2)
bala_3 = 'bala2.png'
bala3 = pygame.image.load(bala_3)
bala4 = pygame.image.load(bala_3)

blue = (0, 0, 255)

x, y = 350, 400
speed = 0.5
x_bala1, x_bala2, y_bala1, y_bala2 = x+2, x-10, y, y
x_1, y_1 = 420, 30
x_2, y_2 = 200, 30
x_b3, y_b3 = 490, 60
x_b4, y_b4 = 270, 60

if __name__ == "__main__":
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= speed
        if keys[pygame.K_RIGHT]:
            x += speed
        
        screen.blit(bg1, (0, 0))
        screen.blit(bala1,(x_bala1, y_bala1))
        screen.blit(bala2,(x_bala2, y_bala2))
        screen.blit(bala3,(x_b3, y_b3))
        screen.blit(bala4, (x_b4, y_b4))
        screen.blit(token, (x, y))
        screen.blit(token1, (x_1, y_1))
        screen.blit(token2, (x_2, y_2))
        
        y_bala1 = y_bala1 - speed
        y_bala2 = y_bala2 - speed
        y_b3 = y_b3 + speed
        y_b4 = y_b4 + speed
        
        if y_bala1 == 32 and y_bala2 == 32:
          y_bala2=400
          y_bala1=400
          x_bala1=x
          x_bala2=x
          
        
        if y_b3 == 580:
            y_b3 = y_1
            
        if y_b4 == 580:
            y_b4 = y_2
           
        if y_b3 == y and x_b3 > x-32 and x_b3 < x+110:
           x = 2000
           
        if y_b4 == y and x_b4 > x-32 and x_b4 < x+110:
           x = 2000
        
        if y_bala1 == y_1 + 80 and x_bala1 > x_b3 -64 and x_bala1 < x_b3 + 64:
             x_1 = 2000
             x_b3 = 3000
             
        if y_bala1 == y_2 + 80 and x_bala1 > x_2 -64 and x_bala1 < x_2 + 64:
             x_2 = 2000
             x_b3 = 3000
        
        pygame.display.flip()
