import pygame

class Text(pygame.sprite.Sprite):

    
    def __init__(self, x, y, text, color = (0, 0, 0) , font_size = 22):
        """
        Set up the texts displayed in the app
        param x: x coordinate of the text
        param y: y coordinate of the text
        param text: text that needs to be displayed
        param color: color of the font
        param font_size: font size
        return: None
        """
        pygame.sprite.Sprite.__init__(self)
        pygame.font.init()
        self.x = x
        self.y = y
        self.user_text = text
        self.base_font = pygame.font.SysFont("bahnschrift", font_size)
        self.text_surface = self.base_font.render(self.user_text, True, color)
