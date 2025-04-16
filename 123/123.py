import pygame 
import random

#цвета 
white = (255, 255, 255)
food = (255, 0, 0)
blik_size = 20
snake_color = (0, 102, 0)
blue = (204, 255, 255)

#Направление 
UP = (0, 1)
RIGHT = (1, 0)
LEFT = (-1, 0)
DOWN = (0, -1)

#Старт 
direction = RIGHT
speed = 5


pygame.init()
screen = pygame.display.set_mode((700,700))
pygame.display.set_caption("Snake")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip() 