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

''' ----------Game play variables--------------'''
score = 0
low_score = 10
player_turn = 0  # Keeps up with what turn the player is on
selected_color = 'red'  # variable to keep track of the color player is using
fps = 30  # not needed but keeps the game running at 30 frames per sec

black_peg = 0  # Keep track of right color and position
white_peg = 0  # keep track of right color wrong position
black_white_pegs = []  # Keeps track of the white and black answer pegs

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
dk_grey = (90, 90, 90)
orange = (235, 149, 52)

code = []  # the list the player is trying to solve

# name of the colors in the game
colorList = ['red', 'green', 'blue', 'yellow', 'white', 'black']

# setting up the screen first time
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('MasterMind')

'''----------------------------- BEGIN SCREEN SET-UP ----------------------------------------'''


def set_playfield():
    # used to set up the spots in the game board play area
    rows = 40
    columns = 100

    for e in range(40):
        rows += 60
        pygame.draw.circle(screen, grey, (rows, columns), 20)
        if e % 4 == 3:
            columns += 60
            rows = 40

    # sets up the spots beside the play area showing the answer code
    rows = 300
    columns = 85

    for r in range(40):
        rows += 30
        pygame.draw.circle(screen, grey, (rows, columns), 10)
        if r % 2 == 1:
            columns += 30
            rows = 300


def set_selection_gui(color):
    # sets up the side selection colors
    y_cor = 320
    for z in range(6):
        pygame.draw.rect(screen, grey, [450, y_cor, 40, 40])
        pygame.draw.rect(screen, colorList[z], [455, (y_cor + 5), 30, 30])
        y_cor += 60

    pygame.draw.circle(screen, grey, (560, 260), 20)
    pygame.draw.circle(screen, color, (560, 260), 15)


def set_color_in_grid():
    # places the guess_code array colors in the correct spots
    x_cord = 100  # beginning x coordinate
    y_cord = 100  # beginning y coordinate
    for t in range(10):
        for y in range(4):
            pygame.draw.circle(screen, guess_code[t][y], (x_cord, y_cord), 15)
            x_cord += 60
            if y % 4 == 3:
                y_cord += 60
                x_cord = 100

    x_cord = 330
    y_cord = 85
    for u in range(10):
        for y in range(4):
            pygame.draw.circle(screen, answer_code[u][y], (x_cord, y_cord), 8)
            x_cord += 30
            if y % 2 == 1:
                y_cord += 30
                x_cord = 330


def draw_buttons():
    pygame.draw.rect(screen, orange, (90, 710, 150, 50))
    pygame.draw.rect(screen, orange, (340, 710, 150, 50))


def draw_font():
    # font for the game title
    title_font = pygame.font.SysFont('inkfree', 45, bold=True)
    title_text = title_font.render('MasterMind', True, (42, 245, 48))
    screen.blit(title_text, (44, 14))

    # font for the check button
    check_font = pygame.font.SysFont('inkfree', 25, bold=True)
    check_text = check_font.render('CHECK', True, red)
    screen.blit(check_text, (124, 718))

    # font for the restart button
    start_font = pygame.font.SysFont('inkfree', 25, bold=True)
    start_text = start_font.render('RESTART', True, red)

    # font for the 'selection' round indicator
    selection_font = pygame.font.SysFont('inkfree', 20, bold=True)
    selection_text = selection_font.render('SELECTION', True, red)
    screen.blit(selection_text, (395, 248))

    # font for the 'score' round indicator
    score_font = pygame.font.SysFont('inkfree', 30, bold=True)
    score_text = score_font.render('SCORE', True, white)
    screen.blit(score_text, (420, 75))

    # font for the 'best score' round indicator
    score_font = pygame.font.SysFont('inkfree', 22, bold=True)
    score_text = score_font.render('BEST SCORE', True, white)
    screen.blit(score_text, (400, 180))


def draw_screen(color):
    screen.fill(black)  # fills the screen black
    set_playfield()  # sets up all the spots for the game
    set_selection_gui(color)  # places color boxes on side the player can select
    set_color_in_grid()  # places the selected color in the spot player clicks
    draw_buttons()  # places all the clickable buttons on the screen
    draw_font()  # places all the lettering on the screen


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


def set_code():
    code.clear()
    for p in range(4):
        code.append(random.choice(colorList[0:6]))


def show_code():
    # used to place the code in the spots
    row = 40
    column = 690

    for f in range(4):
        row += 60
        pygame.draw.circle(screen, code[f], (row, column), 10)


def check_guess(guess, cde):
    """ make copies of the variables so they don't change the original when
        manipulated in the function """
    guess_cpy = guess.copy()
    code_cpy = cde.copy()

    white_correct = 0  # keep track of correct color wrong spot on guess
    black_correct = 0  # keep track of correct color correct spot on guess

    ''' This for loop is used to make the code_cpy list longer so I 
        stop getting an error on the next for loop on the
         second iteration. '''
    for y in range(4):
        code_cpy.append('pink')

    """sets the white correct in the code"""
    for q in range(4):
        for w in range(4):
            if guess_cpy[q] == code_cpy[w]:
                white_correct += 1
                code_cpy.remove(guess_cpy[q])

    """ resets make copies of the variables so they don't change the original 
        when manipulated in the function """
    guess_cpy = guess.copy()
    code_cpy = cde.copy()

    """sets the black correct in the code"""
    for w in range(4):
        if guess_cpy[w] == code_cpy[w]:
            black_correct += 1
            white_correct -= 1

    """returns the black correct and white correct in the code to the caller"""
    return black_correct, white_correct


def restart():
    global guess_code, answer_code

    set_code()
    guess_code = [['grey' for s in range(4)]  # populates guess code to 40 greys
                  for d in range(10)]

    answer_code = [[blue for f in range(4)]  # populates answer code to 40 greys
                   for g in range(10)]

    return 0


def game_over():
    print(score)
    pass


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

                    # if guess_code[player_turn] == ['grey', 'grey', 'grey', 'grey']:
                    #     break
                    set_players_guess(x_pos, selected_color, player_turn)

                # check if check button is pressed
                if 90 <= x_pos <= 240 and 710 <= y_pos <= 760:

                    black_white_pegs = check_guess(guess_code[player_turn], code)
                    y_min += 60
                    y_max += 60

                    for a in range(black_white_pegs[0]):
                        answer_code[player_turn][a] = 'black'

                    for x in range(black_white_pegs[1]):
                        answer_code[player_turn][x + black_white_pegs[0]] = 'white'

                    if black_white_pegs[0] == 4:
                        game_over()

                    player_turn += 1

                # check if restart button is pressed
                if 340 <= x_pos <= 490 and 710 <= y_pos <= 760:
                    player_turn = restart()
                    y_min = 80
                    y_max = 120

                selection_x_cord = (450 <= x_pos <= 490)

                y_low = 320
                y_high = 360

                # Is the left click on one of the side selectors
                if selection_x_cord and y_low <= y_pos <= y_high:
                    selected_color = colorList[0]
                if selection_x_cord and (y_low + 60) <= y_pos <= (y_high + 60):
                    selected_color = colorList[1]
                if selection_x_cord and (y_low + 120) <= y_pos <= (y_high + 120):
                    selected_color = colorList[2]
                if selection_x_cord and (y_low + 180) <= y_pos <= (y_high + 180):
                    selected_color = colorList[3]
                if selection_x_cord and (y_low + 240) <= y_pos <= (y_high + 240):
                    selected_color = colorList[4]
                if selection_x_cord and (y_low + 300) <= y_pos <= (y_high + 300):
                    selected_color = colorList[5]

    pygame.display.update()

pygame.quit()



