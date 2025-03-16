import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spawn Random Rectangles")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# List to store rectangles
rectangles = []

# Main loop
running = True
while running:
    screen.fill(WHITE)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Spawn a new rectangle on spacebar press
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            rect_width = random.randint(30, 100)
            rect_height = random.randint(30, 100)
            x = random.randint(0, WIDTH - rect_width)
            y = random.randint(0, HEIGHT - rect_height)
            rectangles.append(pygame.Rect(x, y, rect_width, rect_height))
    
    # Draw rectangles
    for rect in rectangles:
        pygame.draw.rect(screen, RED, rect)
    
    pygame.display.flip()
    
pygame.quit()
