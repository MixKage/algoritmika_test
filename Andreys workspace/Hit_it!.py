from turtle import *
from time import *

class Sprite(Turtle):
    def start(self, shapex, colorx, x_point, y_point):
        self.step = 10
        self.shape(shapex)
        self.color(colorx)
        self.goto(x_point, y_point)

    def set_move(self):
        if self.xcor() >= 100:
            self.step = -10
        elif self.xcor() <= -100:
            self.step = 10

    def make_step(self):
        self.goto(self.xcor() + self.step, self.ycor())

    def move_forward(self):
        self.goto(self.xcor(), self.ycor() + self.step)

    def move_back(self):
        self.goto(self.xcor(), self.ycor() - self.step)

    def move_right(self):
        self.goto(self.xcor() + self.step, self.ycor())

    def move_left(self):
        self.goto(self.xcor() - self.step, self.ycor())


t1 = Sprite()
t1.penup()
t1.start('circle', 'blue', 0, -75)

t2 = Sprite()
t2.penup()
t2.start('square', 'red', -100, -25)

t3 = Sprite()
t3.penup()
t3.start('square', 'red', 100, 25)

t4 = Sprite()
t4.left(90)
t4.penup()
t4.start('triangle', 'green', 0, 75)

scr = Screen()
scr.listen()
t1.getscreen()

scr.onkey(t1.move_forward, 'w')
scr.onkey(t1.move_back, 's')
scr.onkey(t1.move_right, 'd')
scr.onkey(t1.move_left, 'a')

while True:
    t2.set_move()
    t2.make_step()
    t3.set_move()
    t3.make_step()
    sleep(0.1)