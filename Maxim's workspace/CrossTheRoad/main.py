
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


player = turtle.Turtle(shape="square")
player.hideturtle(); player.speed(0)
player.color(cfg.colors[1]); player.fillcolor(cfg.colors[1])
player.penup(); player.goto(0, -cfg.height//2); player.pendown()

text = turtle.Turtle()
text.speed(0); text.hideturtle()

cfg.text(text, "Hello! It's my new game.\n     Cross The Road", "red", "center", "Arial", 36, "bold")

t1 = turtle.Turtle(shape="turtle")
t1.hideturtle()
t1.color(cfg.randomСolor()); t1.fillcolor(cfg.randomСolor())



#  -------- Other --------
turtle.exitonclick()