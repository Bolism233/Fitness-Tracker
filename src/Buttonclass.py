import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self):
        super.__init__(self)
        self.image = pygame.image.load("assets/calculateButton.jpg")
        self.rect = self.image.get_rect()
        self.rect.x = 450
        self.rect.y = 500

