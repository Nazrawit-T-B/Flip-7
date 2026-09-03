# simple UI class to create a draw buttons
# what it needs to properly to function 
# 1. A background 
#2. A label 
#3. An event 
import pygame 
class Button:
    # constructor function
    def __init__(self, text, x, y, w, h, bg_color=(),text_col=(),hover_col=(),border_r=0):
        self.rect=pygame.Rect(x,y,w,h)
        self.text=text
        self.bg_color=bg_color
        self.curr_col=bg_color
        self.hover_col=hover_col
        self.text_col=text_col
        self.border_r=border_r
        self.font=pygame.font.Font(None,36)
    def update(self):
        mouse_pos=pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.curr_col=self.hover_col
        else:
            self.curr_col=self.bg_color
    def draw(self,surface):
        pygame.draw.rect(surface,self.curr_col,self.rect,border_radius=self.border_r)

        text_surface=self.font.render(self.text,True,self.text_col)

        text_rect=text_surface.get_rect(center=self.rect.center)

        surface.blit(text_surface,text_rect)
    def isClicked(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button ==1 :
                return self .rect.collidepoint(event.pos)
        return False


