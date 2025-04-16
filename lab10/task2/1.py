import pygame
import random
import sqlite3
import json

# Инициализация pygame
pygame.init()

# Параметры экрана
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game with User Progress")

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Подключение к базе данных
conn = sqlite3.connect('snake_game.db')
cursor = conn.cursor()

# Создание таблиц, если они не существуют
cursor.execute('''CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    current_level INTEGER DEFAULT 1
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS user_score (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    score INTEGER,
    game_state TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES user(id)
)''')
conn.commit()

# Уровни
LEVELS = {
    1: {'speed': 10, 'walls': []},
    2: {'speed': 15, 'walls': [(10, 10), (10, 11), (10, 12)]},
    3: {'speed': 20, 'walls': [(15, 15), (15, 16), (15, 17), (16, 17)]}
}

# Функция для рисования сетки
def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, WHITE, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, WHITE, (0, y), (WIDTH, y))

# Функция для рисования змейки
def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

# Функция для рисования еды
def draw_food(food):
    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))

# Функция для рисования стен
def draw_walls(walls):
    for wall in walls:
        pygame.draw.rect(screen, WHITE, (wall[0] * CELL_SIZE, wall[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Функция для генерации случайной позиции
def random_position():
    return random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE)

# Функция для получения пользователя или его создания
def get_or_create_user(username):
    cursor.execute("SELECT id, current_level FROM user WHERE username = ?", (username,))
    user = cursor.fetchone()
    if user:
        print(f"Welcome back {username}! Your current level: {user[1]}")
        return user[0], user[1]
    else:
        cursor.execute("INSERT INTO user (username) VALUES (?)", (username,))
        conn.commit()
        print(f"New user created: {username}")
        return cursor.lastrowid, 1

# Функция для сохранения состояния игры
def save_game_state(user_id, score, game_state):
    cursor.execute("INSERT INTO user_score (user_id, score, game_state) VALUES (?, ?, ?)",
                   (user_id, score, json.dumps(game_state)))
    conn.commit()
    print("Game state saved.")

# Функция для отображения всех игроков
def show_all_players():
    cursor.execute("SELECT username, current_level FROM user")
    users = cursor.fetchall()

    if not users:
        print("Нет зарегистрированных пользователей.")
    else:
        print("Список игроков:")
        for user in users:
            print(f"Имя пользователя: {user[0]}, Уровень: {user[1]}")

# Основное меню
def main_menu():
    print("Добро пожаловать в игру!")
    print("1. Играть")
    print("2. Список игроков")
    choice = input("Выберите действие (1 или 2): ")

    if choice == '1':
        username = input("Введите ваше имя пользователя: ")
        user_id, level = get_or_create_user(username)
        start_game(user_id, level)
    elif choice == '2':
        show_all_players()
        main_menu()
    else:
        print("Неверный выбор. Попробуйте снова.")
        main_menu()

# Функция для начала игры
def start_game(user_id, level):
    clock = pygame.time.Clock()
    level_data = LEVELS.get(level, LEVELS[1])
    speed = level_data['speed']
    walls = [(x * CELL_SIZE, y * CELL_SIZE) for x, y in level_data['walls']]

    snake = [(100, 100)]
    direction = (CELL_SIZE, 0)
    food = random_position()
    score = 0
    running = True
    paused = False

    while running:
        screen.fill(BLACK)
        draw_grid()
        draw_walls([(x, y) for x, y in level_data['walls']])
        draw_snake(snake)
        draw_food(food)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, CELL_SIZE):
                    direction = (0, -CELL_SIZE)
                elif event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE):
                    direction = (0, CELL_SIZE)
                elif event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0):
                    direction = (-CELL_SIZE, 0)
                elif event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
                    direction = (CELL_SIZE, 0)
                elif event.key == pygame.K_p:
                    paused = not paused
                elif event.key == pygame.K_s:
                    state = {
                        'snake': snake,
                        'food': food,
                        'level': level
                    }
                    save_game_state(user_id, score, state)

        if paused:
            continue

        head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        if head in snake or head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
            print("Game Over!")
            break

        for wall in walls:
            if head == wall:
                print("Hit the wall! Game Over!")
                return

        snake.insert(0, head)
        if head == food:
            score += 10
            food = random_position()
        else:
            snake.pop()

        clock.tick(speed)

    pygame.quit()

# Запуск игры
if __name__ == '__main__':
    main_menu()
