import pygame, random
from sys import exit

pygame.init()
pygame.display.set_caption("opyluj květinu")

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
SCREEN = pygame.display.set_mode((600, 600))

FPS = 60 #kolik framu za sekundu
MOVEMENT = 3
VELOCITY = 1

BEE_WIDTH, BEE_HEIGHT = 50, 50
BEE = pygame.image.load("bee.png")
BEE = pygame.transform.scale(BEE, (BEE_WIDTH, BEE_HEIGHT))
bee_direction = "RIGHT"
new_direction = bee_direction
FLOWER_WIDTH, FLOWER_HEIGHT = 50, 50


def bee_move(bee_direction, new_direction):
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and bee_direction != "DOWN":
                new_direction = "UP"
            elif event.key == pygame.K_DOWN and bee_direction != "UP":
                new_direction = "DOWN"
            elif event.key == pygame.K_LEFT and bee_direction != "RIGHT":
                new_direction = "LEFT"
            elif event.key == pygame.K_RIGHT and bee_direction != "LEFT":
                new_direction = "RIGHT"
     new_direction = bee_direction


def grafics(yellow):
    SCREEN.fill("powderblue")
    SCREEN.blit(BEE, (yellow.x, yellow.y))
    pygame.display.update()

     
def main():
    yellow = pygame.Rect(100, 150, BEE_WIDTH, BEE_HEIGHT)#yellow.x position, y position, width, height

    clock = pygame.time.Clock()
    running = True

    

    while running:
         clock.tick(FPS)

         for event in pygame.event.get():
            if event.type == pygame.QUIT: #pokud se stane event quit ukonči hru
                running = False
                pygame.quit()

         keys_pressed = pygame.key.get_pressed()       
         bee_move(bee_direction, new_direction) 
         grafics(yellow)
        
    pygame.quit()

if __name__ == "__main__":
    main()