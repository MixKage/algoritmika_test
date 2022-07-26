import pygame
import random

pygame.init()

clock = pygame.time.Clock()

#Создание экрана
mw = pygame.display.set_mode((500,500))
mw.fill((255,255,255))

#Создание цветов
BLACK = (0,0,0)
LIGHT_BLUE = (200,200,255)

#Работа с текстом
class TextArea():
    def __init__(self, x=0,y=0, width=10,height=10,color=None):
        self.rect = pygame.Rect(x,y,width,height)
        self.fill_color = color
    
    #отрисовка прямоугольника с текстом
    def draw(self, shift_x=0, shift_y=0):
        pygame.draw.rect(mw,self.fill_color,self.rect)
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))
    
    def set_text(self, text, fsize=12, text_color=BLACK):
        self.text = text
        self.image = pygame.font.Font(None, fsize).render(text, True, text_color)
    
quest_card = TextArea(120,100,290,70,LIGHT_BLUE)
quest_card.set_text("Вопрос: ", 75)

ans_card = TextArea(120,240,290,70,LIGHT_BLUE)
ans_card.set_text("Ответ: ", 75)

while True:
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                num = random.randint(1,3)                
                quest_card.set_text(str(num)+"q",25)

                quest_card.draw(10,25)

            if event.key == pygame.K_a:
                num = random.randint(1,3)                
                ans_card.set_text(str(num)+"a",25)

                ans_card.draw(10,10)

    clock.tick(40)