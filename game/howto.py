# how to play page full of instructions
import pygame, sys
from pygame.locals import *
from UI.button import Button
from UI.label import * 

def howto(display, clock):
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
    words_array = descriptionTxt.split(' ')
    
    objCard = pygame.Rect(50, 100, 600, 250)
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        display.fill((253,235,239))
       
        title = header.render("How to Play", True, text_color)
        objective = pygame.font.SysFont("Fredoka", 30, bold=False).render("The objective", True, text_color)
      
        display.blit(title, title.get_rect(center=(display.get_width() // 2, 50)))
        display.blit(objective, objective.get_rect(center=(display.get_width() // 6, 80)))
        
        pygame.draw.rect(display, (255, 255, 255), objCard, border_radius=7)
        pygame.draw.rect(display,(255, 197, 211),victory_rect, border_radius=10)
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

        pygame.display.flip()
        clock.tick(60)
