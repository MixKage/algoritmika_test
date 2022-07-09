from turtle import*


def paint_color_box(color_string, width, heigh):
    pendown()
    color(color_string)
    begin_fill()
    for i in range(2):
        forward(width)
        right(90)
        forward(heigh) 
        right(90)       
    end_fill()
    penup()

speed(100)
penup()
# paint_sky
goto(-200,200)
paint_color_box("blue", 400, 200)
# paint_gress
goto(-200,0)
paint_color_box("green", 400, 200)
# paint_houses
for i in range(3):
    goto(-80 * i+1,80)
    paint_color_box("gray", 60, 120)    
    # # paint_windows    
    for l2 in range(2):                        
        goto(-80 * i+1 + 20, 70 // (l2+1))
        paint_color_box("yellow", 20,20)
hideturtle()
exitonclick()