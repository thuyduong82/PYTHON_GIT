import pygame
import random

# Inicializace Pygame
pygame.init()

# Nastavení obrazovky
ŠÍŘKA, VÝŠKA = 600, 400
obrazovka = pygame.display.set_mode((ŠÍŘKA, VÝŠKA))
pygame.display.set_caption("Jednoduchý Had")

# Barvy
BÍLÁ = (255, 255, 255)
ZELENÁ = (0, 200, 0)
ČERVENÁ = (200, 0, 0)

# Nastavení hada
velikost_hada = 10
pozice_hlavy = [300, 200]  # Počáteční pozice hlavy hada
tělo_hada = [[300, 200], [290, 200], [280, 200]]  # Had má pevnou délku
rychlost = 10  # Rychlost pohybu
směr = "DOPRAVA"  # Počáteční směr
další_směr = směr  # Paměť pro otočení

# Nastavení jídla
pozice_jídla = [random.randint(10, ŠÍŘKA - 10), random.randint(10, VÝŠKA - 10)]
velikost_jídla = 8

hodiny = pygame.time.Clock()
running = True

while running:
    obrazovka.fill(BÍLÁ)

    # Ovládání (klávesnice)
    for událost in pygame.event.get():
        if událost.type == pygame.QUIT:
            running = False
        elif událost.type == pygame.KEYDOWN:
            if událost.key == pygame.K_UP and směr != "DOLŮ":
                další_směr = "NAHORU"
            elif událost.key == pygame.K_DOWN and směr != "NAHORU":
                další_směr = "DOLŮ"
            elif událost.key == pygame.K_LEFT and směr != "DOPRAVA":
                další_směr = "DOLEVA"
            elif událost.key == pygame.K_RIGHT and směr != "DOLEVA":
                další_směr = "DOPRAVA"

    # Aktualizace směru
    směr = další_směr

    # Pohyb hada
    if směr == "NAHORU":
        pozice_hlavy[1] -= rychlost
    elif směr == "DOLŮ":
        pozice_hlavy[1] += rychlost
    elif směr == "DOLEVA":
        pozice_hlavy[0] -= rychlost
    elif směr == "DOPRAVA":
        pozice_hlavy[0] += rychlost

    # Přidání nové hlavy a zachování délky hada
    tělo_hada.insert(0, list(pozice_hlavy))
    tělo_hada = tělo_hada[:3]  # Had má stále stejnou délku

    # Kontrola, zda had snědl jídlo
    if abs(pozice_hlavy[0] - pozice_jídla[0]) < 10 and abs(pozice_hlavy[1] - pozice_jídla[1]) < 10:
        pozice_jídla = [random.randint(10, ŠÍŘKA - 10), random.randint(10, VÝŠKA - 10)]  # Přesunutí jídla

    # Kontrola kolize se sebou samým
    if pozice_hlavy in tělo_hada[1:]:
        běží = False  # Konec hry

    # Kontrola nárazu do stěn
    if pozice_hlavy[0] < 0 or pozice_hlavy[0] > ŠÍŘKA or pozice_hlavy[1] < 0 or pozice_hlavy[1] > VÝŠKA:
        běží = False  # Konec hry

    # Kreslení jídla
    pygame.draw.circle(obrazovka, ČERVENÁ, pozice_jídla, velikost_jídla)

    # Kreslení hada
    for část in tělo_hada:
        pygame.draw.rect(obrazovka, ZELENÁ, (*část, velikost_hada, velikost_hada))

    pygame.display.flip()
    hodiny.tick(15)  # Rychlost hry

pygame.quit()
