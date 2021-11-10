import pygame
from src.Buttonclass import Button

class Controller:
    def __init__(self, width, height):
        #Set up screen
        self.screen_width = width
        self.screen_height = height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Fitness Tracker Demo")
        #set up buttons
        self.startbtn_image = pygame.image.load("assets/start_btn.png")
        self.exitbtn_image = pygame.image.load("assets/exit_btn.png")
        self.start_button = Button (300, 300, self.startbtn_image, 0.25)
        self.exit_button = Button (500, 300, self.exitbtn_image, 0.25)

        #Set up textboxes

    # def btn(self, nam, x,y, image, scale):
    #     name = Button(x, y, image, scale)
    #     name = Button(x, y, image, scale)

    def mainloop(self):
        run = True
        #self.btn(start_button, 100, 200, self.btn_image, 0.25)
        #self.btn(exit_button, 500, 200, self.btn_image, 0.25)
        while run:
            self.screen.fill((202, 229, 241))
            if self.start_button.draw(self.screen):
                print("Start")
            if self.exit_button.draw(self.screen):
                run = False
                #print("Exit")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                # if event.type == pygame.KEYDOWN:
                #     if event.key == pygame.K_DOWN:
                #         start_button.rect.x -=1
                #         screen.blit(start_button.image, (start_button.rect.x, start_button.rect.y))

            pygame.display.update()
        pygame.quit()