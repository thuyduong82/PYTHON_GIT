import pygame
import os

pygame.display.set_caption("první hra")

WIDTH, HEIGHT = 900, 500 #velikost obrazovky
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CREAM_COL = (242, 219, 163)
FPS = 60 #kolik framu za sekundu

JELLY = pygame.image.load("jelly_left.png")
JELLY = pygame.transform.scale(JELLY, (80, 80))
TEDDY = pygame.image.load("teddy_right.png")
TEDDY = pygame.transform.scale(TEDDY, (80, 80))



def grafics():
        SCREEN.fill(CREAM_COL)#barva pozadí
        SCREEN.blit(JELLY, (750, 250))#vyblít na screen
        SCREEN.blit(TEDDY, (150, 250))
        pygame.display.update()#musime updatenout, aby se to cream col ukázala



def main():
    clock = pygame.time.Clock()
    
    running = True #nekonečný cyklus
    while running:
        clock.tick(FPS) #rychlost loopu, nikdy nepřekročíme 60 framu za sekundu
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #pokud se stane event quit ukonči hru
                running = False
        
        grafics()
    
    pygame.quit()

#spoštíme hlavní funkci
if __name__ == "__main__":
    main()
