
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
import cfg


#  -------- Turtles --------
turtle.colormode(255)

line = turtle.Turtle()
line.speed(0); line.hideturtle(); line.pensize(1)
line.penup(); line.goto(cfg.x,cfg.y); line.pendown()
for i in range(50):
    line.forward(1000)
    cfg.y += 20
    line.penup(); line.goto(cfg.x,cfg.y); line.pendown()

player = turtle.Turtle(shape="square")
player.speed(0); # player.hideturtle()
player.color(cfg.colors[1]); player.fillcolor(cfg.colors[1])
player.penup(); player.goto(0, -cfg.height+50); player.pendown()
player.shapesize(1,1,5)

text = turtle.Turtle()
text.speed(0); text.hideturtle()

goal = turtle.Turtle(shape="square")
goal.color(cfg.colors[0]); goal.fillcolor(cfg.randomСolor())
goal.speed(0); # goal.hideturtle()
goal.penup(); goal.goto(0, cfg.height-50); goal.pendown()
goal.shapesize(2,2,1)



# cfg.text(text, "Hello! It's my new game.\n     Cross The Road", "red", "center", "Arial", 36, "bold")



t1 = turtle.Turtle(shape="turtle")
t1.hideturtle()
t1.color(cfg.randomСolor()); t1.fillcolor(cfg.randomСolor())



#  -------- Other --------
turtle.exitonclick()