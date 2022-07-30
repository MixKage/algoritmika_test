
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


#  -------- Variables --------
weight = 200
height = 150

start_pos = (0, -height//2)

total_score = 0


#  -------- All Functions --------
def randomСolor(): #  Random Rgb Color
    return list(np.random.choice(range(256), size=3))


#  -------- Classes --------
class Sprite(turtle.Turtle):
    def __init__(self, x,y, shape="square", color=randomСolor(), step=10):
        super().__init__()
        self.speed(0)
        self.penup()
        self.goto(x,y)
        self.shape(shape)
        self.color(color)
        self.step = step

    def text(self, text, color="Black", align="Center", font="Arial", size=32, type="normal"):  #  Show text by Turtle
        self.color(color)
        self.write(text,align=align,font=(font, size, type))
    
    def move_up(self):
        self.goto(self.xcor(), self.ycor() + self.step)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - self.step)

    def move_left(self):
        self.goto(self.xcor() - self.step, self.ycor())

    def move_right(self):
        self.goto(self.xcor() + self.step, self.ycor())

    def is_collide(self,object):
        return self.distance(object.xcor(), object.ycor()) < 30

    