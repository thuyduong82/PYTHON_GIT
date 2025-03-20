# Program momentálně není funkční, v příští hodině dokončíme přesouvání kódu a hru opět zprovozníme

import pygame
from sys import exit
from settings import *
from utility import image_cutter
from player import Player

# inicializuje hru - spustíme pygame
pygame.init()

# vytvoření animace monstra
def monster_animation():
    # importujeme globální proměnné, které jsme si pro monstrum vytvořili
    global monster_surf, monster_index, monster_run_all

    # animace zjednodušeně - máme list (seznam), ve kterém jsou obrázky v různé fázi pohybu
    # vykreslujeme vždy jeden z obrázků z listu
    # posouváním indexu zvolíme, který obrázek se vykresluje
    monster_index += 0.1 # index měníme pouze o 0.1, aby animace byla pomalejší

    # pokud je index větší, než množství obrázků v listu, vyresetujeme index
    if monster_index > len(monster_run_all):
        monster_index = 0
    
    # surface blitujeme v herní smyčce na obrozovku
    # zde zvolíme, co bude surface, aneb co budeme vykreslovat na obrozovku
    # Pozn.: jelikož měníme index o destinná čísla výše, 
    # je potřeba jej zaokrouhlit zpět na celé číslo pomocí funkce int(), která vždy zaokrouhluje dolu
    monster_surf = monster_run_all[int(monster_index)] 

# funkce na animování hráče, přijímá parametr direction, čímž měníme řadu, ze které vyřezáváme, viz funkce image_cutter
# v našem spritesheetu řada udává směr animace panáčka
# zbytek funkce je podobný funkci animování monstra, s výjimkou, že musíme manuálně napsat, kolik máme framů (nelze to odvodit z velikosti listu, jako to bylo výše)

    

# vytvoříme obraz
screen = pygame.display.set_mode((screen_width, screen_height))

# vytvoř hodiny
clock = pygame.time.Clock()

running = True


# Vytvoření fontu k vykreslení životů - pokud nechcete vlastní font, použijte None (bez uvozovek) místo názvu fontu
font = pygame.font.Font("assets/fonts/PixelifySans-Regular.ttf", 25)


# vytvoření monstra
monster_run1 = pygame.image.load("assets/characters/monsters/monstrum.png").convert_alpha()
monster_run2 = pygame.image.load("assets/characters/monsters/monstrum_run.png").convert_alpha()
monster_run_all = [monster_run1, monster_run2] 
# monster_surf = pygame.transform.rotozoom(monster_surf, 0, 5)
monster_index = 0
monster_surf = monster_run_all[monster_index]

monster_x = screen_width - 100
monster_y = 300
monster_rect = monster_surf.get_rect(midbottom=(monster_x, monster_y))
monster_speed = 1



# Počáteční hodnota časomíry
elapsed_time = 0

# herní smyčka
while running:
    # kontroluje nám události, které se dějí v naší hře
    for event in pygame.event.get():
        # pokud dojde k události vypnout, vypne
        if event.type == pygame.QUIT:
            running = False
            exit()
    
    # proměnná key, pod ní schováme stisknutou klávesu
  
  
    # obarví obrazovku na bílo
    screen.fill("white")

    # render fontu
    # text_lives = font.render(f"Lives: {player_lives}", False, "#000000") 
    # vykreslení textu na obrazovku
    # screen.blit(text_lives, (screen_width-100, 10))

    # na obrazovku vykresli - surface na rectangle (recntagle má souřadnice, viz výše)
    # screen.blit(player_img, player_rect)

    # monstrum se pohybuje zprava doleva
    monster_rect.left -= monster_speed
    # zde spouštíme animaci
    monster_animation()
    screen.blit(monster_surf, monster_rect)

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
    if elapsed_time > 2000:
        # vypni nesmrtelnost
        invulnerability = False



    # updatuje vše
    pygame.display.update()
    # pygame.display.flip() - alternativní funkce k .update

    # omez tickrate (rychlost hry) na 60fps, ať je to konzistentní napříč zařízeními
    clock.tick(60)