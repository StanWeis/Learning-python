"""
Stan Weisbecker 7/26/21
first try at MasterMind Game
using pygame in python
"""

import pygame
import random

pygame.init()  # Needed to start pygame module

screenWidth = 600  # Setting up the screen size
screenHeight = 800  # Setting up the screen size
player_turn = 1  # Keeps up with what turn the player is on
selected_color = 'grey'  # variable to keep track of the color player is using

# used to keep track of where the mouse is pointing
xmin = 80
xmax = 120
ymin = 80
ymax = 120

# Defining the colors in RGB
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)
grey = (120, 120, 120)


code = []  # the list the player is trying to solve
guess_code = ['grey', 'grey', 'grey', 'grey']  # Stores the code the player guesses

# name of the colors in the game
colorList = ['red', 'green', 'blue', 'yellow', 'white', 'black']

# setting up the screen first time
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('MasterMind')


def set_code():
    code.clear()
    for i in range(4):
        code.append(random.choice(colorList))
    print(code)


def set_players_guess(xpos, selection):
    print('the x position ', xpos)
    if 80 <= xpos <= 120:
        guess_code[0] = selection
        print(guess_code[0], ' first spot')
    if 140 <= xpos <= 180:
        guess_code[1] = selection
        print(guess_code[1], ' second spot')
    if 200 <= xpos <= 240:
        guess_code[2] = selection
        print(guess_code[2], ' third spot')
    if 260 <= xpos <= 300:
        guess_code[3] = selection
        print(guess_code[3], ' fourth spot')


def draw_screen(color):

    screen.fill(black)

    # used to set up the spots in the game board
    rows = 40
    columns = 100

    for i in range(40):
        rows += 60
        pygame.draw.circle(screen, grey, (rows, columns), 20)
        if i % 4 == 3:
            columns += 60
            rows = 40

    # sets up the side selection colors
    center_select_col = 105
    select_col = 100
    for z in range(6):
        pygame.draw.rect(screen, grey, [450, select_col, 40, 40])
        pygame.draw.rect(screen, colorList[z], [455, center_select_col, 30, 30])
        center_select_col += 80
        select_col += 80

    # shows rhe players selected color in the top right corner.
    pygame.draw.circle(screen, grey, (470, 40), 20)
    pygame.draw.circle(screen, color, (470, 40), 15)

    # places the guess colors in the correct spots
    x_cord = 100
    y_cord = 100
    for x in range(4):
        pygame.draw.circle(screen, guess_code[x], (x_cord, y_cord), 15)
        x_cord += 60


def show_code():

    # used to place the code in the spots
    peg_rows = 40
    peg_column = 20

    for a in range(4):
        peg_rows += 60
        pygame.draw.circle(screen, code[a], (peg_rows, peg_column), 15)


set_code()  # Sets color code to begin the first turn

# game loop
running = True
while running:

    # Variable to capture mouse coordinates during a mouse click
    xPos = pygame.mouse.get_pos()[0]
    yPos = pygame.mouse.get_pos()[1]

    # calls the draw screen function
    draw_screen(selected_color)
    show_code()  # function call to show the code for testing

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Used to quit the game if the x is pressed
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                set_code()
            elif event.key == pygame.K_c:
                print("checking code")
                ymin += 60
                ymax += 60
                yPos += 60

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check the area where the mouse was clicked
            if event.button == 1:

                # Is the left click at one of the four playing spots
                if (xmin <= xPos <= xmax or (xmin + 60) <= xPos <= (xmax + 60)
                        or (xmin + 120) <= xPos <= (xmax + 120) or (xmin + 180) <= xPos <= (xmax + 180)) \
                        and ymin <= yPos <= ymax:
                    print("left mouse button at(%d, %d)" % event.pos)
                    set_players_guess(xPos, selected_color)

                # Is the left click on one of the side selectors
                if 450 <= xPos <= 490 and 100 <= yPos <= 140:
                    selected_color = 'red'
                if 450 <= xPos <= 490 and 180 <= yPos <= 220:
                    selected_color = 'green'
                if 450 <= xPos <= 490 and 260 <= yPos <= 300:
                    selected_color = 'blue'
                if 450 <= xPos <= 490 and 340 <= yPos <= 380:
                    selected_color = 'yellow'
                if 450 <= xPos <= 490 and 420 <= yPos <= 460:
                    selected_color = 'white'
                if 450 <= xPos <= 490 and 500 <= yPos <= 540:
                    selected_color = 'black'
                print(selected_color)

    pygame.display.update()

pygame.quit()


