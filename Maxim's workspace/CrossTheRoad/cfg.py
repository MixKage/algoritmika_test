
#     $$$$$$\                                                $$$$$$$$\ $$\                       $$$$$$$\                            $$\ 
#   $$  __$$\                                               \__$$  __|$$ |                      $$  __$$\                           $$ |
#   $$ /  \__| $$$$$$\   $$$$$$\   $$$$$$$\  $$$$$$$\          $$ |   $$$$$$$\   $$$$$$\        $$ |  $$ | $$$$$$\   $$$$$$\   $$$$$$$ |
#   $$ |      $$  __$$\ $$  __$$\ $$  _____|$$  _____|         $$ |   $$  __$$\ $$  __$$\       $$$$$$$  |$$  __$$\  \____$$\ $$  __$$ |
#   $$ |      $$ |  \__|$$ /  $$ |\$$$$$$\  \$$$$$$\           $$ |   $$ |  $$ |$$$$$$$$ |      $$  __$$< $$ /  $$ | $$$$$$$ |$$ /  $$ |
#   $$ |  $$\ $$ |      $$ |  $$ | \____$$\  \____$$\          $$ |   $$ |  $$ |$$   ____|      $$ |  $$ |$$ |  $$ |$$  __$$ |$$ |  $$ |
#   \$$$$$$  |$$ |      \$$$$$$  |$$$$$$$  |$$$$$$$  |         $$ |   $$ |  $$ |\$$$$$$$\       $$ |  $$ |\$$$$$$  |\$$$$$$$ |\$$$$$$$ |
#    \______/ \__|       \______/ \_______/ \_______/          \__|   \__|  \__| \_______|      \__|  \__| \______/  \_______| \_______|


#  -------- All Imports --------
import random, time
import turtle
import numpy as np


#  -------- Colors --------
colors = [
    "black",
    "red",
    "lightred",
    "green",
    "blue",
    "yellow",
    "cyan",
    "magenta",
    "purple",
    "gray",
    "white"
]


#  -------- Variables --------
weight = 400
height = 400


#  -------- All Functions --------
def randomСolor():
    return list(np.random.choice(range(256), size=3))


#  -------- Classes --------
class createTurtle:
    def __init__(self, color, shape, name, fillcolor):
        name = turtle.Turtle(visible=False)
        name.shape(shape)
        name.color(color)
        name.fillcolor(fillcolor)