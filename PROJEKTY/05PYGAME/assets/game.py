
import pygame
from sys import exit
from settings import *
from utility import image_cutter
from player import Player
from monster import *

pygame.init()


screen = pygame.display.set_mode((screen_width, screen_height))

# vytvoř hodiny
clock = pygame.time.Clock()

running = True

font = pygame.font.Font("assets/fonts/PixelifySans-Regular.ttf", 25)

monsters = pygame.sprite.Group()
monsters.add(Monster(1, 200, 500),Monster (2, 300, 200),Monster (3, 400, 300),Monster (4, 500, 400))
#type, x , y
player = pygame.sprite.GroupSingle()
player.add(Player())

background = pygame.image.load("background.png")
screen.blit

# # Počáteční hodnota časomíry
elapsed_time = 0

while running:
    # kontroluje nám události, které se dějí v naší hře
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()
    
    # proměnná key, pod ní schováme stisknutou klávesu
  
  
    # obarví obrazovku na bílo
    screen.blit(background, (0,0))


    player.draw(screen)
    player.update(monsters, clock)
    player.sprite.draw_lives(font, screen)
    
    monsters.draw(screen)
    monsters.update()




    # na obrazovku vykresli - surface na rectangle (recntagle má souřadnice, viz výše)
    # screen.blit(player_img, player_rect)

    # monstrum se pohybuje zprava doleva
 
    # zde spouštíme animaci

    # zapni časomíru - pod proměnnou přidávej čas
    elapsed_time += clock.get_time()


    

    # pokud nastane kolize mezi hráčem a monstrem
    # if player_rect.colliderect(monster_rect):
    #     # pokud hráč není nesmrtelný - alternativa zápisu if invulnerability == False
    #     if not invulnerability:
    #         player_lives -= 1 # odeber život
    #         invulnerability = True # zapni nesmrtelnost
    #         elapsed_time = 0 # vynuluj časomíru

    # pokud uběhly 2 sekundy




    # updatuje vše
    pygame.display.update()
    # pygame.display.flip() - alternativní funkce k .update

    # omez tickrate (rychlost hry) na 60fps, ať je to konzistentní napříč zařízeními
    clock.tick(60)