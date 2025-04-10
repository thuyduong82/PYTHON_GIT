import pygame
from utility import image_cutter
from settings import *


class Player(pygame.sprite.Sprite): #nazvy class= velke pismeno (napr Player)
    def __init__(self):
        super().__init__()
        self.x = 150
        self.y = 150
        self.spritesheet = pygame.image.load("assets/characters/player/man_brownhair_run.png").convert_alpha()  
        self.image = image_cutter(self.spritesheet, 0, 0, 15, 16, 3)
        self.rect = self.image.get_rect(midbottom=(self.x, self.y))
        self.index = 0
        self.speed = 10
        self.lives = 3
        self.invulnerability = False
        self.elapsed_time = 0
        
    def draw_lives(self, font, screen):
        zivoty = font.render(f"Health: " + (self.lives), False, white)
        screen.blit(zivoty, ( screen_width - 100, 10))#get_width odečíta velikost textu, -10,10 na ose y a x

    
    def animation(self, direction):
        frame_count = 3

        self.index += 0.1
        if self.index >= frame_count:
            self.index = 0
        
        self.image = image_cutter(self.spritesheet, int(self.index), direction, 15, 16, 3)

    def update(self, monster_group, clock):
        key = pygame.key.get_pressed()

        # pokud je stisknutá klávesa w, pohni hráčem o (x, y)
        if key[pygame.K_w]:
            self.animation(1)
            self.rect.top -= self.speed
        if key[pygame.K_a]:
            self.animation(2)
            self.rect.left -= self.speed
        if key[pygame.K_s]:
            self.animation(0)
            self.rect.bottom += self.speed
        if key[pygame.K_d]:
            self.animation(3)
            self.rect.right += self.speed

        self.monster_group = monster_group

        if self.elapsed_time > 2000:
        # vypni nesmrtelnost
            self.invulnerability = False

        self.elapsed_time += clock.get_time()

        if pygame.sprite.spritecollide(self, monster_group, True):
            if not self.invulnerability:
                self.lives -= 1
                self.invulnerability = True # zapni nesmrtelnost
                self.elapsed_time = 0

            print("minus")


            print("cau")#kdo koliduje, s kým

