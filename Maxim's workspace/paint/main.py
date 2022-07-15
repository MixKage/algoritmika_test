
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


import pygame, sys
import cfg, paint

pygame.init()
pygame.font.init()

sc = pygame.display.set_mode(cfg.screen_size)
pygame.display.set_caption("Paint")
sc.fill(cfg.colors[2])


while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                cfg.pensize += 1
                if cfg.pensize >= 20: cfg.pensize = 1
                print(f"\nSize now - {cfg.pensize}\nMax - 20, Min - 1")
            elif event.key == pygame.K_DOWN:
                cfg.pensize -= 1 
                if cfg.pensize <= 0: cfg.pensize = 20
                print(f"\nSize now - {cfg.pensize}\nMax - 20, Min - 1")
            elif event.key == pygame.K_m:
                if cfg.bool == True: cfg.pensize = 20; print(f"\nSize now - {cfg.pensize}\nMax - 20, Min - 1"); bool = False
                else: cfg.pensize = 1; print(f"\nSize now - {cfg.pensize}\nMax - 20, Min - 1"); bool = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (x, y) = pygame.mouse.get_pos()       # returns the position of mouse cursor
            paint.drawCircle(sc, x,y, cfg.colors[cfg.sel_color], cfg.pensize)
            cfg.isMousePressed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            cfg.isMousePressed = False
        elif event.type == pygame.MOUSEMOTION and cfg.isMousePressed == True:         
            (x, y) = pygame.mouse.get_pos()       # returns the position of mouse cursor
            paint.drawCircle(sc, x,y, cfg.colors[cfg.sel_color], cfg.pensize)
    paint.drawCircle(sc, 40, 40, cfg.colors[cfg.sel_color], 20)
    sc.blit(paint.showText(cfg.pensize, 1, cfg.colors[1]), (50,40))
    pygame.display.update()


    