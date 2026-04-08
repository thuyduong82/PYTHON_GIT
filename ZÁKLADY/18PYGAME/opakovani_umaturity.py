import pygame
import sys

pygame.init()

width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("oapkovani")

WHITE = (255, 255, 255)
BLUE = (153, 217, 234)
RED = (255, 0, 0)

size = 50
x, y = 100, 100
player_rect = pygame.Rect(x, y, size, size)
enemy_rect = pygame.Rect(300,400,size,size)
#player_img = pygame.Surface((size, size))
#player_img.fill(BLUE)


player_img= pygame.image.load("player.png").convert_alpha()
player_img= pygame.transform.scale(player_img,(50,50))
player_rect = player_img.get_rect(center = (x,y))

enemy_img = pygame.image.load("enemy.png").convert_alpha()
enemy_img= pygame.transform.scale(enemy_img,(50,50))
enemy_rect = enemy_img.get_rect(center=(250,200))

enemy_speed=2
enemy_dir=1
speed = 5
clock = pygame.time.Clock()

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    old_rect = player_rect.copy()

    if keys[pygame.K_LEFT]:
        player_rect.x -= speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += speed
    if keys[pygame.K_UP]:
        player_rect.y -= speed
    if keys[pygame.K_DOWN]:
        player_rect.y += speed

    if enemy_rect:
        enemy_rect.y += enemy_speed * enemy_dir

        if enemy_rect.top <= 0:#kdyz je top enemy mensi jak nula jede dolu
            enemy_dir = 1
        if enemy_rect.bottom >= height:#kdyz se dotkne dolejsku jede nahoru
            enemy_dir = -1

    # kolize
    if enemy_rect and player_rect.colliderect(enemy_rect):
        enemy_rect = None
        print("au to bolelo!")  

    screen.blit(player_img, player_rect)
    #creen.blit(enemy_img, enemy_rect)
    if enemy_rect:
        screen.blit(enemy_img, enemy_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()