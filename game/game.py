import pygame,sys
from pygame.locals import *
from UI.button import Button
def game(display,clock):
    # Placeholder for the game logic
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        display.fill((0, 0, 0))  # Fill the screen with black
        pygame.display.flip()
        clock.tick(60)