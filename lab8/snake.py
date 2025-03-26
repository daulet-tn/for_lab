import pygame 
import random 

#переменные которые буду использовать в процессе цвета 
frame_color = (0, 255, 204)
white = (255, 255, 255)
blok_size = 20
count_blok = 27
blue = (204, 255, 255)
margin = 1
snake_color = (0, 102, 0)
food_color = (255, 0, 0)
 
# Направления 
UP = (-1, 0)   
DOWN = (1, 0)  
LEFT = (0, -1) 
RIGHT = (0, 1) 


# Начальное направление 
direction = RIGHT
speed = 5

pygame.init()
screen = pygame.display.set_mode((600, 700))
pygame.display.set_caption('Snake')

class SnakeBlok:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def draw_text(text, x, y, size=30, color=(0, 0, 0)):
    font = pygame.font.Font(None, size)  
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def draw_blok(color, row, column):
    pygame.draw.rect(screen, color,[15 + column * blok_size + margin * (column + 1) ,
                                     40 + row * blok_size + margin * (row + 1), 
                                     blok_size, blok_size ] )

def get_random_food():
    return SnakeBlok(random.randint(0, count_blok - 1), random.randint(0, count_blok - 1))

snake_block = [SnakeBlok(6, 5), SnakeBlok(5, 6)]
food = get_random_food()
clock = pygame.time.Clock()

running = True
while running:
    screen.fill(frame_color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != DOWN:
                direction = UP
            elif event.key == pygame.K_DOWN and direction != UP:
                direction = DOWN
            elif event.key == pygame.K_LEFT and direction != RIGHT:
                direction = LEFT
            elif event.key == pygame.K_RIGHT and direction != LEFT:
                direction = RIGHT

    # Двигаем змейку
    head = snake_block[-1]
    new_head = SnakeBlok(head.x + direction[0], head.y + direction[1])

     # Проверяем столкновение со стенами
    if new_head.x < 0 or new_head.x >= count_blok or new_head.y < 0 or new_head.y >= count_blok:
        running = False  # Игра заканчивается
    
    # Проверяем столкновение с самой собой
    if new_head in snake_block:
        running = False  # Игра заканчивается

    snake_block.append(new_head)
    
    if new_head.x == food.x and new_head.y == food.y:
        food = get_random_food()
        speed += 1
    else:
        snake_block.pop(0)
    
    for row in range(count_blok):
        for column in range(count_blok):
            if (row + column) % 2 == 0:
                color = blue
            else:
                color = white
            draw_blok(color, row, column)

    for block in snake_block:
        draw_blok(snake_color, block.x, block.y)

    draw_blok(food_color, food.x, food.y)
    draw_text(f"Score: {len(snake_block) - 2}", 20, 10, 36, (255, 255, 255))

    pygame.display.flip()
    clock.tick(speed)


pygame.quit()


            
