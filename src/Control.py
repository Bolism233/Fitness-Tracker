import pygame
import sys
from src.Button import Button
from src.Textbox import Textbox
from src.Text import Text
from src.Userdata import Userdata

class Controller:
    def __init__(self, width = 900, height = 500):
        self.clock = pygame.time.Clock()
        pygame.init()
        pygame.font.init()
        pygame.key.set_repeat(200, 100)
        self.state = "Menu"
        #set up colors
        #skyblue = (0, 128, 255)
        black = (0,0,0)
        #Set up screen
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        # self.background = pygame.Surface(self.screen.get_size()).convert()
        # self.background.fill((202, 229, 241)) What does background do
        pygame.display.set_caption("Fitness Tracker Demo")
        #set up buttons
        self.start_button = Button (300, 400, "assets/start_btn.png", 0.25)
        self.exit_button = Button (500, 400, "assets/exit_btn.png", 0.25)
        self.buttons = pygame.sprite.Group() #button sprite group
        self.buttons.add(self.start_button, self.exit_button)
        #set up textboxes
        self.textboxes = pygame.sprite.Group() # textbox sprite group
        num_textboxes = 3
        x = 150
        y = 150
        second_row_y = 300
        for number in range(1, num_textboxes + 1):
            self.textboxes.add(Textbox(x, y, ""))
            self.textboxes.add(Textbox(x, second_row_y, ""))
            x += 200
        # Set up texts above the textboxes
        self.texts = pygame.sprite.Group()  # text sprite group
        self.title = Text(width/2 - 100, 50, "Fitness Tracker", black, 28)
        self.texts.add(self.title)
        self.categories = ["Gender", "Weight", "Age", "Activity Level", "Height", "Desired Weight"]
        index = 0
        for textbox in self.textboxes:
            self.texts.add(Text(textbox.x, textbox.y -35, self.categories[index]))
            index += 1
        self.dude = Userdata()

    def mainloop(self):
        while True:
            if self.state == "Menu":
                self.menuloop()
            elif self.state == "Calculation":
                self.calculationloop()

    def menuloop(self):
        while self.state == "Menu":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_button.rect.collidepoint(event.pos): #Check if its clicked on the buttons
                        #Save User Data
                        self.dude.gender = self.textboxes.sprites()[0].user_text
                        self.dude.age = self.textboxes.sprites()[1].user_text
                        self.dude.weight = self.textboxes.sprites()[2].user_text
                        self.dude.height = self.textboxes.sprites()[3].user_text
                        self.dude.activity_level = self.textboxes.sprites()[4].user_text
                        self.dude.desired_weight = self.textboxes.sprites()[5].user_text
                        self.state = "Calculation"
                    elif self.exit_button.rect.collidepoint(event.pos):
                        sys.exit()
                    for textbox in self.textboxes:
                        textbox.active = False
                        if textbox.input_rect.collidepoint(event.pos):
                            textbox.active = True
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
                            #for deleting userinput
                            if event.key == pygame.K_BACKSPACE:
                                textbox.user_text = textbox.user_text[:-1]
                                textbox.update()
                            # for entering userinput
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
                # render user_texts
                textbox.text_surface = textbox.base_font.render(textbox.user_text, True, (0, 0, 0))
                self.screen.blit(textbox.text_surface, (textbox.input_rect.x + 5, textbox.input_rect.y + 5))




            #update the window at once
            pygame.display.flip()
            self.clock.tick(60)

    def calculationloop(self):
        while self.state == "Calculation":
            self.screen.fill((202, 229, 241))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.flip()
