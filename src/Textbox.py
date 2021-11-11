import pygame


class Textbox(pygame.sprite.Sprite):
    def __init__(self, x, y, user_text = ''):
        pygame.sprite.Sprite.__init__(self)
        pygame.font.init()
        self.x = x
        self.y = y
        base_font = pygame.font.Font(None,50)
        self.text_surface = base_font.render(user_text, True, (0,0,0))
