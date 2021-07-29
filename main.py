import pygame
import random
# import math

pygame.init()

fps = 30
clock = pygame.time.Clock()
screen_width, screen_height = 600, 800  # For the background size
player_x, player_y = 100, 100  # Players starting position
sun_scale = 20
player_velocity = 3
red = (255, 0, 0)
font = pygame.font.Font('freesansbold.ttf', 32)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('TURD TESTER')

# load image
bg_img = pygame.image.load('img/sky.png')

# scale and load images
player = pygame.transform.scale(pygame.image.load('img/guy1.png'), (30, 60))
sun = pygame.transform.scale(pygame.image.load('img/sun.png'), (sun_scale, sun_scale))


# A list to store all the suns position
suns = []
sun_x = []
sun_y = []
num_of_suns = 6


class PlayerZ:

    def __init__(self, x, y):
        pass


for i in range(num_of_suns):
    suns.append(sun)
    sun_x.append(random.randint(0, screen_width - 11))
    sun_y.append(random.randint(0, screen_height - 11))


def show_hit(x, y):
    score = font.render(" HIT ", True, (255, 255, 255))
    screen.blit(score, (x, y))


def is_collision(player_x, player_y, sun_x, sun_y):
    # distance = math.sqrt((math.pow((player_x + 20) - sun_x, 2)) + (math.pow((player_y + 20) - sun_y, 2)))

    # Conditional line to detect a sun colliding with the players body
    if player_x + 23 > sun_x and player_x + 7 < sun_x + 20:
        if player_y + 59 > sun_y and player_y + 28 < sun_y + 20:
            return True

    # Conditional line to detect a sun colliding with the players head
    if player_x + 26 > sun_x and player_x + 1 < sun_x + 20:
        if player_y + 27 > sun_y and player_y + 3 < sun_y + 20:
            return True
        else:
            return False


run = True
while run:

    # set the frames per second
    clock.tick(fps)

    # put the background and player on the screen
    screen.blit(bg_img, (0, 0))
    screen.blit(player, (player_x, player_y))
    # pygame.draw.rect(screen, red, (player_x, player_y, 30, 60), 1)

    # screen.blit(player, (random.randint(0, screen_width - 33), random.randint(0, screen_height - 33)))

    # placing the suns on the screen
    for i in range(num_of_suns):
        screen.blit(suns[i], (sun_x[i], sun_y[i]))
        # pygame.draw.rect(screen, red, (sun_x[i], sun_y[i], sun_scale, sun_scale), 1)

    # player movement
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        player_x -= player_velocity
    if key[pygame.K_d]:
        player_x += player_velocity
    if key[pygame.K_w]:
        player_y -= player_velocity
    if key[pygame.K_s]:
        player_y += player_velocity

    # call the check for collision function
    for i in range(num_of_suns):
        collision = is_collision(player_x, player_y, sun_x[i], sun_y[i])
        if collision:
            show_hit(100, 100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # pygame.draw.line(screen, red, (100, 160, 200, 260), 3)
    # pygame.draw.lines(screen, red, False, [(150, 200), (200, 300)], 1)
    pygame.display.update()

pygame.quit()
