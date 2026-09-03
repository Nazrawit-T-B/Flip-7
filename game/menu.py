# menu page that prompts the user to enter the number of players 
import pygame, sys
from pygame.locals import*
from UI.button import Button
def menu(display,clock):
    options=[2,3,4,5,6]
    selectedPlayers=2
    btnSize=50
    gap=2
    playerAmountCard=pygame.Rect(350,300,100,100)
    addBtn=Button("+",playerAmountCard.right+gap,playerAmountCard.centery-btnSize//2,btnSize,btnSize)
    subBtn=Button("-",playerAmountCard.left - btnSize-gap, playerAmountCard.centery-btnSize //2, btnSize,btnSize)
    continueBtn=Button("Continue",350,400,50,50)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if addBtn.isClicked(event) and selectedPlayers < max(options):
                selectedPlayers+=1
            if subBtn.isClicked(event) and selectedPlayers > min(options):
                selectedPlayers-=1
        display.fill((255,197,211))
        pygame.draw.rect(display,(),playerAmountCard,border_radius=5)
        addBtn.update()
        addBtn.draw(display)
        subBtn.update()
        subBtn.draw(display)
        pygame.display.flip()

        clock.tick(60)



