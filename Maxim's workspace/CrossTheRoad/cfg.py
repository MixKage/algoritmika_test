
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
x = -500
y = -500

#  -------- All Functions --------
def randomСolor(): #  Random Rgb Color
    return list(np.random.choice(range(256), size=3))

def text(name, text, color, align, font, size, type):  #  Show text by Turtle
    name.color(color)
    name.write(text,align=align,font=(font, size, type))


#  -------- Classes --------
class createTurtle:
    def __init__(self, color, shape, name, fillcolor):
        name = turtle.Turtle(visible=False)
        name.shape(shape)
        name.color(color)
        name.fillcolor(fillcolor)