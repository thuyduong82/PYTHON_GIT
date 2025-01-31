import pygame
import os

print(os.getcwd())

pygame.display.set_caption("první hra")

WIDTH, HEIGHT = 900, 500 #velikost obrazovky
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CREAM_COL = (242, 219, 163)
BLACK = (0, 0, 0)
PINK = (232, 0, 156)
YELLOW = (232, 224, 10)

BORDER = pygame.Rect(WIDTH//2 - 7.5 , 0, 15, HEIGHT)

# HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
# WINNER_FONT = pygame.font.SysFont('comicsans', 100)

FPS = 60 #kolik framu za sekundu
MOVEMENT = 5

BUL_WIDTH = 10
BUL_HEIGHT = 5
BULLET_MOVEMENT = 7
MAX_BULLET = 3

YELLOW_HIT = pygame.USEREVENT + 1 #1==unique id eventu,yellow a pink nemuzou mit stejne cislo
PINK_HIT = pygame.USEREVENT + 2 #nejakej event

#r ->rawstring dělá, aby to bral "\" jako obyč znak(v pythonu je "\" escape backlash ) 
#nebo můžeme "\" zdvojit viz. \\
#nebo místo "\" použít "/"
JELLY_PATH = (r"C:\Users\nqthu\Downloads\PYTHON (1)\game.penguin\PROJEKTY\03CANDY\jelly_left.png")
TEDDY_PATH = ("C:/Users/nqthu/Downloads/PYTHON (1)/game.penguin/PROJEKTY/03CANDY/teddy_right.png")

#u teddy jsem použila rotate u jelly ne
JELLY_WIDTH, JELLY_HEIGHT = 80, 80
TEDDY_WIDTH, TEDDY_HEIGHT = 80, 80
TEDDY = pygame.image.load(TEDDY_PATH)
TEDDY = pygame.transform.rotate(pygame.transform.scale(TEDDY, (TEDDY_WIDTH, TEDDY_HEIGHT)), -90)#90stupnu rotace
JELLY = pygame.image.load(JELLY_PATH)
JELLY = pygame.transform.scale(JELLY, (JELLY_WIDTH, JELLY_HEIGHT))#nerotace:D


def yellow_move(keys_pressed, yellow):
        if keys_pressed[pygame.K_a] and yellow.x - MOVEMENT + 10 > 0:
             yellow.x -= MOVEMENT
        if keys_pressed[pygame.K_d] and yellow.x + MOVEMENT + TEDDY_WIDTH - 6 < BORDER.x : #musí tam být teddy_width, aby to nepřekročilo border
             yellow.x += MOVEMENT
        if keys_pressed[pygame.K_w] and yellow.y - MOVEMENT + 10 > 0:
             yellow.y -= MOVEMENT
        if keys_pressed[pygame.K_s] and yellow.y + MOVEMENT + TEDDY_HEIGHT - 5 < HEIGHT:
             yellow.y += MOVEMENT

def pink_move(keys_pressed, pink):
        if keys_pressed[pygame.K_LEFT] and pink.x - MOVEMENT - 5 > BORDER.x :#left
             pink.x -= MOVEMENT
        if keys_pressed[pygame.K_RIGHT] and pink.x + JELLY_WIDTH + MOVEMENT - 10 < WIDTH:#right -10je par pixelů, aby to bylo víc clean ale není to potřebný
             pink.x += MOVEMENT
        if keys_pressed[pygame.K_UP] and pink.y - MOVEMENT + 12 > 0: #up
             pink.y -= MOVEMENT
        if keys_pressed[pygame.K_DOWN] and pink.y + MOVEMENT + JELLY_HEIGHT - 15 < HEIGHT :#down
             pink.y += MOVEMENT

def handle_bullets(yellow_bullets, pink_bullets, yellow, pink):
     for bullet in yellow_bullets:
          bullet.x += BULLET_MOVEMENT
          if pink.colliderect(bullet):#pokud pink se setká s bullet
               pygame.event.post(pygame.event.Event(PINK_HIT))
               yellow_bullets.remove(bullet)
          elif bullet.x > WIDTH:
               yellow_bullets.remove(bullet)


     for bullet in pink_bullets:
          bullet.x -= BULLET_MOVEMENT
          if yellow.colliderect(bullet):#pokud pink se setká s bullet
               pygame.event.post(pygame.event.Event(YELLOW_HIT))
               pink_bullets.remove(bullet)    
          elif bullet.x < 0:
               pink_bullets.remove(bullet) 
#díky tomuhle je to actually vidět

def grafics(pink, yellow, pink_bullets, yellow_bullets ):#aby funkce znala proměné pink yellow
        SCREEN.fill(CREAM_COL)#barva pozadí
        pygame.draw.rect(SCREEN, BLACK, BORDER)#kam kreslíme, barvu a co kreslíme
        SCREEN.blit(JELLY, (pink.x, pink.y))#jelly zastupuje pink rectangle->proto x==700 y==300
        SCREEN.blit(TEDDY, (yellow.x, yellow.y))

        for bullet in pink_bullets:
             pygame.draw.rect(SCREEN, PINK, bullet)
        for bullet in yellow_bullets:
             pygame.draw.rect(SCREEN, YELLOW, bullet)

        pygame.display.update()#musime updatenout, aby se to cream col ukázala




def main():
    pink = pygame.Rect(700, 300, JELLY_WIDTH, JELLY_HEIGHT)#
    yellow = pygame.Rect(100, 300, TEDDY_WIDTH, TEDDY_HEIGHT)#pink.x position, y position, width, height

    pink_bullets = []
    yellow_bullets = []

    clock = pygame.time.Clock()
    
    running = True #nekonečný cyklus
    while running:
        clock.tick(FPS) #rychlost loopu, nikdy nepřekročíme 60 framu za sekundu
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #pokud se stane event quit ukonči hru
                running = False

            if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLET:#leftcontol
                      bullet = pygame.Rect(
                           yellow.x + TEDDY_WIDTH - 6, yellow.y + TEDDY_HEIGHT//2 - 2.5, BUL_WIDTH,BUL_HEIGHT)#/2 vystřelí zprostředka výšky teddy,-2.5->pol výškybullet,
                      yellow_bullets.append(bullet)    

                 if event.key == pygame.K_RCTRL and len(pink_bullets) < MAX_BULLET:#nestrilej dalsi bullets pokud na screen už je maximalni pocet bullets
                      bullet = pygame.Rect(
                           pink.x, pink.y + JELLY_HEIGHT//2 , BUL_WIDTH, BUL_HEIGHT)
                      pink_bullets.append(bullet)
          
        keys_pressed = pygame.key.get_pressed()
        yellow_move(keys_pressed, yellow)
        pink_move(keys_pressed, pink)
        
        handle_bullets(yellow_bullets, pink_bullets, yellow, pink)
    
        grafics(pink, yellow, pink_bullets, yellow_bullets)
    
    pygame.quit()

#spoštíme hlavní funkci
if __name__ == "__main__":
    main()
