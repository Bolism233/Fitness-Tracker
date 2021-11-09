import pygame


class Button(pygame.Sprite.Sprite):
    def __init__(self):
        super.__init__(self)
        self.inputbox = pygame.Rect(100, 100, 140, 32)
        self.color_inactive = self.inputbox.Color("lightskyblue3")
        self.color_active = self.inputbox.Color("dodgerblue2")


    def input(self):
