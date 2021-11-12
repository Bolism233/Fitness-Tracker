import pygame

class Text(pygame.sprite.Sprite):
    def __init__(self, x, y, text, color = (0, 128, 255) , font_size = 22):
        pygame.sprite.Sprite.__init__(self)
        pygame.font.init()
        self.x = x
        self.y = y
        self.user_text = text
        self.base_font = pygame.font.SysFont("comicsans", font_size)
        self.text_surface = self.base_font.render(self.user_text, True, color)