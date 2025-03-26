import pygame
import random

# Инициализация Pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Скорость игры
clock = pygame.time.Clock()
speed = 5

# Загрузка изображения машины
car_img = pygame.image.load("lab8/10382282.png")  # Добавь картинку в папку с кодом
car_width, car_height = 50, 100
car_x, car_y = WIDTH // 2 - car_width // 2, HEIGHT - car_height - 20

# Класс монет
class Coin:
    def __init__(self):
        self.x = random.randint(100, WIDTH - 100)
        self.y = random.randint(-600, -50)
        self.radius = 15

    def move(self):
        self.y += speed // 2
        if self.y > HEIGHT:
            self.y = random.randint(-600, -50)
            self.x = random.randint(100, WIDTH - 100)

    def draw(self):
        pygame.draw.circle(screen, YELLOW, (self.x, self.y), self.radius)

# Создание списка монет
coins = [Coin() for _ in range(5)]
coins_collected = 0

running = True
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Движение машины
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 100:
        car_x -= speed
    if keys[pygame.K_RIGHT] and car_x < WIDTH - 100 - car_width:
        car_x += speed
    
    # Отрисовка машины
    screen.blit(car_img, (car_x, car_y))
    
    # Отрисовка и движение монет
    for coin in coins:
        coin.move()
        coin.draw()
        
        # Проверка столкновения с монетами
        if abs(car_x + car_width//2 - coin.x) < 30 and abs(car_y + car_height//2 - coin.y) < 30:
            coins_collected += 1
            coin.y = random.randint(-600, -50)
            coin.x = random.randint(100, WIDTH - 100)
    
    # Вывод количества собранных монет
    font = pygame.font.Font(None, 36)
    text = font.render(f"Coins: {coins_collected}", True, BLACK)
    screen.blit(text, (WIDTH - 150, 20))
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
