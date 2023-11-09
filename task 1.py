import pygame
import random

pygame.init()

# Constants
SCREEN_SIZE = 400
CELL_SIZE = 20
SNAKE_SIZE = 20
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Initialize game window
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption('Snake Game')

# Initialize snake and food positions
snake = [(200, 200)]
snake_direction = 'RIGHT'
food_pos = (random.randrange(1, SCREEN_SIZE // CELL_SIZE) * CELL_SIZE,
            random.randrange(1, SCREEN_SIZE // CELL_SIZE) * CELL_SIZE)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # Check for arrow key presses to change snake direction
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and snake_direction != 'DOWN':
            snake_direction = 'UP'
        elif keys[pygame.K_DOWN] and snake_direction != 'UP':
            snake_direction = 'DOWN'
        elif keys[pygame.K_LEFT] and snake_direction != 'RIGHT':
            snake_direction = 'LEFT'
        elif keys[pygame.K_RIGHT] and snake_direction != 'LEFT':
            snake_direction = 'RIGHT'

    # Move the snake in the current direction
    x, y = snake[0]
    if snake_direction == 'UP':
        y -= CELL_SIZE
    elif snake_direction == 'DOWN':
        y += CELL_SIZE
    elif snake_direction == 'LEFT':
        x -= CELL_SIZE
    elif snake_direction == 'RIGHT':
        x += CELL_SIZE

    # Check for collisions with food
    if (x, y) == food_pos:
        snake.append((0, 0))  # Add a new segment to the snake
        food_pos = (random.randrange(1, SCREEN_SIZE // CELL_SIZE) * CELL_SIZE,
                    random.randrange(1, SCREEN_SIZE // CELL_SIZE) * CELL_SIZE)

    # Update snake body positions
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = snake[i - 1]

    # Update snake head position
    snake[0] = (x, y)

    # Check for collisions with screen edges or itself
    if x < 0 or x >= SCREEN_SIZE or y < 0 or y >= SCREEN_SIZE or (x, y) in snake[1:]:
        pygame.quit()
        quit()

    # Draw everything on the screen
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (food_pos[0], food_pos[1], CELL_SIZE, CELL_SIZE))

    for segment in snake:
        pygame.draw.rect(screen, RED, (segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))

    pygame.display.update()

    # Limit frames per second
    pygame.time.Clock().tick(10)
import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
SNAKE_SIZE = 20
SNAKE_SPEED = 15
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Initialize the snake
snake = [(100, 50)]
snake_dir = (1, 0)
food = (random.randrange(1, WIDTH // SNAKE_SIZE) * SNAKE_SIZE,
        random.randrange(1, HEIGHT // SNAKE_SIZE) * SNAKE_SIZE)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
 
