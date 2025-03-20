import pygame
from utility import image_cutter

class Player(pygame.sprite.Sprite): #nazvy class= velke pismeno (napr Player)
    def __init__(self):
        self.x = 150
        self.y = 150
        self.spritesheet = pygame.image.load("assets/characters/player/man_brownhair_run.png").convert_alpha()  
        self.img = image_cutter(self.spritesheet, 0, 0, 15, 16, 3)
        self.rect = self.img.get_rect(midbottom=(self.x, self.y))
        self.index = 0
        self.speed = 10
        self.lives = 3
        self.invulnerability = False
    
    def animation(self, direction):
        frame_count = 3

        self.index += 0.1
        if self.index >= frame_count:
            self.index = 0
        
        self.img = image_cutter(self.spritesheet, int(self.index), direction, 15, 16, 3)