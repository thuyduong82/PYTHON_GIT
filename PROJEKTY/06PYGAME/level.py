import pygame
import json
from game_objects import GameObject

class Level:
    def __init__(self, screen, background, level_data, sprite_groups):
        self.screen = screen
        self.background = background
        self.level_data = level_data
        self.sprite_groups = sprite_groups

        for group_name, group in self.sprite_groups.items():
            self.create_object(group_name, group)

    def draw_objects(self):
        for group in self.sprite_groups.values():
            group.draw(self.screen)
    
    def create_object(self, object_type, group):
        with open(self.level_data, mode="r") as file:
            data = json.load(file)
        
        for entity in data["entities"][object_type]:
            x = entity["x"]
            y = entity["y"]
            w = entity["width"]
            h = entity["height"]
            game_object = GameObject(x, y, w, h)
            group.add(game_object)
   
