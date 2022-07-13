import turtle
import time
import random

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()

points = 0

w = 200
h = 200

def turtle_parameters():
    t1.color("blue")
    t1.fillcolor("gray")
    t1.shape("turtle")
    t1.speed(5)
    t1.left(135)
    

    t2.color("red")
    t2.fillcolor("gray")
    t2.shape("turtle")
    t2.speed(5)
    t2.left(90)

    t3.color("green")
    t3.fillcolor("gray")
    t3.shape("turtle")
    t3.speed(5)
    t3.left(25)

turtle_parameters()
def turtlclick(t):
    global points
    points += 1
    if points == 10:
        gameFinished(t)
    t.penup()
    t.goto(random.randint(-w, w), random.randint(-h, h))
    t.pendown()
    num = random.randint(1,2)
    if num == 1:
        t.left(90)
    elif num == 2:
        t.right(90)

def gameFinished(t):
    if abs(t.xcor()) >= w or abs(t.ycor()) >= h:
        t.write("GAME OVER", font=("Arial", 17, "bold"))
        return True
    

t1.onclick(turtlclick(t1))
t2.onclick(turtlclick(t2))
t3.onclick(turtlclick(t3))

while True:
    t1.forward(10)
    gameFinished(t1)
    t2.forward(10)
    gameFinished(t2)
    t3.forward(10)
    gameFinished(t3)
    if gameFinished(t1) or gameFinished(t2) or gameFinished(t3):
        break

