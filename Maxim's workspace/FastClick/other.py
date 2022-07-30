import pygame as pg
import settings as st

class Area():
    def __init__(self, sc=None, x=0,y=0, width=50,height=80, color=None):
        self.rect = pg.Rect(x, y, width, height)
        self.color = color
        self.screen = sc

    def setColor(self, color):
        self.color = color

    def colorFill(self): # Заливка карточки
        pg.draw.rect(self.screen, self.color, self.rect)

    def setOutline(self, color, shift=5):
        pg.draw.rect(self.screen, color, self.rect, shift)

class Label(Area):
    def __init__(self, sc, x, y=st.scHeight//2.5):
        super().__init__()
        self.screen = sc
        self.rect.x = x
        self.rect.y = y

    def set_text(self, text, fsize=12, text_color=(0,0,0)):
        self.text = text
        self.image = pg.font.Font(None, fsize).render(text, True, text_color)
    
    def draw(self, shift_x=0, shift_y=0, shift=5):   
        pg.draw.rect(self.screen, self.color, self.rect)
        self.screen.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))
    
        