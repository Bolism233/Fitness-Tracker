import pygame
import sys
from src.Button import Button
from src.Textbox import Textbox
from src.Text import Text
from src.Userdata import Userdata

class Controller:


    def __init__(self, width = 900, height = 500):

        #init pygame
        pygame.init()
        pygame.font.init()
        pygame.key.set_repeat(200, 100)
        self.clock = pygame.time.Clock()
        self.state = "Start"

        #set up user object
        self.user = Userdata()

        #set up screen
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Fitness Tracker")

        #set up start screen text
        self.start_title = Text(317,200,"Fitness Calculator",font_size=40)
        self.start_subtitle = Text(350,240,"By Jay, Lucas, and Sal",font_size=25)
        self.titletext = pygame.sprite.Group()
        self.titletext.add(self.start_title, self.start_subtitle)

        #set up textboxes
        self.textboxes = pygame.sprite.Group() # textbox sprite group
        num_textboxes = 3
        x = 175
        y = 125
        second_row_y = y + 100
        for number in range(1, num_textboxes + 1):
            self.textboxes.add(Textbox(x, y))
            self.textboxes.add(Textbox(x, second_row_y))
            x += 200
        self.textboxes.add(Textbox(175,y+200))

        #set up buttons
        self.start_button = Button(575, 400, "assets/start_btn.png", 0.25)
        self.back_button = Button(((253+580)/2)-8,400, "assets/back_btn.png", 0.25)
        self.exit_button = Button(240, 400, "assets/exit_btn.png", 0.25)
        self.info_button = Button(375, y+200, "assets/info_btn.png", 0.25)
        self.buttons = pygame.sprite.Group() #button sprite group
        self.buttons.add(self.start_button, self.exit_button)

        #set up text above textboxes
        self.texts = pygame.sprite.Group()  # text sprite group
        categories = ["Height (in cm)", "Age", "Current Weight (in kg)", "Activity Level (1-6)", "Desired Weight (in kg)", "Intensity (1-3)", "Gender"]
        index = 0
        for textbox in self.textboxes:
            self.texts.add(Text(textbox.x, textbox.y - 25, categories[index]))
            index += 1

        #set up text for results screen
        self.resultstexts = pygame.sprite.Group()


    def mainloop(self):

        while True:

            if self.state == "Start":
                self.startloop()

            elif self.state == "Menu":
                self.menuloop()

            elif self.state == "Info":
                self.infoloop()

            elif self.state == "Results":
                self.resultsloop()


    def startloop(self):

        while self.state == "Start":

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if self.start_button.rect.collidepoint(event.pos):
                        self.start_button.zoomOut()
                        self.state = "Menu"

                    elif self.exit_button.rect.collidepoint(event.pos):
                        sys.exit()

                if event.type == pygame.MOUSEMOTION:

                    for button in self.buttons:

                        if button.rect.collidepoint(event.pos) and button.status == False:
                            button.zoomIn()
                            button.status = True

                        if not button.rect.collidepoint(event.pos) and button.status == True:
                            button.zoomOut()
                            button.status = False

            #Set the screen for textinput
            self.screen.fill((255, 255, 255))

            #drawing buttons/text
            self.buttons.remove(self.back_button, self.info_button)
            self.buttons.draw(self.screen)
            # self.start_title=Text(320,200,"Fitness Calculator",font_size=40)
            # self.start_subtitle=Text(300,240,"By Jay, Lucas, and Sal",font_size=20)
            for text in self.titletext:
                self.screen.blit(text.text_surface, (text.x, text.y))

            #update the window at once
            pygame.display.flip()
            self.clock.tick(60)


    def menuloop(self):

        while self.state == "Menu":

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if self.start_button.rect.collidepoint(event.pos): #Check if its clicked on the buttons
                        #Save User Data
                        self.user.saveData(self)
                        #switch to new screen
                        self.start_button.zoomOut()

                        self.crnt_bmi = self.user.bmi(self.user.weight,'BMI')
                        self.dsrd_bmi = self.user.bmi(self.user.desired_weight,'Desired BMI')
                        self.calory_maintain = self.user.calories()[0]
                        self.calory_goal = self.user.calories()[1]

                        self.state = "Results"

                    elif self.back_button.rect.collidepoint(event.pos):
                        #Save User Data
                        self.user.saveData(self)
                        #switch to new screen
                        self.back_button.zoomOut()
                        self.state = "Start"

                    elif self.exit_button.rect.collidepoint(event.pos):
                        sys.exit()

                    for textbox in self.textboxes:
                        textbox.active = False
                        if textbox.input_rect.collidepoint(event.pos):
                            textbox.active = True

                if event.type == pygame.MOUSEMOTION:

                    for button in self.buttons:

                        if button.rect.collidepoint(event.pos) and button.status == False:
                            button.zoomIn()
                            button.status = True

                        if not button.rect.collidepoint(event.pos) and button.status == True:
                            button.zoomOut()
                            button.status = False

                if event.type == pygame.KEYDOWN:

                    for textbox in self.textboxes:

                        if textbox.active == True:

                            if event.key == pygame.K_BACKSPACE:      #for deleting userinput
                                textbox.user_text = textbox.user_text[:-1]
                                textbox.setDefaultLen()

                            else:              #for entering userinput
                                textbox.user_text += event.unicode
                                textbox.setDefaultLen()

            #Set the screen for textinput
            self.screen.fill((255, 255, 255))
            #drawing buttons
            self.buttons.add(self.back_button,self.info_button)
            self.buttons.draw(self.screen)

            #rendering texts above the textboxes
            for text in self.texts:
                self.screen.blit(text.text_surface, (text.x, text.y))

            #rendering textboxes for each
            for textbox in self.textboxes:

                if textbox.active == True:
                    pygame.draw.rect(self.screen, (51,153,255), textbox.input_rect, 1)
                else:
                    pygame.draw.rect(self.screen, (0,0,0), textbox.input_rect, 1)

                # render user_texts
                textbox.text_surface = textbox.base_font.render(textbox.user_text, True, (0, 0, 0))
                self.screen.blit(textbox.text_surface, (textbox.input_rect.x + 5, textbox.input_rect.y + 5))

            #update the window at once
            pygame.display.flip()
            self.clock.tick(60)


    def infoloop(self):

        while self.state == "Info":

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if self.back_button.rect.collidepoint(event.pos):
                        self.state == "Menu"

            pygame.display.flip()
            self.clock.tick(60)


    def resultsloop(self):

        while self.state == "Results":

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sys.exit()

            #if "assets/bmi" doesn't exist:
                #run api

            # crnt_bmi = self.user.bmi(self.user.weight,'BMI')
            # dsrd_bmi = self.user.bmi(self.user.desired_weight,'Desired BMI')
            # calory_maintain = self.user.calories()[0]
            # calory_goal = self.user.calories()[1]

            #else:
                #just display data

            if self.crnt_bmi < 18.5:
                weight_status = 'underweight.'
            elif 18.5 <= self.crnt_bmi < 25:
                weight_status = 'healthy.'
            elif 25 <= self.crnt_bmi:
                weight_status = 'overweight.'

            if self.dsrd_bmi < 18.5:
                dsrd_weight_status = 'underweight.'
            elif 18.5 <= self.dsrd_bmi < 25:
                dsrd_weight_status = 'healthy.'
            elif 25 <= self.dsrd_bmi:
                dsrd_weight_status = 'overweight.'

            self.bmi = Text(100,100, f'Your current BMI is {self.crnt_bmi}, which is considered {weight_status}',font_size=30)
            if dsrd_weight_status == weight_status:
                self.desired_bmi = Text(100,150, f'Your desired BMI is {self.dsrd_bmi}, which is also considered {dsrd_weight_status}',font_size=30)
            else:
                self.desired_bmi = Text(100,150, f'Your desired BMI is {self.dsrd_bmi}, which is considered {dsrd_weight_status}',font_size=30)
            self.maintain_text = Text(100,200, f'To maintain your current weight, you should consume {self.calory_maintain} calories a day.')
            self.goal_text = Text(100,230, f'To reach your desired weight with the intensity selected, you should consume {self.calory_goal} calories a day. ')
            self.resultstexts.add(self.bmi, self.desired_bmi,self.maintain_text, self.goal_text)

            self.screen.fill((255, 255, 255))
            for text in self.resultstexts:
                self.screen.blit(text.text_surface, (text.x, text.y))

            pygame.display.flip()
            self.clock.tick(60)
