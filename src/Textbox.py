import pygame


class Textbox:
    def __init__(self, user_input, surface, coord):
        base_font = pygame.font.Font(None, 32)
        user_text = user_input
        text_surface = base_font.render(user_text, True, (255,255,255)) #.render text, anti-alias, color
        surface.blit(text_surface, (0,0))
