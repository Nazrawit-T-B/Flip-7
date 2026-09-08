import pygame, sys
from pygame.locals import *
from game.menu import menu
from game.game import game

pygame.init()

def main():
    display = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption('Flip 7')
    clock = pygame.time.Clock()
    status = "menu"
    selectedPlayers = None

    while True:
        if status == "menu":
            result = menu(display, clock)
            selectedPlayers = result
            status = "game"
        elif status == "game":
            game(display, clock, selectedPlayers)
            status = "menu" 
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()