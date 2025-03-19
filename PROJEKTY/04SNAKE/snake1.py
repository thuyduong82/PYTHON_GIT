import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
SQUARE_SIZE = 20
SPEED = 10
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Snake Game")

# Initialize game variables
x, y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
food_x, food_y = random.randint(0, (SCREEN_WIDTH - SQUARE_SIZE) // SQUARE_SIZE) * SQUARE_SIZE, random.randint(0, (HEIGHT - SQUARE_SIZE) // SQUARE_SIZE) * SQUARE_SIZE
dx, dy = 0, 0
score = 0
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    screen.fill(WHITE)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and dx == 0:
                dx, dy = -SQUARE_SIZE, 0
            elif event.key == pygame.K_RIGHT and dx == 0:
                dx, dy = SQUARE_SIZE, 0
            elif event.key == pygame.K_UP and dy == 0:
                dx, dy = 0, -SQUARE_SIZE
            elif event.key == pygame.K_DOWN and dy == 0:
                dx, dy = 0, SQUARE_SIZE
    
    # Move square
    x += dx
    y += dy
    
    # Wrap around the screen
    x %= WIDTH
    y %= HEIGHT
    
    # Check collision with food
    if abs(x - food_x) < SQUARE_SIZE and abs(y - food_y) < SQUARE_SIZE:
        score += 1
        food_x = random.randint(0, (WIDTH - SQUARE_SIZE) // SQUARE_SIZE) * SQUARE_SIZE
        food_y = random.randint(0, (HEIGHT - SQUARE_SIZE) // SQUARE_SIZE) * SQUARE_SIZE
    
    # Draw square
    pygame.draw.rect(screen, GREEN, (x, y, SQUARE_SIZE, SQUARE_SIZE))
    
    # Draw food
    pygame.draw.rect(screen, RED, (food_x, food_y, SQUARE_SIZE, SQUARE_SIZE))
    
    # Update display
    pygame.display.flip()
    clock.tick(SPEED)

pygame.quit()
