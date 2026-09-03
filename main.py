import pygame,sys
from pygame.locals import *
from game.menu import menu
from game.howto import howto
pygame.init()
def main():
    display=pygame.display.set_mode((800,800))
    pygame.display.set_caption('Flip 7')
    clock=pygame.time.Clock()
    status="menu"
    while True:
        if status =="menu":
            result=menu(display,clock)
            if result=="howto":
                status="howto"
            continue
        elif status=="howto":
            result=howto(display,clock)
            if result=="menu":
                status="menu"
        pygame.display.update()
        clock.tick(60)
if __name__=='__main__':
    main()



