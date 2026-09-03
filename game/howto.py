# how to play page full of instructions
import pygame,sys
from pygame.locals import *
def howto(display,clock):
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        display.fill((255,197,211))
        pygame.display.flip()
        clock.tick(60)