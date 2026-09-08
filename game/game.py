import pygame,sys
from pygame.locals import *
from UI.button import Button
from card import Card,CardType
import random
from UI.layout import LAYOUTS
def draw_card(display,card,pos):
    if card.is_number():
        card_image = pygame.image.load(f"Assets/cardimg/{card.value}.jpg").convert_alpha()
    else:
        card_image = pygame.image.load(f"Assets/cardimg/{card.card_type.name}.png").convert_alpha()
    scaled_card = pygame.transform.scale(card_image, (64, 80))
    display.blit(scaled_card, pos)
    
def game(display,clock,selectedPlayers):
    
    hitBtn=Button("Hit",50,700,100,50,border_r=5)
    NumCards = []

    for value in range(13):
        for _ in range(value+1):
            NumCards.append(Card(CardType.NUMBER,value))
    
    print(selectedPlayers)

    ActionCards = [Card(CardType.FREEZE),Card(CardType.FREEZE),Card(CardType.FREEZE),Card(CardType.FLIP_THREE),Card(CardType.FLIP_THREE),Card(CardType.FLIP_THREE),Card(CardType.SECOND_CHANCE),Card(CardType.SECOND_CHANCE),Card(CardType.SECOND_CHANCE)]

    DECK=NumCards+ActionCards

    random.shuffle(DECK)

    positions = LAYOUTS[selectedPlayers]["players"]

    deck_position=LAYOUTS[selectedPlayers]["deck"]

    cardBack = pygame.image.load("Assets/cardimg/cardBack.png").convert_alpha()
    scaleBack=pygame.transform.scale(cardBack,(64,80))

    player_hands=[[] for _ in range(selectedPlayers)]
    current_player=-1
    Player_Card=None
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if hitBtn.isClicked(event):
                if len(DECK)>0:
                    Player_Card=DECK.pop(0)
                    player_hands[current_player].append(Player_Card)
                    current_player=(current_player+1)%selectedPlayers
        display.fill((253,235,239)) 
        if len(DECK)>0:
            display.blit(scaleBack,deck_position)
        for player_index,hand in enumerate(player_hands):
            start_x, start_y = positions[player_index]
            for card_index, card in enumerate(hand):
                draw_card(display, card, (start_x + card_index * 25, start_y))
        hitBtn.update()
        hitBtn.draw(display)
        pygame.display.flip()
        clock.tick(60)
