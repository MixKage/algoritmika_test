
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
weight = 800 # WEIGHT
height = 800 # HEIGHT
#  icon = pygame.image.load("algoritmika_test\Maxim's workspace\paint\logo.jpg")

# Variables
pensize = 2  # radius of circle
sel_color = 1  # from colors
radius = 20


# BOOLS
min_or_max = False  # pensize
bool = True  # Useful bool, just bool
isMousePressed = False  # MousePressed

keybinds = """
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
E - Earser
Space - Earse All
M - Minimum/Maximum Size

Left, Right - Color change
Up, Down - Size change
"""

colors = {
    1: (0, 0, 0),   # BLACK
    2: (255, 0, 0),   # RED
    3: (0, 255, 0),   # GREEN
    4: (0, 0, 225),   # BLUE
    5: (255, 255, 0),   # YELLOW
    6: (0, 255, 255),    # CYAN
    7: (255, 0, 255),    # MAGENTA
    8: (128, 0, 128),    # PURPLE
    9: (128, 128, 128),  # GRAY
    10: (255, 255, 255)   # WHITE
}



