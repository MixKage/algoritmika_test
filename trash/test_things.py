import queue
import pygame

pygame.init()

sc = pygame.display.set_mode((1000, 500))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()