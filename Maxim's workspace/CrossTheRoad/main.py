
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


player = turtle.Turtle(visible=False, shape="square")
player.speed(100)
player.color(cfg.colors[1]); player.fillcolor(cfg.colors[1])
player.penup(); player.goto(0, -cfg.height//2); player.pendown()

t1 = turtle.Turtle(visible=False, shape="turtle")
t1.color(cfg.randomСolor()); t1.fillcolor(cfg.randomСolor())





#  -------- Other --------
turtle.exitonclick()