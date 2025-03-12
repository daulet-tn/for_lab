import os
current_dir = os.path.dirname(__file__)  # Получаем папку, где находится сам скрипт
image_path = os.path.join(current_dir, 'mickeyclock.jpeg')  # Создаем путь к файлу

background = pygame.image.load(image_path)  # Загружаем изображение

import pygame
pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basic Window")

background = pygame.image.load('/Users/daulet/Documents/GitHub/for_lab/lab7/mickeyclock.jpeg')

screen.blit(background, (0,0))
pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
