import pygame
from src.Buttonclass import Button
from src.Textbox import Textbox


class Controller:
    def __init__(self, width = 900, height = 500):
        self.clock = pygame.time.Clock()
        pygame.init()
        pygame.font.init()
        #Set up screen
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Fitness Tracker Demo")
        self.screen.fill((202, 229, 241))
        #set up buttons
        self.start_button = Button (300, 400, "assets/start_btn.png", 0.25)
        self.exit_button = Button (500, 400, "assets/exit_btn.png", 0.25)
        self.buttons = pygame.sprite.Group() #button sprite group
        self.buttons.add(self.start_button, self.exit_button)
        #set up textboxes
        self.textbox1 = Textbox(150, 150, "")
        self.textbox2 = Textbox(350, 150, "")
        self.textbox3 = Textbox(550, 150, "")
        self.textbox4 = Textbox(150, 300, "")
        self.textbox5 = Textbox(350, 300, "")
        self.textbox6 = Textbox(550, 300, "")
        self.textboxes = pygame.sprite.Group() # textbox sprite group
        self.textboxes.add(self.textbox1, self.textbox2, self.textbox3, self.textbox4, self.textbox5, self.textbox6)
        # for textbox in self.textboxes:
        #     pygame.draw.rect(self.screen, (255,255,255), textbox.input_rect, 2)
        #     self.screen.blit(textbox.text_surface, (textbox.x, textbox.y ))

    def mainloop(self):
        run = True

        while run:
            self.buttons.draw(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_button.rect.collidepoint(event.pos): #Check if its clicked on the buttons
                        print("Good")
                    elif self.exit_button.rect.collidepoint(event.pos):
                        print("Bye")
                        run = False
                    #textbox selection need to be optimized
                    elif self.textbox1.input_rect.collidepoint(event.pos):
                        for textbox in self.textboxes:
                            textbox.active = False
                        self.textbox1.active = True
                    elif self.textbox2.input_rect.collidepoint(event.pos):
                        for textbox in self.textboxes:
                            textbox.active = False
                        self.textbox2.active = True
                    elif self.textbox3.input_rect.collidepoint(event.pos):
                        for textbox in self.textboxes:
                            textbox.active = False
                        self.textbox3.active = True
                    elif self.textbox4.input_rect.collidepoint(event.pos):
                        for textbox in self.textboxes:
                            textbox.active = False
                        self.textbox4.active = True
                    elif self.textbox5.input_rect.collidepoint(event.pos):
                        for textbox in self.textboxes:
                            textbox.active = False
                        self.textbox5.active = True
                    elif self.textbox6.input_rect.collidepoint(event.pos):
                        for textbox in self.textboxes:
                            textbox.active = False
                        self.textbox6.active = True

                if event.type == pygame.KEYDOWN:
                    for textbox in self.textboxes:
                        if textbox.active == True:
                            if event.key == pygame.K_BACKSPACE:
                                textbox.user_text = textbox.user_text[:-1]
                            else:
                                textbox.user_text += event.unicode

            #Set the screen for textinput
            self.screen.fill((202, 229, 241))
            #drawing buttons
            self.buttons.draw(self.screen)
            #rendering texts for each
            for textbox in self.textboxes:
                pygame.draw.rect(self.screen, (0,0,0), textbox.input_rect, 1)
                textbox.text_surface = textbox.base_font.render(textbox.user_text, True, (0, 0, 0))
                self.screen.blit(textbox.text_surface, (textbox.input_rect.x +5, textbox.input_rect.y + 5))




            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()