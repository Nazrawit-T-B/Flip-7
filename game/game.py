import pygame,sys
from pygame.locals import *
from UI.button import Button
from card import Card,CardType
import random
from UI.layout import LAYOUTS
from game.player import Player

def end_round(players):
    for p in players:
        p.skipped=False
        p.frozen=False
        p.hand=[]

def draw_card(display,card,pos):
    if card.is_number():
        card_image = pygame.image.load(f"Assets/cardimg/{card.value}.jpg").convert_alpha()
    else:
        card_image = pygame.image.load(f"Assets/cardimg/{card.card_type.name}.png").convert_alpha()
    scaled_card = pygame.transform.scale(card_image, (64, 80))
    display.blit(scaled_card, pos)

def build_deck(selectedPlayers):
    NumCards = []
    
    for value in range(13):
            for _ in range(value+1):
                NumCards.append(Card(CardType.NUMBER,value))
        
    print(selectedPlayers)
    
    ActionCards = [Card(CardType.FREEZE),Card(CardType.FREEZE),Card(CardType.FREEZE),Card(CardType.FLIP_THREE),Card(CardType.FLIP_THREE),Card(CardType.FLIP_THREE),Card(CardType.SECOND_CHANCE),Card(CardType.SECOND_CHANCE),Card(CardType.SECOND_CHANCE)]
    
    DECK=NumCards+ActionCards
    
    random.shuffle(DECK)
    return DECK
def has_flip7(player):
    return len({c.value for c in player.hand if c.is_number()}) >=7
def get_next_active(players, current_player, selectedPlayers):
    next_player = (current_player + 1) % selectedPlayers
    for _ in range(selectedPlayers):
        if not players[next_player].skipped and not players[next_player].frozen:
            return next_player
        next_player = (next_player + 1) % selectedPlayers
    return None
def has_duplicate(Player_Card,players,current_player):
    if not Player_Card.is_number():
        return False
    return any(c.is_number() and c.value == Player_Card.value for c in players[current_player].hand)
def game(display,clock,selectedPlayers):
    font=pygame.font.SysFont('Fredoka',20,bold=False)
    hitBtn=Button("Hit",50,700,100,50,border_r=5)
    skipBtn=Button("Skip",170,700,100,50,border_r=5)
 
    DECK=build_deck(selectedPlayers)

    players=[Player() for _ in range(selectedPlayers)]
    positions = LAYOUTS[selectedPlayers]["players"]

    deck_position=LAYOUTS[selectedPlayers]["deck"]

    cardBack = pygame.image.load("Assets/cardimg/cardBack.png").convert_alpha()
    scaleBack=pygame.transform.scale(cardBack,(64,80))

    current_player=0
    Player_Card=None
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if hitBtn.isClicked(event):
                if len(DECK)>0 and not players[current_player].skipped and not players [current_player].frozen:
                        Player_Card=DECK.pop(0)
                        duplicate=has_duplicate(Player_Card,players,current_player)
                        if not duplicate:
                            players[current_player].hand.append(Player_Card)
                            if Player_Card.is_number():
                                players[current_player].score+=Player_Card.value
                            print(players[current_player].score)
                            if has_flip7(players[current_player]):
                                end_round(players)
                                current_player=0
                            else:
                                nxt=get_next_active(players,current_player,selectedPlayers)
                                if nxt is None:
                                    end_round(players)
                                    current_player=0
                                else:
                                    current_player=nxt
                        else:
                            players[current_player].score-=sum(c.value for c in players[current_player].hand if c.is_number())
                            players[current_player].skipped=True
                            display.blit(font.render(f"Duplicate found!Player {current_player}",True,(40,40,40)),(400,400))
                            nxt=get_next_active(players,current_player,selectedPlayers)
                            if nxt is None:
                                end_round(players)
                                current_player=0
                            else:
                                current_player=nxt
            if skipBtn.isClicked(event):
                players[current_player].skipped=True
                nxt=get_next_active(players,current_player,selectedPlayers)
                if nxt is None:
                    end_round(players)
                    current_player=0
                else:
                    current_player=nxt
        display.fill((253,235,239)) 
        if len(DECK)>0:
            display.blit(scaleBack,deck_position)
        for player_index,player in enumerate(players):
            start_x, start_y = positions[player_index]
            score_text=font.render(f"Player {player_index+1}-> {player.score}",True,(40,40,40))
            display.blit(score_text,(start_x,start_y-30))
            for card_index, card in enumerate(player.hand):
                draw_card(display, card, (start_x + card_index * 25, start_y))         
        hitBtn.update()
        hitBtn.draw(display)
        skipBtn.update()
        skipBtn.draw(display)
        pygame.display.flip()
        clock.tick(60)
 