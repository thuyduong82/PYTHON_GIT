import pygame
import random
import sys

pygame.init()

# velikost okna
WIDTH, HEIGHT = 400, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chytej míčky")

# barvy
WHITE = (255,255,255)
RED = (230,50,50)
BLUE = (50,50,200)
BLACK = (0,0,0)

# hráč
paddle_width = 110
paddle_height = 16
paddle_x = WIDTH//2 - paddle_width//2
paddle_y = HEIGHT - 50
paddle_speed = 13

# míčky
ball_radius = 15
ball_count = 2
MIN_SPACING_Y = 400  # větší rozestup na ose Y

base_speeds = [4.0, 4.6]  # každý míček trochu jinak rychlý

def rand_x():
    return random.randint(ball_radius, WIDTH - ball_radius)

def best_spaced_y(existing_y):
    # spawn vysoko nad obrazovkou
    if not existing_y:
        return -random.randint(400, 1000)
    best_y = None
    best_score = -1
    for _ in range(300):
        candidate = -random.randint(400, 1000)
        distances = [abs(candidate - y) for y in existing_y]
        min_dist = min(distances)
        score = min_dist + (10000 if min_dist >= MIN_SPACING_Y else 0)
        if score > best_score:
            best_score = score
            best_y = candidate
    return best_y

# inicializace
balls = []
speeds = []
ys = []
for i in range(ball_count):
    x = rand_x()
    y = best_spaced_y(ys)
    balls.append([x, y])
    speeds.append(base_speeds[i % len(base_speeds)])
    ys.append(y)

score = 0
caught = 0
missed = 0
game_over = False

font = pygame.font.Font(None, 36)
big_font = pygame.font.Font(None, 64)
clock = pygame.time.Clock()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if game_over:
        screen.fill(WHITE)
        go = big_font.render("KONEC HRY", True, BLACK)
        info = font.render(f"Skóre: {score}   Propadlo: {missed}/5", True, BLACK)
        screen.blit(go, (WIDTH//2 - go.get_width()//2, HEIGHT//2 - 60))
        screen.blit(info, (WIDTH//2 - info.get_width()//2, HEIGHT//2 + 10))
        pygame.display.flip()
        clock.tick(60)
        continue

    # pohyb hráče
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - paddle_width:
        paddle_x += paddle_speed

    current_ys = [b[1] for b in balls]

    for i in range(len(balls)):
        balls[i][1] += speeds[i]

        # propadne dolů
        if balls[i][1] > HEIGHT:
            tmp_ys = current_ys[:]; tmp_ys.pop(i)
            balls[i][0] = rand_x()
            balls[i][1] = best_spaced_y(tmp_ys)
            score -= 1
            missed += 1
            if missed >= 5:
                game_over = True

        # kolize s plošinkou
        if (paddle_y < balls[i][1] + ball_radius < paddle_y + paddle_height and
            paddle_x < balls[i][0] < paddle_x + paddle_width):
            score += 1
            caught += 1
            if caught % 1 == 0:#kdyz se chytne jeden míček
                for j in range(len(speeds)):
                    speeds[j] += 0.5  # zrychlení každé 2 chycené
            tmp_ys = current_ys[:]; tmp_ys.pop(i)
            balls[i][0] = rand_x()
            balls[i][1] = best_spaced_y(tmp_ys)

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (paddle_x, paddle_y, paddle_width, paddle_height))
    for b in balls:
        pygame.draw.circle(screen, RED, (b[0], b[1]), ball_radius)

    hud = font.render(f"Skóre: {score}   Propadlo: {missed}/5", True, BLACK)
    screen.blit(hud, (10, 10))

    pygame.display.flip()
    clock.tick(60)
