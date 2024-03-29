import pygame

class Textbox(pygame.sprite.Sprite):


    def __init__(self, x, y, user_text = ''):
        pygame.sprite.Sprite.__init__(self)
        pygame.font.init()
        self.black = (0, 0 ,0)
        self.white = (255, 255, 255)
        font_size = 22
        self.x = x
        self.y = y
        self.user_text = user_text
        self.base_font = pygame.font.Font(None, font_size)
        self.text_surface = self.base_font.render(self.user_text, True, self.white)
        self.input_rect = pygame.Rect(self.x, self.y, 140, 32)
        self.active = False # whether it is clicked on or not.


    def setDefaultLen(self):
        """
        Set the default length of the texboxes
        :params: None
        :return: None
        """
        self.input_rect.w = max(140, self.text_surface.get_width() + 20)
