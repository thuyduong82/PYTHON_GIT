import pygame 
from sys import exit

pygame.init() 

pygame.display.set_caption("penguin hunt")

screen_height = 600
screen_width = 800

screen = pygame.display.set_mode((screen_width, screen_height)) #rozliseni
clock = pygame.time.Clock()

running = True #nekonecný cyklus 

player_path = ("penguin.png")
enemy_path = ("fox.png")

# player = pygame.Rect((50, 100, 50, 50))#vytvoření hráče -> hráč je obdélník x,y,šířka,výška , dvojite zavorky protoze jsme vlozili jednodušší a rychlejší list
player_surf = pygame.image.load(player_path).convert_alpha()#aplha pruhledny pozadí
player_surf = pygame.transform.rotozoom(player_surf, 0, 2)
player_x = 200
player_y = 150
player_rect = player_surf.get_rect(midbottom=(player_x, player_y))
player_speed = 5
player_lives = 3


enemy_run1 = pygame.image.load("fox.png").convert_alpha()
enemy_run2 = pygame.image.load("fox.png").convert_alpha()
enemy_index = 0
enemy_surf = enemy_run_all[enemy_index]
enemy_run_all = [enemy_run1, enemy_run2]
enemy_surf = pygame.image.load(enemy_path).convert_alpha()
enemy_surf = pygame.transform.rotozoom(enemy_surf,0, 2)#koho, rotovani , velikost-scale
enemy_x = screen_width - 20
enemy_y = 300
enemy_speed = 5
enemy_rect = enemy_surf.get_rect(midbottom=(enemy_x, enemy_y))

elapsed_time = 0

font = pygame.font.SysFont('algerian', 25)

invulnerability = 0

def penguin_move(key ,player_rect):
    if key[pygame.K_w]:
        player_rect.top -= player_speed
    if key[pygame.K_a]:
        player_rect.left -= player_speed
    if key[pygame.K_s]:
        player_rect.bottom += player_speed
    if key[pygame.K_d]:
        player_rect.right += player_speed



while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #kontroluje vypínání hry
            running = False
            exit()
    
    key = pygame.key.get_pressed()
    penguin_move(key, player_rect)


    # if key[pygame.K_RIGHT]:
    #     player.move_ip(2, 0)#pohybame player díky funkci move_ip a v zavorce o kolik pohybuje x,y
    # if key[pygame.K_LEFT]:
    #     player.move_ip(-2, 0)
    # if key[pygame.K_UP]:
    #     player.move_ip(0, -2)
    # if key[pygame.K_DOWN]:
    #     player.move_ip(0, 2)


  
    screen.fill("powderblue")

    text_lives = font.render(f"Lives", False, "pink")
    text_lives = font.render("Health: " + str(player_lives), 1, "#ff00ff")
    screen.blit(text_lives , (50, 50))

    # pygame.draw.rect(screen, ("pink"), player )#povrch, barva, value jakyý rectangle chceme vykreslit

    screen.blit(player_surf, ((player_rect)))#dát na screen player_surf(tucnáka)a souřadnice, kde se spawne
    screen.blit(enemy_surf, ((enemy_x, enemy_y)))#blit jako vyblit neco na screen
    enemy_x -= enemy_speed

    elapsed_time += clock.get_time()
    if elapsed_time > 2000:
        invulnerability == False


    if player_rect.colliderect(enemy_rect):
        if not invulnerability:
            player_lives -= 1
            invulnerability = True
            elapsed_time = 0
        
    if player_lives == 0:
        exit()

    pygame.display.update()
    #pygame.display.flip() alernstivní funkce .update

    clock.tick(60) #omezi to maximálně na 60 framů
