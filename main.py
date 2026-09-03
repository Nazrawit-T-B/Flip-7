import pygame,sys
from pygame.locals import *
from game.menu import*
pygame.init()
def main():
    display=pygame.display.setmode((800,800))
    pygame.set_caption('Flip 7')
    clock=pygame.time.Clock()
    status="menu"
    while True:
        if status =="menu":
            continue
        pygame.display.update()
        clock.tick(60)
if __name__=='__main__':
    main()



