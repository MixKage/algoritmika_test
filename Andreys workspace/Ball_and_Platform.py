from random import randint
import pygame
import time
pygame.init()
'''создаём окно программы'''
back = (200, 255, 255)
main_window = pygame.display.set_mode(
    (500, 500))  # окно программы (main window)
main_window.fill(back)
clock = pygame.time.Clock()
'''класс прямоугольник'''


class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)  # прямоугольник
        self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(main_window, self.fill_color, self.rect)

    def outline(self, frame_color, thickness):  # обводка существующего прямоугольника
        pygame.draw.rect(main_window, frame_color, self.rect, thickness)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)


'''класс надпись'''


class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont(
            'verdana', fsize).render(text, True, text_color)

    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        main_window.blit(self.image, (self.rect.x +
                         shift_x, self.rect.y + shift_y))

class Image(Area):
    def __init__(self, file_name, x, y, width, height):
        Area.__init__(self, x, y, width, height)
        self.image = pygame.image.load(file_name)

    def draw(self):
        main_window.blit(self.image, (self.rect.x, self.rect.y))

start_x = 5
start_y = 5
count = 9
monsters = []

for i in range(3):
    y = start_y + (55 * i)
    x = start_x + (27.5 * i)
    for j in range(count):
        enemy = Image('enemy.png', x, y, 50, 50)
        monsters.append(enemy)
        x += 55
    count -= 1

ball = Image('ball.png', 230, 250, 50, 50)

platform = Image('platform.png', 200, 350, 50, 50)
    


while True:
    for m in monsters:
        m.draw()
    ball.draw()
    platform.draw()
    pygame.display.update()
    clock.tick(40)

pygame.display.update()
