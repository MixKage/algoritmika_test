##### IMPORTS #####
import pygame
import settings, classes
import random, time
pygame.init()  # Important Thing


clock = pygame.time.Clock()
sc = pygame.display.set_mode((settings.sc_width, settings.sc_height))
title = "Reaction Game"


def main():
    pygame.display.set_caption(title)  # Window Name

    # Variables
    running = True
    started_timer = False
    wait = random.randint(100, 600)
    # Create Examples of Classes
    time_text = classes.TextArea(x=settings.sc_width//2.5, y=settings.sc_height//6, color=settings.bg)
    red_button = classes.Button(settings.rb_img)
    green_button = classes.Button(settings.gb_img)

    # Start Timer

    while running:  # Main Loop
        for event in pygame.event.get():   # Event Handler
            if event.type == pygame.QUIT: running = False  # Quit Game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q: started = True

        
        sc.fill(settings.bg)
        
        if wait <= 0:
            green_button.draw(sc)
            if not started_timer: start = time.time(); started_timer = True
            if not green_button.clicked: time_text.set_text(f"{round(time.time()-start, 3)}"); 
            
        else:         
            red_button.draw(sc)
            time_text.set_text("0.000")
            wait -= 1

        time_text.draw_text(sc)

        
    
        clock.tick(settings.FPS)
        pygame.display.update()  # Update every loop something
        
    
    pygame.quit()  # Close Window

if __name__ == "__main__":  
    main()