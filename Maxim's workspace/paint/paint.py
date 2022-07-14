#   -- IMPORTS --
import pygame as pg
import sys
import cfg

pg.init()

sc = pg.display.set_mode((1000, 900))
sc.fill(cfg.WHITE)
pg.display.update()
 
pg.mouse.set_visible(False)  
 
clock = pg.time.Clock()   # FPS 

while True:  # Главный цикл
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            pos = pg.mouse.get_pos()
            pg.draw.rect(sc, cfg.BLACK, (pos[0] - 10, pos[1] - 10, 20, 20))
 
    sc.fill(cfg.WHITE)
 
    if pg.mouse.get_focused():
        pos = pg.mouse.get_pos()
        pg.draw.rect(
            sc, cfg.BLUE, (pos[0] - 2.5,
                           pos[1] - 2.5,
                           5, 5))


    pg.display.update()
    clock.tick(cfg.FPS)