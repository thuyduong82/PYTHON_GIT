import pygame
from utility import image_cutter

class Monster(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 300
        self.y = 300
        