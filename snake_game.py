import pygame
import random

# Initialize Pygame
pygame.init()

# Screen size
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Snake Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Clock
clock = pygame.time.Clock()
FPS = 10

# Snake setup
snake_block = 20
snake_speed = 10
snake_list = [[100, 50]]
snake_direction = "RIGHT"

# Food setup
food_x = round(random.randrange(0, WIDTH - snake_block) / 20) * 20
food_y = round(random.randrange(0, HEIGHT - snake_block) / 20) * 20

# Score
score = 0

# Font
font = pygame.font.SysFont(None, 35)

def draw_snake(snake_list):
    for x, y in snake_list:
        pygame.draw.rect(screen, GREEN, [x, y, snake_block, snake_block])

def show_score(score):
    value = font.render("Score: " + str(score), True, WHITE)
    screen.blit(value, [0, 0])

# Main game loop
running = True
while running:
    screen.fill(BLACK)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                snake_direction = "LEFT"
            elif event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                snake_direction = "RIGHT"
            elif event.key == pygame.K_UP and snake_direction != "DOWN":
                snake_direction = "UP"
            elif event.key == pygame.K_DOWN and snake_direction != "UP":
                snake_direction = "DOWN"
    
    # Move snake
    head_x, head_y = snake_list[-1]
    if snake_direction == "LEFT":
        head_x -= snake_block
    elif snake_direction == "RIGHT":
        head_x += snake_block
    elif snake_direction == "UP":
        head_y -= snake_block
    elif snake_direction == "DOWN":
        head_y += snake_block
    
    # Add new head
    snake_list.append([head_x, head_y])
    
    # Check if snake eats food
    if head_x == food_x and head_y == food_y:
        score += 1
        food_x = round(random.randrange(0, WIDTH - snake_block) / 20) * 20
        food_y = round(random.randrange(0, HEIGHT - snake_block) / 20) * 20
    else:
        # Remove last part of snake if not eaten
        snake_list.pop(0)
    
    # Draw food
    pygame.draw.rect(screen, RED, [food_x, food_y, snake_block, snake_block])
    
    # Draw snake
    draw_snake(snake_list)
    
    # Show score
    show_score(score)
    
    # Check collisions with walls
    if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
        running = False
    
    # Check collisions with self
    for block in snake_list[:-1]:
        if block == [head_x, head_y]:
            running = False
    
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
print("Game Over! Your score:", score)