"""
Stan Weisbecker 7/26/21
first try at MasterMind Game
using pygame in python
"""

import pygame
import random

# import numpy as np

pygame.init()  # Needed to start pygame module

screenWidth = 600  # Setting up the screen size
screenHeight = 800  # Setting up the screen size
player_turn = 0  # Keeps up with what turn the player is on
selected_color = 'red'  # variable to keep track of the color player is using
fps = 30

# used to keep track of where the mouse is pointing
x_min = 80
x_max = 120
y_min = 80
y_max = 120

# Defining the colors in RGB
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)
grey = (120, 120, 120)
orange = (235, 149, 52)

code = []  # the list the player is trying to solve
# guess_code = [['grey' for y in range(4)]  # populates guess code to 40 greys
#               for x in range(10)]

# name of the colors in the game
colorList = ['red', 'green', 'blue', 'yellow', 'white', 'black']

# setting up the screen first time
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('MasterMind')

'''----------------------------- BEGIN SCREEN SET-UP ----------------------------------------'''


def set_playfield():
    # used to set up the spots in the game board
    rows = 40
    columns = 100

    for i in range(40):
        rows += 60
        pygame.draw.circle(screen, grey, (rows, columns), 20)
        if i % 4 == 3:
            columns += 60
            rows = 40
    for x in range(40):
        pass


def set_selection_gui(color):
    # sets up the side selection colors
    y_cor = 100
    for z in range(6):
        pygame.draw.rect(screen, grey, [450, y_cor, 40, 40])
        pygame.draw.rect(screen, colorList[z], [455, (y_cor + 5), 30, 30])
        y_cor += 80

    pygame.draw.circle(screen, grey, (540, 40), 20)
    pygame.draw.circle(screen, color, (540, 40), 15)


def set_color_in_grid():
    # places the guess colors in the correct spots
    x_cord = 100
    y_cord = 100
    for x in range(10):
        for y in range(4):
            pygame.draw.circle(screen, guess_code[x][y], (x_cord, y_cord), 15)
            x_cord += 60
            if y % 4 == 3:
                y_cord += 60
                x_cord = 100


def draw_buttons():
    pygame.draw.rect(screen, orange, (90, 710, 150, 50))
    pygame.draw.rect(screen, orange, (340, 710, 150, 50))


def draw_font():
    # font for the game title
    check_font = pygame.font.SysFont('inkfree', 45, bold=True)
    check_text = check_font.render('MasterMind', True, (42, 245, 48))
    screen.blit(check_text, (44, 14))

    # font for the check button
    check_font = pygame.font.SysFont('inkfree', 25, bold=True)
    check_text = check_font.render('CHECK', True, red)
    screen.blit(check_text, (124, 718))

    # font for the restart button
    start_font = pygame.font.SysFont('inkfree', 25, bold=True)
    start_text = start_font.render('RESTART', True, red)
    screen.blit(start_text, (350, 718))

    selection_font = pygame.font.SysFont('inkfree', 20, bold=True)
    selection_text = selection_font.render('SELECTION', True, red)
    screen.blit(selection_text, (380, 28))


def draw_screen(color):
    screen.fill(black)

    set_playfield()
    set_selection_gui(color)
    set_color_in_grid()
    draw_buttons()
    draw_font()


'''----------------------------- END of SCREEN SET-UP ----------------------------------------'''


def set_players_guess(x_cord, selection, turn):
    if 80 <= x_cord <= 120:
        guess_code[turn][0] = selection
    if 140 <= x_cord <= 180:
        guess_code[turn][1] = selection
    if 200 <= x_cord <= 240:
        guess_code[turn][2] = selection
    if 260 <= x_cord <= 300:
        guess_code[turn][3] = selection
    print(player_turn, guess_code)


def set_code():
    code.clear()
    for i in range(4):
        code.append(random.choice(colorList[0:6]))
    print(code)


def show_code():
    # used to place the code in the spots
    row = 310
    column = 640

    for a in range(4):
        row += 60
        pygame.draw.circle(screen, code[a], (row, column), 15)


def check_guess(guess, cde):
    guess_cpy = guess.copy()
    code_cpy = cde.copy()
    white_peg = 0
    black_peg = 0
    ''' This for loop is used to make the code_cpy list longer so I 
        stop getting an error on the next for loop on the
         second iteration. '''
    for y in range(3):
        code_cpy.append('pink')

    for i in range(4):
        for x in range(4):
            if guess_cpy[i] == code_cpy[x]:
                white_peg += 1
                code_cpy.remove(guess_cpy[i])
    print(white_peg, black_peg)

    guess_cpy = guess.copy()
    code_cpy = cde.copy()

    for x in range(4):
        if guess_cpy[x] == code_cpy[x]:
            black_peg += 1
            white_peg -= 1

    print(guess_cpy, code_cpy, white_peg, black_peg)


def restart():
    global guess_code
    set_code()
    guess_code = [['grey' for y in range(4)]  # populates guess code to 40 greys
                  for x in range(10)]
    return 0


restart()  # sets-up the game for the first run

# game loop
running = True
while running:

    # sets the frames per second
    clock = pygame.time.Clock()
    clock.tick(fps)

    # Variable to capture mouse coordinates during a mouse click
    x_pos = pygame.mouse.get_pos()[0]
    y_pos = pygame.mouse.get_pos()[1]

    # calls the draw screen function
    draw_screen(selected_color)
    show_code()  # function call to show the code for testing

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Used to quit the game if the x is pressed
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                set_code()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check the area where the mouse was clicked
            if event.button == 1:

                # Is the left click at one of the four playing spots
                if (x_min <= x_pos <= x_max or (x_min + 60) <= x_pos <= (x_max + 60)
                    or (x_min + 120) <= x_pos <= (x_max + 120) or (x_min + 180) <= x_pos <= (x_max + 180)) \
                        and y_min <= y_pos <= y_max:
                    print("left mouse button at(%d, %d)" % event.pos)
                    # if guess_code[player_turn] == ['grey', 'grey', 'grey', 'grey']:
                    #     break
                    set_players_guess(x_pos, selected_color, player_turn)

                # check if check button is pressed
                if 90 <= x_pos <= 240 and 710 <= y_pos <= 760:
                    player_turn += 1
                    check_guess(guess_code[player_turn - 1], code)
                    y_min += 60
                    y_max += 60

                # check if restart button is pressed
                if 340 <= x_pos <= 490 and 710 <= y_pos <= 760:
                    player_turn = restart()
                    y_min = 80
                    y_max = 120
                tester = (450 <= x_pos <= 490)

                # Is the left click on one of the side selectors
                if tester and 100 <= y_pos <= 140:
                    selected_color = 'red'
                if 450 <= x_pos <= 490 and 180 <= y_pos <= 220:
                    selected_color = 'green'
                if 450 <= x_pos <= 490 and 260 <= y_pos <= 300:
                    selected_color = 'blue'
                if 450 <= x_pos <= 490 and 340 <= y_pos <= 380:
                    selected_color = 'yellow'
                if 450 <= x_pos <= 490 and 420 <= y_pos <= 460:
                    selected_color = 'white'
                if 450 <= x_pos <= 490 and 500 <= y_pos <= 540:
                    selected_color = 'black'
                # print(selected_color)

    pygame.display.update()

pygame.quit()



