#Подключение нужных модулей
import pygame
from random import randint
pygame.init()
 
#создание окна игры
clock = pygame.time.Clock()
back = (255, 255, 255) #цвет фона (background)
mw = pygame.display.set_mode((1000, 600)) #окно программы (main window)
mw.fill(back)
 
#цвета
BLACK = (0, 0, 0)
LIGHT_BLUE = (200, 200, 255)

class Area():
    def __init__(self, x=0, y=0, width=5, height=5, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color

    def colorx(self, color_per):
        self.color = color_per

    def fill_color(self):
        pygame.draw.rect(mw, self.color, self.rect)

    def set_outline(self, color_per, shiftx):
        pygame.draw.rect(mw, self.color, self.rect, shiftx)
 
class Label(Area):
   #установить текст
   def set_text(self, text, fsize=12, text_color=BLACK):
       self.text = text
       self.image = pygame.font.Font(None, fsize).render(text, True, text_color)
      
   #отрисовка прямоугольника с текстом
   def draw(self, shift_x=0, shift_y=0):
       pygame.draw.rect(mw, self.fill_color, self.rect)
       mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))   
 
#создание карточек
card1 = Label(150, 300, 100, 100, LIGHT_BLUE)
card1.set_text("Click", 40)
 
card2 = Label(300, 300, 100, 100, LIGHT_BLUE)
card2.set_text("Click", 40)

card3 = Label(450, 300, 100, 100, LIGHT_BLUE)
card3.set_text("Click", 40)
 
card4 = Label(600, 300, 100, 100, LIGHT_BLUE)
card4.set_text("Click", 40)
 
card1.draw(10,40)
card2.draw(10,40)
card3.draw(10,40)
card4.draw(10,40)
 
while 1:
    pygame.display.update()
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
        pygame.QUIT()
                    
    clock.tick(40)           
 
