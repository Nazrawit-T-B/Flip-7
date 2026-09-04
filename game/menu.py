# menu page that prompts the user to enter the number of players 
import pygame, sys
from pygame.locals import*
from UI.button import Button
from game.howto import howto
def menu(display,clock):
    options=[2,3,4,5,6]
    selectedPlayers=2
    btnSize=50
    gap=20
    playerAmountCard=pygame.Rect(350,300,100,100)
    addBtn=Button("+",playerAmountCard.right+gap,playerAmountCard.centery-btnSize//2,btnSize,btnSize)
    subBtn=Button("-",playerAmountCard.left - btnSize-gap, playerAmountCard.centery-btnSize //2, btnSize,btnSize)
    continueBtn=Button("Continue",playerAmountCard.x+5,playerAmountCard.bottom+gap,100,50,border_r=5)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if addBtn.isClicked(event) and selectedPlayers < max(options):
                selectedPlayers+=1
            if subBtn.isClicked(event) and selectedPlayers > min(options):
                selectedPlayers-=1
            if continueBtn.isClicked(event):
                result=howto(display,clock)
                if result=="menu":
                    continue
        display.fill((253,235,239))
        title = pygame.font.SysFont("Fredoka", 30, bold=True).render("Select Number of Players", False, (102, 44, 57))
        display.blit(title, title.get_rect(center=(display.get_width() // 2, 250)))
        pygame.draw.rect(display,(153,96,110),playerAmountCard,border_radius=5)
        addBtn.update()
        addBtn.draw(display)
        subBtn.update()
        subBtn.draw(display)
        continueBtn.update()
        continueBtn.draw(display)
        text= pygame.font.SysFont("Fredoka", 50, bold=True).render(str(selectedPlayers),True,(255,255,255))
        display.blit(text, text.get_rect(center=playerAmountCard.center))
        pygame.display.flip()

        clock.tick(60)



