import pygame
import random

deck = 'ace two three four'.split()
random.shuffle(deck)
print(deck)

# used to define a mouse click
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            print("left mouse button")
        elif event.button == 2:
            print("middle mouse button")
        elif event.button == 3:
            print("right mouse button")
        elif event.button == 4:
            print("mouse wheel up")
        elif event.button == 5:
            print("mouse wheel down")
