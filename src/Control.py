import pygame
from src.Buttonclass import Button
from src.Textbox import Textbox


class Controller:
    def __init__(self, width = 900, height = 500):
        pygame.init()
        #Set up screen
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Fitness Tracker Demo")
        self.screen.fill((202, 229, 241))
        #set up buttons
        self.start_button = Button (300, 300, "assets/start_btn.png", 0.25)
        self.exit_button = Button (500, 300, "assets/exit_btn.png", 0.25)
        self.buttons = pygame.sprite.Group()
        self.buttons.add(self.start_button, self.exit_button)
        #set up textboxes
        self.textbox1 = Textbox(300, 250, "Nerd Simulator")
        self.screen.blit(self.textbox1.text_surface, (self.textbox1.x,self.textbox1.y))

    def mainloop(self):
        run = True
        #self.btn(start_button, 100, 200, self.btn_image, 0.25)
        #self.btn(exit_button, 500, 200, self.btn_image, 0.25)
        while run:
            self.buttons.draw(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                pos = pygame.mouse.get_pos()
                # if event.type == pygame.MOUSEMOTION: Button zoom in when mouse hovering
                #     if self.start_button.rect.collidepoint(pos):
                #         self.start_button.zoomin()
                #     elif self.start_button.rect.collidepoint(pos):
                #         self.start_button.zoomout()
                #     elif self.exit_button.rect.collidepoint(pos):
                #         self.exit_button.zoomin()
                #     elif self.exit_button.rect.collidepoint(pos):
                #         self.exit_button.zoomout()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_button.rect.collidepoint(pos): #Check if its clicked on the buttons
                        print("Good")
                    elif self.exit_button.rect.collidepoint(pos):
                        print("Bye")
                        run = False





                # if event.type == pygame.KEYDOWN:
                #     if event.key == pygame.K_DOWN:
                #         start_button.rect.x -=1
                #         screen.blit(start_button.image, (start_button.rect.x, start_button.rect.y))

            pygame.display.update()
        pygame.quit()