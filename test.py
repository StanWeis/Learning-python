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
player_turn = 0  # Keeps up with what turn the player is on

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


def draw_screen():

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


def show_code():

    # used to place the code in the spots
    peg_rows = 40
    peg_column = 100

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
    draw_screen()
    show_code()  # function call to show the code for testing

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Used to quit the game if the x is pressed
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                set_code()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if (xmin <= xPos <= xmax or (xmin + 60) <= xPos <= (xmax + 60)
                        or (xmin + 120) <= xPos <= (xmax + 120) or (xmin + 180) <= xPos <= (xmax + 180)) \
                        and ymin <= yPos <= ymax:
                    print("left mouse button at(%d, %d)" % event.pos)
                # if 140 <= xPos <= 180 and 80 <= yPos <= 120:
                #     print("left mouse button at(%d, %d)" % event.pos)
                # if 200 <= xPos <= 240 and 80 <= yPos <= 120:
                #     print("left mouse button at(%d, %d)" % event.pos)
                # if 260 <= xPos <= 300 and 80 <= yPos <= 120:
                #     print("left mouse button at(%d, %d)" % event.pos)
            elif event.button == 2:
                if 80 <= xPos <= 120 and 80 <= yPos <= 120:
                    print("middle mouse button at(%d, %d)" % event.pos)
            elif event.button == 3:
                if 80 <= xPos <= 120 and 80 <= yPos <= 120:
                    print("right mouse button at(%d, %d)" % event.pos)
            elif event.button == 4:
                print("mouse wheel up")
            elif event.button == 5:
                print("mouse wheel down")

    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:  # Used to quit the game if the x is pressed
    #         running = False
    #
    #     if event.type == pygame.KEYDOWN:
    #         if event.key == pygame.K_n:
    #             set_code()
    #
    #     elif event.type == pygame.MOUSEBUTTONDOWN:
    #         if event.button == 1:
    #             if xmin <= xPos <= xmax and ymin <= yPos <= ymax:
    #                 print("left mouse button at(%d, %d)" % event.pos)
    #             if 140 <= xPos <= 180 and 80 <= yPos <= 120:
    #                 print("left mouse button at(%d, %d)" % event.pos)
    #             if 200 <= xPos <= 240 and 80 <= yPos <= 120:
    #                 print("left mouse button at(%d, %d)" % event.pos)
    #             if 260 <= xPos <= 300 and 80 <= yPos <= 120:
    #                 print("left mouse button at(%d, %d)" % event.pos)
    #         elif event.button == 2:
    #             if 80 <= xPos <= 120 and 80 <= yPos <= 120:
    #                 print("middle mouse button at(%d, %d)" % event.pos)
    #         elif event.button == 3:
    #             if 80 <= xPos <= 120 and 80 <= yPos <= 120:
    #                 print("right mouse button at(%d, %d)" % event.pos)
    #         elif event.button == 4:
    #             print("mouse wheel up")
    #         elif event.button == 5:
    #             print("mouse wheel down")

    pygame.display.update()

pygame.quit()

