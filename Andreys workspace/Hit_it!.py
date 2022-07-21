from turtle import *
from time import *

score = 0

dist1 = 0
dist2 = 0
dist3 = 0

class Sprite(Turtle):
    def start(self, shapex, colorx, x_point, y_point):
        self.step = 10
        self.shape(shapex)
        self.color(colorx)
        self.goto(x_point, y_point)
        self.speed(0)

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
t1.step = 25

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

t5 = Sprite()
t5.penup()
t5.start('circle', 'red', 100, 100)

scr = Screen()
scr.listen()
t1.getscreen()

scr.onkey(t1.move_forward, 'w')
scr.onkey(t1.move_back, 's')
scr.onkey(t1.move_right, 'd')
scr.onkey(t1.move_left, 'a')

while True:
    dist1 = t1.distance(t2.xcor(), t2.ycor())
    dist2 = t1.distance(t3.xcor(), t3.ycor())
    dist3 = t1.distance(t4.xcor(), t4.ycor())
    if dist1 <= 20 or dist2 <= 20:
        t1.hideturtle()
        break
    elif dist3 <= 5:
        t1.goto(0, -75)
        score += 1
        sleep(0.1)
    if score == 0:
        t5.color('red')
    elif score == 1:
        t5.color('yellow')
    elif score == 2:
        t5.color('orange')
    elif score >= 3:
        t5.color('green')
        t2.hideturtle()
        t3.hideturtle()
        break
    
    t2.set_move()
    t2.make_step()
    t3.set_move()
    t3.make_step()
    sleep(0.1)

input('yay')
