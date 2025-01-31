import pygame
import os

pygame.display.set_caption("první hra")

assets_path = "/game.penguin/PROJEKTY/ASSETS/jelly_left.png"

WIDTH, HEIGHT = 900, 500 #velikost obrazovky
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CREAM_COL = (242, 219, 163)
FPS = 60 #kolik framu za sekundu
JELLY_WIDTH, JELLY_HEIGHT = 80, 80
TEDDY_WIDTH, TEDDY_HEIGHT = 80, 80


JELLY = pygame.image.load(os.path.join(assets_path))
JELLY = pygame.transform.scale(JELLY, (JELLY_WIDTH, JELLY_HEIGHT))
TEDDY = pygame.image.load("teddy_right.pgn")
TEDDY = pygame.transform.scale(TEDDY, (TEDDY_WIDTH, TEDDY_HEIGHT))



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
