import pygame
import psycopg2
import random
import time

# Подключение к базе данных
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="061214500802",
    host="localhost",
)
cur = conn.cursor()

# Создание таблиц
def init_db():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) UNIQUE
        );
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS user_scores (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            score INTEGER,
            level INTEGER
        );
    """)
    conn.commit()



# create_tables()

# Получение или создание пользователя
def get_or_create_user(name):
    cur.execute("SELECT id FROM users WHERE name = %s", (name,))
    user = cur.fetchone()
    if user:
        user_id = user[0]
        cur.execute("""
            SELECT score, level FROM user_scores 
            WHERE user_id = %s ;
        """, (user_id,))
        last_data = cur.fetchone()
        return user_id, (last_data if last_data else (0, 1))
    else:
        cur.execute("INSERT INTO users(name) VALUES(%s) RETURNING id;", (name,))
        user_id = cur.fetchone()[0]
        conn.commit()
        return user_id, (0, 1)

init_db()


name = input("Введите ваше имя: ")
user_id, (last_score, last_level) = get_or_create_user(name)
print(f"Последний уровень: {last_level}, последний счет: {last_score}")


pygame.init()
WIDTH, HEIGHT = 600, 600
CELL = 30
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")


colorWHITE = (255, 255, 255)
colorGRAY = (200, 200, 200)
colorBLACK = (0, 0, 0)
colorRED = (255, 0, 0)
colorYELLOW = (255, 255, 0)
colorGREEN = (0, 255, 0)
colorPURPLE = (128, 0, 128)
colorWALL = (222, 96, 38)


font = pygame.font.SysFont("Verdana", 60)
score_font = pygame.font.SysFont("Verdana", 20)

def draw_grid():
    for x in range(0, WIDTH, CELL):
        for y in range(0, HEIGHT, CELL):
            pygame.draw.rect(screen, colorGRAY, (x, y, CELL, CELL), 1)

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx, self.dy = 1, 0
        self.score = last_score
        self.level = last_level
        self.growing = False
        self.cnt = 0

    def move(self):
        new_head = Point((self.body[0].x + self.dx) % (WIDTH // CELL),
                         (self.body[0].y + self.dy) % (HEIGHT // CELL))
        if any(seg.x == new_head.x and seg.y == new_head.y for seg in self.body):
            return False
        self.body.insert(0, new_head)
        if not self.growing: self.body.pop()
        else: self.growing = False
        return True

    def draw(self):
        pygame.draw.rect(screen, colorRED, (self.body[0].x * CELL, self.body[0].y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food_manager):
        for food in list(food_manager.foods):
            if food and self.body[0].x == food.pos.x and self.body[0].y == food.pos.y:
                self.growing = True
                self.score += food.value
                self.cnt += food.value
                food_manager.remove_food(food)
                if self.cnt >= 7:
                    self.level += 1
                    self.cnt = self.cnt % 7
                return

    def hit_wall(self):
        head_rect = pygame.Rect(self.body[0].x * CELL, self.body[0].y * CELL, CELL, CELL)
        return any(head_rect.colliderect(wall) for wall in walls)


class Food:
    def __init__(self):
        self.pos = self.random_pos()
        self.spawn_time = time.time()
        self.lifetime = random.uniform(5, 15)
        self.value = 1

    def random_pos(self):
        while True:
            p = Point(random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1))

            in_snake = any(seg.x == p.x and seg.y == p.y for seg in snake.body)

            food_rect = pygame.Rect(p.x * CELL, p.y * CELL, CELL, CELL)
            in_wall = any(food_rect.colliderect(wall) for wall in walls)

            if not in_snake and not in_wall:
                return p


    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def is_expired(self):
        return time.time() - self.spawn_time > self.lifetime

class SpecialFood(Food):
    def __init__(self):
        super().__init__()
        self.value = 3
        self.lifetime = random.uniform(3, 7)

    def draw(self):
        pygame.draw.rect(screen, colorPURPLE, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

class FoodManager:
    def __init__(self):
        self.foods = []
        self.last_spawn = time.time()
        self.spawn_interval = 3

    def update(self):
        now = time.time()
        self.foods = [f for f in self.foods if not f.is_expired()]
        if now - self.last_spawn > self.spawn_interval:
            self.spawn_food()
            self.last_spawn = now

    def spawn_food(self):
        self.foods.append(SpecialFood() if random.random() < 0.3 else Food())

    def remove_food(self, food):
        if food in self.foods:
            self.foods.remove(food)

    def draw(self):
        for food in self.foods:
            food.draw()

def save_game():
    cur.execute("DELETE FROM user_scores WHERE user_id = %s", (user_id,))
    conn.commit()

    cur.execute("""
        INSERT INTO user_scores(user_id, score, level)
        VALUES (%s, %s, %s)
    """, (user_id, snake.score, snake.level))
    conn.commit()
    print("Игра сохранена.")



snake = Snake()
food_manager = FoodManager()
clock = pygame.time.Clock()
paused = False
running = True


walls = []

def draw_level_walls(level):
    walls.clear()
    if level >= 2:
        rect1 = pygame.Rect(5 * CELL, 10 * CELL, CELL * 10, CELL)
        walls.append(rect1)
        pygame.draw.rect(screen, colorWALL, rect1)
    if level >= 3:
        rect2 = pygame.Rect(9 * CELL, 15 * CELL, CELL * 2, CELL * 5)
        walls.append(rect2)
        pygame.draw.rect(screen, colorWALL, rect2)
    if level >= 4:
        rect3 = pygame.Rect(9 * CELL, 0, CELL * 2, CELL * 5)
        walls.append(rect3)
        pygame.draw.rect(screen, colorWALL, rect3)


while running:
    screen.fill(colorBLACK)
    draw_grid()
    draw_level_walls(snake.level)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = not paused
                if paused:
                    save_game()
            elif not paused:
                if event.key == pygame.K_UP and snake.dy == 0: snake.dx, snake.dy = 0, -1
                elif event.key == pygame.K_DOWN and snake.dy == 0: snake.dx, snake.dy = 0, 1
                elif event.key == pygame.K_LEFT and snake.dx == 0: snake.dx, snake.dy = -1, 0
                elif event.key == pygame.K_RIGHT and snake.dx == 0: snake.dx, snake.dy = 1, 0

    if not paused:
        food_manager.update()
        if not snake.move() or snake.hit_wall():
            save_game()
            screen.fill(colorBLACK)
            game_over_text = font.render("Game Over", True, colorRED)
            center_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(game_over_text, center_rect)
            pygame.display.flip()
            pygame.time.delay(2000)
            running = False


        snake.check_collision(food_manager)

    snake.draw()
    food_manager.draw()

    score_text = score_font.render(f"Счет: {snake.score} | Уровень: {snake.level}", True, colorWHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(5 + snake.level * 0.5)

pygame.quit()
conn.close()