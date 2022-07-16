from turtle import *

t = Turtle()
t.color('blue')
t.shape('circle')
t.speed(10)
t.pensize(2)

ind = Turtle()
ind.color('black')
ind.shape('circle')
ind.penup()
ind.goto(-300, 300)

scr = Screen()
scr.listen()
t.getscreen()

step = 15
pen = 3

def draw(x, y):
    t.goto(x, y)

def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def up():
    t.goto(t.xcor(), t.ycor() + step)
 
def down():
    t.goto(t.xcor(), t.ycor() - step)
 
def left():
    t.goto(t.xcor() - step, t.ycor())
 
def right():
    t.goto(t.xcor() + step, t.ycor())


def red():
    t.color('red')

def blue():
    t.color('blue')

def violet():
    t.color('violet')

def green():
    t.color('green')

def gray():
    t.color('gray')

def yellow():
    t.color('yellow')

def black():
    t.color('black')


def fill_end():
    t.end_fill()
    ind.color('lightblue')

def fill_begin():
    t.begin_fill()
    ind.color('crimson')


def draw_circle():
    t.circle(50)

def draw_kvadrat():
    for i in range(4):
        t.forward(80)
        t.left(90)

def draw_pramougolnik():
    for i in range(2):
        t.forward(160)
        t.left(90)
        t.forward(80)
        t.left(90)

def draw_treugolnik():
    for i in range(3):
        t.forward(100)
        t.left(120)


scr.onscreenclick(move)
scr.onkey(up, 'Up')
scr.onkey(down, 'Down')
scr.onkey(right, 'Right')
scr.onkey(left, 'Left')

scr.onkey(red, 'r')
scr.onkey(blue, 't')
scr.onkey(black, 'y')
scr.onkey(violet, 'u')
scr.onkey(yellow, 'i')
scr.onkey(gray, 'o')
scr.onkey(green, 'p')

scr.onkey(fill_begin, 'q')
scr.onkey(fill_end, 'w')

scr.onkey(draw_circle, 'a')
scr.onkey(draw_kvadrat, 's')
scr.onkey(draw_pramougolnik, 'd')
scr.onkey(draw_treugolnik, 'f')


t.ondrag(draw)

input()
