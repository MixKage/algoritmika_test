
import pygame, time
import settings


class TextArea():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color 
    
    def set_text(self, text, fsize=64, text_color=(0,0,0)):
        self.text = text
        self.image = pygame.font.Font(None, fsize).render(text, True, text_color)
    
    def draw_text(self, screen, shift_x=0, shift_y=0):
        pygame.draw.rect(screen, self.fill_color, self.rect)
        screen.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))
        
class Button():
    def __init__(self, image, x=settings.sc_width//4, y=settings.sc_height//4):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.handled = False
    
    def draw(self, screen):
        mpos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mpos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True

        # Draw Button On Screen 
        screen.blit(self.image, (self.rect.x, self.rect.y))
    
    def startTimer(self):
        if not self.handled: 
            self.start_timer = time.time(); self.handled = True

