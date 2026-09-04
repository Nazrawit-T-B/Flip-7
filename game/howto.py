# how to play page full of instructions
import pygame, sys
from pygame.locals import *
from UI.button import Button
from UI.label import * 
from game.howto2 import howto2
from game.game import game
def howto(display, clock):
    continueBtn=Button("Continue",display.get_width()//7-50,display.get_height()-100,100,50,border_r=5,font_size=20)
    playgameBtn=Button("Play Game",display.get_width()//3-50,display.get_height()-100,120,50,border_r=5,font_size=20)
    menuBtn=Button("Menu",display.get_width()//2-50,display.get_height()-100,100,50,border_r=5,font_size=10)
    header = pygame.font.SysFont("Fredoka", 30, bold=True)
    body_font = pygame.font.SysFont('Fredoka', 20, bold=False)
    text_color = (102, 44, 57)
    
    descriptionTxt = (
        "Score more points by flipping cards into your active row. "
        "Bank your points by choosing to Freeze or push your luck to collect "
        "7 unique number cards for a massive jackpot bonus"
    )
    victory_header=pygame.font.SysFont("Fredoka",20,bold=True).render("Victory Condition",True,text_color)

    victory_desc1=body_font.render("The first player to accumulate 200 total points across rounds wins!",True,text_color)
    victory_rect=pygame.Rect(60,220,500,100)
    flip_rect=pygame.Rect(60,500,250,100)
    freeze_rect=pygame.Rect(330,500,250,100)

    anatomy_header=header.render("Anatomy of a Turn",True,text_color)

    words_array = descriptionTxt.split(' ')


    
    objCard = pygame.Rect(50, 100, 600, 250)
    anatomyCard1=pygame.Rect(50,395,600,250)
    anatomyCard1desc=header.render("Flip or Freeze?",True,text_color)
    anatomyCard1detail=body_font.render("On your turn, choose to FLIP the top card from the deck into your collection, ",True,text_color)
    anatomyCard1detail2=body_font.render("or FREEZE your collection to bank your points and end your turn.",True,text_color)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if continueBtn.isClicked(event):
                        result=howto2(display,clock)
                        if result=="menu":
                            return "menu"
                        elif result=="game":
                            return "game"
            elif menuBtn.isClicked(event):
                        return "menu"
            elif playgameBtn.isClicked(event):
                        return "game"  
        display.fill((253,235,239))
       
        title = header.render("How to Play", True, text_color)
        objective = pygame.font.SysFont("Fredoka", 30, bold=False).render("The objective", True, text_color)
      
        display.blit(title, title.get_rect(center=(display.get_width() // 2, 50)))
        display.blit(objective, objective.get_rect(center=(display.get_width() // 6, 80)))
        
        pygame.draw.rect(display, (255, 255, 255), objCard, border_radius=7)
        pygame.draw.rect(display,(255, 197, 211),victory_rect, border_radius=10)
        pygame.draw.rect(display,(255,255,255),anatomyCard1,border_radius=7)
        pygame.draw.rect(display,(255,197,211),flip_rect,border_radius=10)
        pygame.draw.rect(display,(255,197,211),freeze_rect,border_radius=10)
        start_x = objCard.x + 20
        current_y = objCard.y + 40
        max_width = objCard.width - 40 
        
        current_line = ""
        
        for word in words_array:
            test_line = current_line + " " + word if current_line else word
            
            if body_font.size(test_line)[0] < max_width:
                current_line = test_line
            else:
        
                line_surface = body_font.render(current_line, True, text_color)
                display.blit(line_surface, (start_x, current_y))
                
                current_y += line_surface.get_height() + 6
                current_line = word
    
        if current_line:
            line_surface = body_font.render(current_line, True, text_color)
            display.blit(line_surface, (start_x, current_y))
        
        display.blit(victory_header,(victory_rect.x+20,victory_rect.y+15))
        display.blit(victory_desc1,(victory_rect.x+20,victory_rect.y+50))
        display.blit(anatomy_header,(50,370))
        display.blit(anatomyCard1desc,(anatomyCard1.x+20,anatomyCard1.y+15))
        display.blit(anatomyCard1detail,(anatomyCard1.x+20,anatomyCard1.y+50))
        display.blit(anatomyCard1detail2,(anatomyCard1.x+20,anatomyCard1.y+80))
        display.blit(header.render("Flip",True,text_color),(flip_rect.x+60,flip_rect.y+15))
        display.blit(body_font.render("Draw & add to hand",True,text_color),(flip_rect.x+40,flip_rect.y+50))
        display.blit(header.render("Freeze",True,text_color),(freeze_rect.x+60,freeze_rect.y+15))
        display.blit(body_font.render("Bank points & stay",True,text_color),(freeze_rect.x+40,freeze_rect.y+50))
        continueBtn.update()
        continueBtn.draw(display)
        playgameBtn.update()
        playgameBtn.draw(display)
        menuBtn.update()
        menuBtn.draw(display)
        pygame.display.flip()
        clock.tick(60)
