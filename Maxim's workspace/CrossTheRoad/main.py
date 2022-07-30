
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





# cfg.text(text, "Hello! It's my new game.\n     Cross The Road", "red", "center", "Arial", 36, "bold")

player = cfg.Sprite(0,-cfg.height//2, "circle", "orange")
enemy1 = cfg.Sprite(-cfg.weight, 0, 'square', cfg.randomСolor(), 15)
enemy2 = cfg.Sprite(cfg.weight, 70, 'square', cfg.randomСolor(), 15)
goal = cfg.Sprite(0, cfg.height, 'triangle', 'green', 20)
 
scr = player.getscreen()
scr.listen()
scr.onkey(player.move_up, 'Up')
scr.onkey(player.move_left, 'Left')
scr.onkey(player.move_right, 'Right')
scr.onkey(player.move_down, 'Down')



while cfg.total_score < 3:
    if player.is_collide(goal): player.goto(cfg.start_pos); cfg.total_score += 1
    elif player.is_collide(enemy1) or player.is_collide(enemy2): goal.hideturtle(); break

#  -------- Other --------
turtle.exitonclick()