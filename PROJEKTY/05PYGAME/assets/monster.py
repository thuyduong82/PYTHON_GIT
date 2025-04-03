import pygame
from utility import image_cutter
from player import Player
from settings import *

class Monster(Player):
    def __init__(self, type, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.spritesheet = pygame.image.load("assets\characters\monsters\monster_spritesheet.png").convert_alpha()  
        self.type = type
        self.image = image_cutter(self.spritesheet, 0, self.type, 15, 16, 3)
        self.rect = self.image.get_rect(midbottom=(self.x, self.y))
        self.index = 0
        self.speed = 7
        self.frame_count = 3
        self.direction = "left"
        
    
    def update(self):

        if self.rect.x < 0:
            self.direction = "right"
        elif self.rect.x > screen_width:
            self.direction = "left"

        if self.direction == "right":
            self.rect.x += self.speed
        elif self.direction == "left":
            self.rect.x -= self.speed
        
        self.animation(self.type)
        

    def animation(self, row):

        self.index += 0.1
        if self.index >= self.frame_count:
            self.index = 0
        
        self.image = image_cutter(self.spritesheet, int(self.index), row, 15, 16, 3) #



