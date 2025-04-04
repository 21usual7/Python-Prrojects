import pygame
import random

pygame.init()

# Основные настройки
WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка в Pygame")
clock = pygame.time.Clock()

# Цвета
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
WHITE = (255, 255, 255)

# Параметры змейки
snake_x = WIDTH // 2
snake_y = HEIGHT // 2
snake_block = 10
move_x = 0
move_y = 0
snake_length = 1
snake_body = []

# Загружаем изображение еды
food_image = pygame.image.load('apple.jpg')
food_image_scaled = pygame.transform.scale(food_image, (snake_block, snake_block))
food_image_rect = food_image_scaled.get_rect()
food_image_rect.x = random.randint(0, (WIDTH - snake_block) // snake_block) * snake_block
food_image_rect.y = random.randint(0, (HEIGHT - snake_block) // snake_block) * snake_block

# Счёт
score = 0
font = pygame.font.SysFont("comicsansms", 35)

def draw_lost(message):
    """Вывод сообщения о проигрыше или победе."""
    WIN.fill(GREY)  # Очистка экрана
    text = font.render(message, True, BLACK)
    WIN.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.update()  # Обновление экрана
    pygame.time.delay(3000)  # Задержка 3 секунды перед завершением

running = True
while running:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and move_x == 0:  # Исключение движения "назад"
                move_x = -snake_block
                move_y = 0
            elif event.key == pygame.K_d and move_x == 0:
                move_x = snake_block
                move_y = 0
            elif event.key == pygame.K_w and move_y == 0:
                move_y = -snake_block
                move_x = 0
            elif event.key == pygame.K_s and move_y == 0:
                move_y = snake_block
                move_x = 0

    # Обновляем координаты змейки
    snake_x += move_x
    snake_y += move_y

    # Ограничение выхода за экран
    if snake_x < 0 or snake_x >= WIDTH or snake_y < 0 or snake_y >= HEIGHT:
        draw_lost("Game Over")
        running = False

    # Проверяем, съела ли змея еду
    if snake_x == food_image_rect.x and snake_y == food_image_rect.y:
        food_image_rect.x = random.randint(0, (WIDTH - snake_block) // snake_block) * snake_block
        food_image_rect.y = random.randint(0, (HEIGHT - snake_block) // snake_block) * snake_block
        score += 1
        snake_length += 1
        if score >= 10:  # Условие победы
            draw_lost("You Win!")
            running = False

    # Обновляем тело змейки
    snake_body.append((snake_x, snake_y))
    if len(snake_body) > snake_length:
        snake_body.pop(0)

    # Проверка столкновения головы с телом
    for block in snake_body[:-1]:
        if snake_x == block[0] and snake_y == block[1]:
            draw_lost("Game Over")
            running = False

    # Рендеринг
    WIN.fill(GREEN)

    # Отрисовка змейки
    for block in snake_body:
        pygame.draw.rect(WIN, BLACK, (block[0], block[1], snake_block, snake_block))
    
    # Отрисовка еды
    WIN.blit(food_image_scaled, food_image_rect)

    # Отображение счёта
    text = font.render(f"Score: {score}", True, BLACK)
    WIN.blit(text, (10, 10))

    pygame.display.update()

pygame.quit()