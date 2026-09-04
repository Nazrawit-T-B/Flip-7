import pygame, sys
from pygame.locals import *
from UI.button import Button
from UI.label import * 
from game.game import game
def howto2(display, clock):

    header = pygame.font.SysFont("Fredoka", 30, bold=True)
    body_font = pygame.font.SysFont('Fredoka', 20, bold=False)
    text_color = (102, 44, 57)
    playgameBtn=Button("Play Game",display.get_width()//3-50,display.get_height()-70,120,50,border_r=5,font_size=20)
    menuBtn=Button("Menu",display.get_width()//2-50,display.get_height()-70,100,50,border_r=5,font_size=10)

    anatomy_header=header.render("Anatomy of a Turn",True,text_color)
    specialActionheader=header.render("Special Action Cards",True,text_color)

    anatomyCard2=pygame.Rect(50,100,600,150)
    anatomyCard3=pygame.Rect(50,280,600,150)

    duplicateinst=header.render("Avoid the duplicate",True,text_color)
    duplicateinst2=body_font.render("Cards numbered 0 through 12 populate the deck.If you flip a number that you already have",True,text_color)
    duplicateinst3=body_font.render("in your active hand this round: YOU BUST!You forefeit all points accumulated for this",True,text_color)
    duplicateinst4=body_font.render("round",True,text_color)

    flipinst=header.render("Flip 7 =Jackpot !",True,text_color)
    flipinst1=body_font.render("If you successfully reveal 7 unique number cards without busting,you trigger an instant ",True,text_color)
    flipinst2=body_font.render(" round win,collect an extra +15 BONUS POINTS and immediately lock in your score!",True,text_color)   

    secondChance_rect=pygame.Rect(60,500,300,100)
    Freeze_rect=pygame.Rect(400,500,300,100)
    FlipThree_rect=pygame.Rect(60,610,300,100)
    Modifiers_rect=pygame.Rect(400,610,300,100)

    secondChanceHeader=body_font.render("Second Chance",True,text_color)
    secondChancedesc=body_font.render("Hold this card in front of you. When you draw",True,text_color)
    secondChancedesc2=body_font.render("a duplicate, you can use this card to avoid ",True,text_color)
    secondChancedesc3=body_font.render("busting and continue your turn.",True,text_color)

    freezeHeader=body_font.render("Freeze",True,text_color)
    freezedesc=body_font.render("Forces a chosen player (or yourself) to ",True,text_color)
    freezedesc2=body_font.render("immediately stop flipping and lock in their ",True,text_color)
    freezedesc3=body_font.render("current card score for the round.",True,text_color)

    flipThreeHeader=body_font.render("Flip Three",True,text_color)
    flipThreedesc=body_font.render("You must immediately flip 3 cards ",True,text_color)
    flipThreedesc2=body_font.render("consecutively! If any one duplicates, you ",True,text_color)
    flipThreedesc3=body_font.render("bust out instantly unless protected",True,text_color)

    modifiersHeader=body_font.render("Modifiers",True,text_color)
    modifiersdesc=body_font.render("Modifiers do not count as number cards ",True,text_color)
    modifiersdesc2=body_font.render(" toward the 7- card threshold, but add flat  ",True,text_color)
    modifiersdesc3=body_font.render("bonus points to your banked round score",True,text_color)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if playgameBtn.isClicked(event):
                result=game(display,clock)
            elif menuBtn.isClicked(event):
                return "menu"
        display.fill((253,235,239))

    
        display.blit(anatomy_header,(50,50))
        pygame.draw.rect(display,(255,255,255),anatomyCard2,border_radius=7)
        display.blit(duplicateinst,(anatomyCard2.x+20,anatomyCard2.y+15))
        display.blit(duplicateinst2,(anatomyCard2.x+20,anatomyCard2.y+50))
        display.blit(duplicateinst3,(anatomyCard2.x+20,anatomyCard2.y+70))
        display.blit(duplicateinst4,(anatomyCard2.x+20,anatomyCard2.y+90))

        pygame.draw.rect(display,(255,255,255),anatomyCard3,border_radius=7)
        display.blit(flipinst,(anatomyCard3.x+20,anatomyCard3.y+15))
        display.blit(flipinst1,(anatomyCard3.x+20,anatomyCard3.y+50))
        display.blit(flipinst2,(anatomyCard3.x+20,anatomyCard3.y+70))

        display.blit(specialActionheader,(50,450))
        pygame.draw.rect(display,(255, 197, 211),secondChance_rect,border_radius=7)
        pygame.draw.rect(display,(255,255,255),Freeze_rect,border_radius=7)
        pygame.draw.rect(display,(255,255,255),FlipThree_rect,border_radius=7)
        pygame.draw.rect(display,(255,197,211),Modifiers_rect,border_radius=7)

        display.blit(secondChanceHeader,(secondChance_rect.x+20,secondChance_rect.y+10))
        display.blit(secondChancedesc,(secondChance_rect.x+10,secondChance_rect.y+30))
        display.blit(secondChancedesc2,(secondChance_rect.x+10,secondChance_rect.y+43))
        display.blit(secondChancedesc3,(secondChance_rect.x+10,secondChance_rect.y+56))

        display.blit(freezeHeader,(Freeze_rect.x+20,Freeze_rect.y+10))
        display.blit(freezedesc,(Freeze_rect.x+10,Freeze_rect.y+30))
        display.blit(freezedesc2,(Freeze_rect.x+10,Freeze_rect.y+43))
        display.blit(freezedesc3,(Freeze_rect.x+10,Freeze_rect.y+56))

        
        display.blit(flipThreeHeader,(FlipThree_rect.x+20,FlipThree_rect.y+10))
        display.blit(flipThreedesc,(FlipThree_rect.x+10,FlipThree_rect.y+30))
        display.blit(flipThreedesc2,(FlipThree_rect.x+10,FlipThree_rect.y+43))
        display.blit(flipThreedesc3,(FlipThree_rect.x+10,FlipThree_rect.y+56))

        display.blit(modifiersHeader,(Modifiers_rect.x+20,Modifiers_rect.y+10))
        display.blit(modifiersdesc,(Modifiers_rect.x+10,Modifiers_rect.y+30))
        display.blit(modifiersdesc2,(Modifiers_rect.x+10,Modifiers_rect.y+43))
        display.blit(modifiersdesc3,(Modifiers_rect.x+10,Modifiers_rect.y+56))
        
        playgameBtn.update()
        playgameBtn.draw(display)
        menuBtn.update()
        menuBtn.draw(display)
    
        pygame.display.flip()

        clock.tick(60)
