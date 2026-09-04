#simple UI class to create simple and unique text labels
import pygame 
class Label:
    def __init__(self,text,bg_color,text_color,x,y,w,h,border_r=0):
        self.text=text
        self.rect=pygame.rect(x,y,w,h)
        self.bg_color=bg_color
        self.text_color=text_color
        self.border_r=border_r
    def draw(self,display):
        pygame.draw.rect(display,self.bg_color,self.rect,border_radius=self.border_r)
        
