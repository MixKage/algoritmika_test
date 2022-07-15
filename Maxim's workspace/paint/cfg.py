
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

FPS = 75  # Frame Per Seconds
screen_size = (800, 800)  # WEIGHT, HEIGHT
font = pygame.font.SysFont('microsofttaile', 12)


bool = False  # Useful bool, just bool

isMousePressed = False  # MousePressed

colors = {
    1: (0, 0, 0),   # BLACK
    2: (255, 255, 255),   # WHITE
    3: (255, 0, 0),   # RED
    4: (0, 255, 0),   # GREEN
    5: (0, 0, 225),   # BLUE
    6: (255, 255, 0),   # YELLOW
    7: (0, 255, 255),    # CYAN
    8: (255, 0, 255),    # MAGENTA
    9: (128, 0, 128),    # PURPLE
    10: (128, 128, 128)  # GRAY
}



pensize = 2  # radius of circle
sel_color = 1  # from colors