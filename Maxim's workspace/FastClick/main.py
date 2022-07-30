#### Imports ####
from pick import pick
import pygame as pg
import settings, other
import random, time

pg.init()


sc = pg.display.set_mode((settings.scWidth, settings.scHeight))
clock = pg.time.Clock()

def main():
    running = True
    play = False
    settingsOn = False
    handled = False
    points = 0
    wait = 0
    x = settings.scWidth - 120

    pg.display.set_caption(settings.title)

    

    cardList = []

    timeText = other.Label(sc, 20, 20)
    timeText.rect.width = 0; timeText.rect.height = 0
    timeText.setColor((0,0,0))

    pointsText = other.Label(sc, settings.scWidth-120, 20)
    pointsText.rect.width = 0; pointsText.rect.height = 0
    pointsText.setColor((0,0,0))


    playButton = other.Label(sc, 40, 60)
    playButton.rect.width = 350; playButton.rect.height = 80
    playButton.setColor(settings.buttonColor); playButton.set_text("Play", 80)

    settingsButton = other.Label(sc, 40, 160)
    settingsButton.rect.width = 350; settingsButton.rect.height = 80
    settingsButton.setColor(settings.buttonColor); settingsButton.set_text("Settings", 80)

    quitButton = other.Label(sc, 40, 260)
    quitButton.rect.width = 350; quitButton.rect.height = 80
    quitButton.setColor(settings.buttonColor); quitButton.set_text("Quit", 80)

    pickWhite = other.Area(sc, settings.scWidth//8, settings.scHeight//1.5, 100, 100, settings.bgWhiteColor); pickWhite.setColor(settings.bgWhiteColor)
    pickBlue = other.Area(sc, settings.scWidth//2, settings.scHeight//1.5, 100, 100, settings.bgPurpleColor); pickBlue.setColor(settings.bgPurpleColor)

    start = time.time()

    for i in range(4):
        # x: 380, 280, 180, 80
        card = other.Label(sc, x)
        card.setColor(settings.cardColorIn)
        card.set_text("Click!", 20, (255,0,0))
        
        cardList.append(card)
        x -= 100

    while running:
        mpos = pg.mouse.get_pos()

        for event in pg.event.get():
            if event.type == pg.QUIT: running = False
                
        sc.fill(settings.bgColor)

        if play:       
            for i in cardList:
                i.colorFill()
                i.setOutline(settings.cardColorOut)
                    
            if (time.time()-start) <= 10: 
                click = random.randint(0,3)
                cardList[click].draw(7,30)
                pointsText.set_text(f"Clicks: {points}", 32)
                pointsText.draw()
                timeText.set_text(f"Time: {int(time.time()-start)}", 32)
            else:
                if points < 10: 
                    timeText.rect.x = settings.scWidth//3.5
                    timeText.rect.y = settings.scHeight//4
                    timeText.set_text("Game Over", 62); pointsText.set_text("")
                    for i in cardList:
                        i.set_text("?", 64, (255,0,0))
                        i.draw(15,20)
                    playButton.set_text("Not Active", 80)
                    running = False
                else: 
                    timeText.rect.x = settings.scWidth//3
                    timeText.rect.y = settings.scHeight//3.5
                    timeText.set_text("You WIN!", 62, (255,0,0)); pointsText.set_text("")
                    for i in cardList:
                        i.set_text("$", 64, (50,255,0))
                        i.draw(14,20)
                    playButton.set_text("Not Active", 80)
                    play = False
            
            
            if pg.mouse.get_pressed()[0] and cardList[click].rect.collidepoint(mpos) and not handled and points <= 10:
                points += 1
                print("Clicked!")
                handled = True
            elif not pg.mouse.get_pressed()[0] and handled: handled = False

            timeText.draw()

        else: 
            if not settingsOn: settingsButton.draw(10,10); playButton.draw(10,10); quitButton.draw(10, 10)

            if pg.mouse.get_pressed()[0] and not handled:            
                if playButton.rect.collidepoint(mpos): play = True; settingsOn = False
                if settingsButton.rect.collidepoint(mpos):
                    settingsOn = True
                if quitButton.rect.collidepoint(mpos): running = False

                if pickWhite.rect.collidepoint(mpos) and not handled: settings.bgColor = settings.bgWhiteColor; settingsOn = False
                if pickBlue.rect.collidepoint(mpos) and not handled: settings.bgColor = settings.bgPurpleColor; settingsOn = False
                handled = True
            elif not pg.mouse.get_pressed()[0]: handled = False
                

            if settingsOn: 
                pickWhite.colorFill(); pickBlue.colorFill()
                pickWhite.setOutline((0,0,0)); pickBlue.setOutline((0,0,0))

            

                    

        
        

        

        clock.tick(settings.fps)
        pg.display.update()
    

    exit()

    

    

if __name__ == "__main__":
    main()