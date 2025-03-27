import pygame
from utility import image_cutter
from player import Player
from settings import *

class Monster(Player):
    def __init__(self):
        super().__init__()
        self.x = screen_width - 100
        self.y = 300
        self.spritesheet = pygame.image.load("assets\characters\monsters\monster_spritesheet.png").convert_alpha()  
        self.image = image_cutter(self.spritesheet, 0, 0, 15, 16, 3)
        self.rect = self.image.get_rect(midbottom=(self.x, self.y))
        self.index = 0
        self.speed = 5
    
    def update(self, ):
        self.rect.left -= self.speed
        if self.x == screen_width:
            self.rect.right += self.speed
        
    def animation(self, direction):
        frame_count = 3

        self.index += 0.1
        if self.index >= frame_count:
            self.index = 0
        
        self.image = image_cutter(self.spritesheet, int(self.index), direction, 15, 16, 3)

    def update(self):
        self.rect.left -= self.speed
    

