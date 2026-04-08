import pygame
import sys

pygame.init()

width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("oapkovani")

WHITE= (255, 255, 255)
BLUE = (153, 217, 234)

size = 50
x, y = 50, 50
player_rect = pygame.Rect(x,y,size,size)
player_surf = pygame.Surface((size,size))
player_surf.fill(BLUE)
speed = 5

clock = pygame.time.Clock()

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += speed
    if keys[pygame.K_UP]:
        player_rect.y -= speed
    if keys[pygame.K_DOWN]:
        player_rect.y += speed

    # Vykreslení čtverečku
    #pygame.draw.rect(screen, BLUE, (x, y, size, size)) 
    screen.blit(player_surf, player_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()