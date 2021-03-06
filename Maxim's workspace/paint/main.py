
#                                      ___      
#                     .-.             (   )     
#    .-..     .---.  ( __)  ___ .-.    | |_     
#   /    \   / .-, \ (''") (   )   \  (   __)   
#  ' .-,  ; (__) ; |  | |   |  .-. .   | |      
#  | |  . |   .'`  |  | |   | |  | |   | | ___  
#  | |  | |  / .'| |  | |   | |  | |   | |(   ) 
#  | |  | | | /  | |  | |   | |  | |   | | | |  
#  | |  ' | ; |  ; |  | |   | |  | |   | ' | |  
#  | `-'  ' ' `-'  |  | |   | |  | |   ' `-' ;  
#  | \__.'  `.__.'_. (___) (___)(___)   `.__.   
#  | |                                          
# (___)  


from turtle import pensize
import pygame, sys
import cfg, paint

# INITS
pygame.init()

sc = pygame.display.set_mode((cfg.weight, cfg.height))
pygame.display.set_caption("Paint")   # TITLE
# pygame.display.set_icon(cfg.icon)   NOT WORKING
sc.fill(cfg.colors[10])  # BACKGROUND
pygame.mouse.set_visible(False)
print(cfg.keybinds)


i = 0
while True:  # MAIL LOOP
    for event in pygame.event.get():  # MAIN EVENT CHECKER
        if event.type == pygame.QUIT: sys.exit()  # EXIT

        elif event.type == pygame.KEYDOWN:  # WHEN PRESSED ANY KEY

            if event.key == pygame.K_UP:  # +1 SIZE (MAX - 20, MIN - 1)
                cfg.pensize += 1
                if cfg.pensize >= 20: cfg.pensize = 1
                print(f"\nSize now - {cfg.pensize}\nMax - 20, Min - 1")

            elif event.key == pygame.K_DOWN:  # -1 SIZE (MAX - 20, MIN - 1)
                cfg.pensize -= 1 
                if cfg.pensize <= 0: cfg.pensize = 20
                print(f"\nSize now - {cfg.pensize}\nMax - 20, Min - 1")

            elif event.key == pygame.K_m:  # MIN SIZE OR MAX SIZE TURN
                if cfg.min_or_max == True: cfg.pensize = 20; print(f"\nSize now - {cfg.pensize}\nMax - 20, Min - 1"); cfg.min_or_max = False
                else: cfg.pensize = 1; print(f"\nSize now - {cfg.pensize}\nMax - 20, Min - 1"); cfg.min_or_max = True

            elif event.key == pygame.K_LEFT:  # BACKWARD COLOR
                cfg.sel_color -= 1
                if cfg.sel_color < 1: cfg.sel_color = len(cfg.colors)-1

            elif event.key == pygame.K_RIGHT:  # NEXT COLOR
                cfg.sel_color += 1
                if cfg.sel_color == len(cfg.colors): cfg.sel_color = 1
            
            elif event.key == pygame.K_e: # EARSER
                if cfg.bool == False: print(f"\nEarser {cfg.bool}"); cfg.sel_color = 1; cfg.bool = True
                else: print(f"\nEarser {cfg.bool}"); cfg.sel_color = len(cfg.colors); cfg.bool = False; 
            
            elif event.key == pygame.K_SPACE:  # EARSE ALL
                pygame.draw.rect(sc, cfg.colors[len(cfg.colors)], [0,0, cfg.weight, cfg.height])
                print("\nEarsed All")


        elif event.type == pygame.MOUSEBUTTONDOWN:
            (x, y) = pygame.mouse.get_pos()       # returns the position of mouse cursor
            paint.drawCircle(sc, x,y, cfg.colors[cfg.sel_color], cfg.pensize)
            cfg.isMousePressed = True

        elif event.type == pygame.MOUSEBUTTONUP:
            cfg.isMousePressed = False

        elif event.type == pygame.MOUSEMOTION and cfg.isMousePressed == True:         
            (x, y) = pygame.mouse.get_pos()       # returns the position of mouse cursor
            paint.drawCircle(sc, x,y, cfg.colors[cfg.sel_color], cfg.pensize)
            # paint.drawAline(sc, cfg.colors[cfg.sel_color], x,y)
    if i == 50000:
        print(cfg.keybinds)
        i=0
    paint.drawCircle(sc, cfg.weight//15, cfg.height//15, cfg.colors[cfg.sel_color], cfg.radius)  # 40, 40
    coord = pygame.mouse.get_pos()
    sc.blit(sc, pygame.draw.circle(sc, (cfg.colors[1]), coord, cfg.pensize))
    # sc.blit(paint.showText(cfg.pensize, 1, cfg.colors[1]), (50,40))
    pygame.display.update()
    i+=1

    