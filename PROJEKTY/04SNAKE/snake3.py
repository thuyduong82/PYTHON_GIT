import pygame, random #random na jidlo

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 500, 300
GRID_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake setup
snake = [(100, 100), (80, 100), (60, 100)]
snake_dir = (GRID_SIZE, 0)
food = (random.randrange(0, WIDTH, GRID_SIZE), random.randrange(0, HEIGHT, GRID_SIZE))

clock = pygame.time.Clock()

running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != (0, GRID_SIZE):
                snake_dir = (0, -GRID_SIZE)
            elif event.key == pygame.K_DOWN and snake_dir != (0, -GRID_SIZE):
                snake_dir = (0, GRID_SIZE)
            elif event.key == pygame.K_LEFT and snake_dir != (GRID_SIZE, 0):
                snake_dir = (-GRID_SIZE, 0)
            elif event.key == pygame.K_RIGHT and snake_dir != (-GRID_SIZE, 0):
                snake_dir = (GRID_SIZE, 0)

    # Move the snake
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    if new_head == food:  # Eat food
        food = (random.randrange(0, WIDTH, GRID_SIZE), random.randrange(0, HEIGHT, GRID_SIZE))
    else:
        snake.pop()  # Remove tail if no food eaten

    # Check for collisions
    if (
        new_head in snake  # Collision with itself
        or new_head[0] < 0 or new_head[0] >= WIDTH  # Wall collision
        or new_head[1] < 0 or new_head[1] >= HEIGHT
    ):
        running = False  # Game over

    snake.insert(0, new_head)

    # Draw food and snake
    pygame.draw.rect(screen, RED, (*food, GRID_SIZE, GRID_SIZE))
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, GRID_SIZE, GRID_SIZE))

    pygame.display.flip()
    clock.tick(10)  # Control game speed

pygame.quit()
