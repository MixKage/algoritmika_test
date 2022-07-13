# import queue
# import pygame

# pygame.init()

# sc = pygame.display.set_mode((1000, 500))

# clock = pygame.time.Clock()

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             quit()
    
#     pygame.draw.arc(sc, (255, 0 ,0), 50, 2, 5)

#     pygame.display.flip()
#     clock.tick(30)

import turtle


t1 = turtle.Turtle()
t1.color("red")
t1.pensize(2) 
t1.left(130)
t1.penup()
t1.goto(0,-200)
t1.pendown()

t2 = turtle.Turtle()
t2.color("red")
t2.pensize(2)
t2.left(10)
t2.penup()
t2.goto(0,-200)
t2.pendown()

t1.begin_fill()
t2.begin_fill()
for i in range(20):
    t1.right(2)
    t2.left(2)
    t1.forward(5)
    t2.forward(5)
for i in range(28):
    t1.right(5)
    t2.left(5)
    t1.forward(2)
    t2.forward(2)

t1.forward(35)
t2.forward(35)

t1.end_fill()
t2.end_fill()

turtle.hideturtle()
turtle.exitonclick()
