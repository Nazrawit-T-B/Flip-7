import pygame,sys
from pygame.locals import *
#from UI.button import Button
from card import Card,CardType
import random

def game(display,clock,selectedPlayers):
    
    
    NumCards=[]
    for value in range(13):
        for _ in range(value+1):
            NumCards.append(Card(CardType.NUMBER,value))
    
    print(selectedPlayers)

    ActionCards=[Card(CardType.FREEZE),Card(CardType.FREEZE),Card(CardType.FREEZE),Card(CardType.FLIP_THREE),Card(CardType.FLIP_THREE),Card(CardType.FLIP_THREE),Card(CardType.SECOND_CHANCE),Card(CardType.SECOND_CHANCE),Card(CardType.SECOND_CHANCE)]

    DECK=NumCards+ActionCards
    
    random.shuffle(DECK)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        display.fill((0, 0, 0))  # Fill the screen with black
        pygame.display.flip()
        clock.tick(60)