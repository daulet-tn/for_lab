import pygame

# Инициализация Pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 1500, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint in Pygame")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
current_color = BLACK

# Переменные состояния
running = True
mode = "brush"  # brush, rectangle, circle, eraser
start_pos = None
size = 5  # Размер кисти / ластика

# Очистка экрана
screen.fill(WHITE)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = "rectangle"
            elif event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_b:
                mode = "brush"
            elif event.key == pygame.K_e:
                mode = "eraser"
            elif event.key == pygame.K_1:
                current_color = RED
            elif event.key == pygame.K_2:
                current_color = GREEN
            elif event.key == pygame.K_3:
                current_color = BLUE

        elif event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = event.pos
        
        elif event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]:
            if mode == "brush":
                pygame.draw.circle(screen, current_color, event.pos, size)
            elif mode == "eraser":
                pygame.draw.circle(screen, WHITE, event.pos, size)
        
        elif event.type == pygame.MOUSEBUTTONUP:
            end_pos = event.pos
            if mode == "rectangle" and start_pos:
                rect_width = abs(end_pos[0] - start_pos[0])
                rect_height = abs(end_pos[1] - start_pos[1])
                pygame.draw.rect(screen, current_color, (min(start_pos[0], end_pos[0]), 
                                                         min(start_pos[1], end_pos[1]),
                                                         rect_width, rect_height), 2)
            elif mode == "circle" and start_pos:
                radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
                pygame.draw.circle(screen, current_color, start_pos, radius, 2)
    
    pygame.display.flip()

pygame.quit()
