import pygame
from src.Buttonclass import Button

class Controller:
    def __init__(self, w, d):
        self.width= w
        self.height = d
        win = pygame.display.set_mode((self.width, self.height))
        green = Button
        pygame.display.set_caption("Shooter")
        pygame.display.update()

    def mainloop(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
        pygame.quit()

