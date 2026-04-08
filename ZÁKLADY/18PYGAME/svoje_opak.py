import pygame
import sys

pygame.init()

width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("oapkovani")

WHITE = (255, 255, 255)
BLUE = (153, 217, 234)

clock = pygame.time.Clock()

class Player:
    def __init__(self, x, y, size, color, speed):
        self.rect = pygame.Rect(x, y, size, size)
        self.surf = pygame.Surface((size, size))
        self.surf.fill(color)
        self.speed = speed

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.surf, self.rect)


player = Player(50, 50, 50, BLUE, 5)

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    player.move(keys)
    player.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()