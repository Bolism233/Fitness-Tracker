import pygame
from src.Buttonclass import Button
from src.Textbox import Textbox
from src.Text import Text
from src.Userdata import Userdata

class Controller:
    def __init__(self, width = 900, height = 500):
        self.clock = pygame.time.Clock()
        pygame.init()
        pygame.font.init()
        #set up colors
        skyblue = (0, 128, 255)
        black = (0,0,0)
        #Set up screen
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Fitness Tracker Demo")
        self.screen.fill((202, 229, 241))
        self.screen_rect = self.screen.get_rect()
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
        # Set up texts above the textboxes
        self.text0 = Text(width/2 - 100, 50, "Fitness Tracker", black, 28)
        self.text1 = Text(self.textbox1.x, self.textbox1.y - 30, "Age")
        self.text2 = Text(self.textbox2.x, self.textbox2.y - 30, "Gender")
        self.text3 = Text(self.textbox3.x, self.textbox3.y - 30, "Height")
        self.text4 = Text(self.textbox4.x, self.textbox4.y - 30, "Weight")
        self.text5 = Text(self.textbox5.x, self.textbox5.y - 30, "Activity Level")
        self.text6 = Text(self.textbox6.x, self.textbox6.y - 30, "Desired Weight")
        self.texts = pygame.sprite.Group()
        self.texts.add(self.text0, self.text1, self.text2, self.text3, self.text4, self.text5, self.text6)

    def mainloop(self):
        run = True

        while run:
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
                if event.type == pygame.MOUSEMOTION:
                    for button in self.buttons:
                        if button.rect.collidepoint(event.pos) and button.status == False:
                            button.zoomin()
                            button.status = True
                        if not button.rect.collidepoint(event.pos) and button.status == True:
                            button.zoomout()
                            button.status = False
                if event.type == pygame.KEYDOWN:
                    for textbox in self.textboxes:
                        if textbox.active == True:
                            if event.key == pygame.K_BACKSPACE:
                                textbox.user_text = textbox.user_text[:-1]
                                textbox.update()
                            else:
                                textbox.user_text += event.unicode
                                textbox.update()

            #Set the screen for textinput
            self.screen.fill((202, 229, 241))
            #drawing buttons
            self.buttons.draw(self.screen)
            #rendering texts above the textboxes
            for text in self.texts:
                self.screen.blit(text.text_surface, (text.x, text.y))
            #rendering textboxes for each
            for textbox in self.textboxes:
                if textbox.active == True:
                    pygame.draw.rect(self.screen, (0,0,0), textbox.input_rect, 1)
                else:
                    pygame.draw.rect(self.screen, (255, 255, 255), textbox.input_rect, 1)
                textbox.text_surface = textbox.base_font.render(textbox.user_text, True, (0, 0, 0))
                self.screen.blit(textbox.text_surface, (textbox.input_rect.x +5, textbox.input_rect.y + 5))




            #update the window at once
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()