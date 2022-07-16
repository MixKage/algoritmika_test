
#                                      ___      
#                     .-.             (   )     
#    .-..     .---.  ( __)  ___ .-.    | |_     
#   /    \   / .-, \ (''") (   )   \  (   __)   
#  ' .-,  ; (__) ; |  | |   |  .-. .   | |      
#  | |  . |   .'`  |  | |   | |  | |   | | ___  
#  | |  | |  / .'| |  | |   | |  | |   | |(   ) 
#  | |  | | | /  | |  | |   | |  | |   | | | |  
#  | |  ' | ; |  ; |  | |   | |  | |   | ' | |  
#  | `-'  ' ' `-'  |  | |   | |  | |   ' `-' ;  
#  | \__.'  `.__.'_. (___) (___)(___)   `.__.   
#  | |                                          
# (___)  


import pygame
import cfg

pygame.font.init()

font = pygame.font.SysFont(None, 12)

def drawCircle( screen, x,y, color, size):
  pygame.draw.circle( screen, color, ( x,y ), size )

def drawAline(screen, color,x,y):
    pygame.draw.aalines(screen, color, False, (x,y))

def showText(text, smooth, color):
    text = font.render(text, smooth, color)