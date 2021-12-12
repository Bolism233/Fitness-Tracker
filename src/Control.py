import os
import pygame
import sys
from src.Button import Button
from src.Textbox import Textbox
from src.Text import Text
from src.Userdata import Userdata


class Controller:

    def __init__(self, width=900, height=500):

        # init pygame
        pygame.init()
        pygame.font.init()
        pygame.key.set_repeat(200, 100)
        self.clock = pygame.time.Clock()
        self.state = "Start"

        # set up user object
        self.user = Userdata()

        # set up screen
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Fitness Tracker")

        # set up start screen text
        self.start_title = Text(317, 200, "Fitness Calculator", font_size=40)
        self.start_subtitle = Text(350, 240, "By Jay, Lucas, and Sal", font_size=25)
        self.titletext = pygame.sprite.Group()
        self.titletext.add(self.start_title, self.start_subtitle)

        # set up textboxes
        self.textboxes = pygame.sprite.Group()  # textbox sprite group
        num_textboxes = 3
        x = 175
        y = 125
        second_row_y = y + 100
        for number in range(1, num_textboxes + 1):
            self.textboxes.add(Textbox(x, y))
            self.textboxes.add(Textbox(x, second_row_y))
            x += 200
        self.textboxes.add(Textbox(175, y + 200))

        # set up buttons
        self.start_button = Button(575, 400, "assets/start_btn.png", 0.25)
        self.back_button = Button(((253 + 580) / 2) - 8, 400, "assets/back_btn.png", 0.25)
        self.exit_button = Button(240, 400, "assets/exit_btn.png", 0.25)
        self.info_button = Button(375, y + 200, "assets/info_btn.png", 0.25)
        self.kg_button = Button(x, y, "assets/kg.png, 0.25")
        self.lb_button = Button(x, y, "assets/lb.png, 0.25")
        self.buttons = pygame.sprite.Group()  # button sprite group
        self.weightbuttons = pygame.sprite.Group().add(self.kg_button, self.lb_button)
        # set up text above textboxes
        self.texts = pygame.sprite.Group()  # text sprite group
        categories = [
            "Height (in cm)",
            "Age",
            "Current Weight (in kg)",
            "Activity Level (1-6)",
            "Desired Weight (kg/lbs)",
            "Intensity (1-3)",
            "Gender"
        ]

        index = 0
        for textbox in self.textboxes:
            self.texts.add(Text(textbox.x, textbox.y - 25, categories[index], font_size=19))
            index += 1

        # set up text for results screen
        self.resultstexts = pygame.sprite.Group()
        self.infotexts = pygame.sprite.Group()

        info = [
            '1: Burning 0 calories per day',
            '1: Mild weight loss/gain (0.25 kg per week)',
            '2: Little to no exercise',
            '2: Medium weight loss/gain (0.5 kg per week)',
            '3: Exercise 1-3 times/week',
            '3: Extreme weight loss/gain (1 kg per week)',
            '4: Exercise 4-5 times/week',
            '',
            '5: Daily exercise',
            '',
            '6: Intense daily exercise'
        ]

        self.infotexts.add(Text(100, 80, 'Activity level', font_size=28))
        self.infotexts.add(Text(500, 80, 'Intensity level', font_size=28))
        i = 0

        self.weight_status = 0

        for text in info:

            if not i % 2:
                self.infotexts.add(Text(100, 120 + (20 * i), text))

            else:
                self.infotexts.add(Text(500, 120 + (20 * (i - 1)), text))

            i += 1

    def exit(self):

        '''
        Deletes json files if there are any, then quits the program.
        :params: None
        :return: None
        '''

        try:
            os.remove('assets/BMI.json')
            os.remove('assets/Calories.json')
            os.remove('assets/Desired BMI.json')
            os.remove('assets/Macronutrients.json')
            sys.exit()

        except FileNotFoundError:
            sys.exit()

    def bmiHealth(self, bmiStatus):

        '''
        Determines whether the user's current and desired bmis are healthy or not
        :param bmiStatus: User's current/desired BMI
        :param wtStatus: Healthy, overweight, or underweight
        :return: Whether user's bmi is healthy/underweight/overweight
        '''

        if bmiStatus < 18.5:
            wtStatus = 'underweight.'
        elif 18.5 <= bmiStatus < 25:
            wtStatus = 'healthy.'
        elif 25 <= bmiStatus:
            wtStatus = 'overweight.'

        return wtStatus

    def mainloop(self):

        '''
        Sets state according to user input
        :params: None
        :return: None
        '''

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

        '''
        Displays start screen with credits and start and exit button.
        :params: None
        :return: None
        '''

        while self.state == "Start":

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if self.start_button.rect.collidepoint(event.pos):
                        self.start_button.zoomOut()
                        self.state = "Menu"

                    elif self.exit_button.rect.collidepoint(event.pos):
                        self.exit()

                if event.type == pygame.MOUSEMOTION:

                    for button in self.buttons:

                        if button.rect.collidepoint(event.pos) and button.status == False:
                            button.zoomIn()
                            button.status = True

                        if not button.rect.collidepoint(event.pos) and button.status == True:
                            button.zoomOut()
                            button.status = False

            # Set the screen for textinput
            self.screen.fill((255, 255, 255))

            # drawing buttons/text
            self.buttons.empty()
            self.buttons.add(self.start_button, self.exit_button)
            self.buttons.draw(self.screen)
            for text in self.titletext:
                self.screen.blit(text.text_surface, (text.x, text.y))

            # update the window at once
            pygame.display.flip()
            self.clock.tick(60)

    def menuloop(self):

        '''
        Displays screen where user can input data for the API to use to calculate BMI, calories, and macronutrient info.
        :params: None
        :return: None
        '''

        while self.state == "Menu":

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if self.start_button.rect.collidepoint(event.pos):  # Check if its clicked on the buttons
                        # Save User Data
                        self.user.saveData(self)
                        # switch to new screen
                        self.start_button.zoomOut()

                        if self.user.height == '' or self.user.age == '' or self.user.weight == '' or self.user.activity_level == '' or self.user.desired_weight == '' or self.user.intensity == '' or self.user.gender == '':
                            print("Please fill in everybox")
                        else:
                            self.crnt_bmi = self.user.bmi(self.user.weight, 'BMI')
                            self.dsrd_bmi = self.user.bmi(self.user.desired_weight, 'Desired BMI')
                            self.calory_maintain = self.user.calories()[0]
                            self.calory_goal = self.user.calories()[1]
                            self.macronutrients = self.user.macronutrients()

                            self.state = "Results"

                    elif self.back_button.rect.collidepoint(event.pos):
                        # Save User Data
                        self.user.saveData(self)
                        # switch to new screen
                        self.back_button.zoomOut()
                        self.state = "Start"

                    elif self.exit_button.rect.collidepoint(event.pos):
                        self.exit()

                    elif self.info_button.rect.collidepoint(event.pos):
                        # Save User Data
                        self.user.saveData(self)
                        # switch to new screen
                        self.info_button.zoomOut()
                        self.state = "Info"

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

                            if event.key == pygame.K_BACKSPACE:  # for deleting userinput
                                textbox.user_text = textbox.user_text[:-1]
                                textbox.setDefaultLen()

                            else:  # for entering userinput
                                textbox.user_text += event.unicode
                                textbox.setDefaultLen()

            # Set the screen for textinput
            self.screen.fill((255, 255, 255))
            # drawing buttons
            self.buttons.empty()
            self.buttons.add(self.start_button, self.exit_button, self.back_button, self.info_button)
            self.buttons.draw(self.screen)

            # rendering texts above the textboxes
            for text in self.texts:
                self.screen.blit(text.text_surface, (text.x, text.y))

            # rendering textboxes for each
            for textbox in self.textboxes:

                if textbox.active == True:
                    pygame.draw.rect(self.screen, (51, 153, 255), textbox.input_rect, 1)
                else:
                    pygame.draw.rect(self.screen, (0, 0, 0), textbox.input_rect, 1)

                # render user_texts
                textbox.text_surface = textbox.base_font.render(textbox.user_text, True, (0, 0, 0))
                self.screen.blit(textbox.text_surface, (textbox.input_rect.x + 5, textbox.input_rect.y + 5))

            # update the window at once
            pygame.display.flip()
            self.clock.tick(60)

    def infoloop(self):

        '''
        Displays info about the params used to determine user's health
        :params: None
        :return: None
        '''

        while self.state == "Info":

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if self.exit_button.rect.collidepoint(event.pos):
                        self.exit()

                    if self.back_button.rect.collidepoint(event.pos):
                        self.back_button.zoomOut()
                        self.state = "Menu"

                if event.type == pygame.MOUSEMOTION:

                    for button in self.buttons:

                        if button.rect.collidepoint(event.pos) and button.status == False:
                            button.zoomIn()
                            button.status = True

                        if not button.rect.collidepoint(event.pos) and button.status == True:
                            button.zoomOut()
                            button.status = False

            # Set the screen for textinput
            self.screen.fill((255, 255, 255))
            # drawing buttons
            self.buttons.empty()
            self.buttons.add(self.exit_button, self.back_button)
            self.buttons.draw(self.screen)
            for text in self.infotexts:
                self.screen.blit(text.text_surface, (text.x, text.y))

            pygame.display.flip()
            self.clock.tick(60)

    def resultsloop(self):

        '''
        Displays results returned by API and tells user whether their current/desired weights are healthy or not.
        :params: None
        :return: None
        '''

        while self.state == "Results":

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if self.back_button.rect.collidepoint(event.pos):
                        self.back_button.zoomOut()
                        self.state = "Menu"

                    if self.exit_button.rect.collidepoint(event.pos):
                        self.exit()

                if event.type == pygame.MOUSEMOTION:

                    for button in self.buttons:

                        if button.rect.collidepoint(event.pos) and button.status == False:
                            button.zoomIn()
                            button.status = True

                        if not button.rect.collidepoint(event.pos) and button.status == True:
                            button.zoomOut()
                            button.status = False

            weight_status = self.bmiHealth(self.crnt_bmi)
            dsrd_weight_status = self.bmiHealth(self.dsrd_bmi)

            self.bmi = Text(50, 70, f'Your current BMI is {self.crnt_bmi}, which is considered {weight_status}',
                            font_size=28)
            if dsrd_weight_status == weight_status:
                self.desired_bmi = Text(50, 120,
                                        f'Your desired BMI is {self.dsrd_bmi}, which is also considered {dsrd_weight_status}',
                                        font_size=28)
            else:
                self.desired_bmi = Text(50, 120,
                                        f'Your desired BMI is {self.dsrd_bmi}, which is considered {dsrd_weight_status}',
                                        font_size=28)

            self.maintain_text = Text(50, 180,
                                      f'To maintain your current weight, you should consume {self.calory_maintain} calories a day.')
            self.goal_text = Text(50, 210,
                                  f'To reach your desired weight with the intensity selected, you should consume {self.calory_goal} calories a day. ')

            self.macronutrients_title = Text(50, 260, "Macronutrient ratios", font_size=28)
            self.balanced_text = Text(50, 320,
                                      f'Balanced: {int(self.macronutrients["balanced"]["protein"])}g protein, {int(self.macronutrients["balanced"]["fat"])}g fat, {int(self.macronutrients["balanced"]["carbs"])}g carbs.')
            self.lowfat_text = Text(50, 350,
                                    f'Low fat: {int(self.macronutrients["lowfat"]["protein"])}g protein, {int(self.macronutrients["lowfat"]["fat"])}g fat, {int(self.macronutrients["lowfat"]["carbs"])}g carbs.')
            self.lowcarbs_text = Text(450, 320,
                                      f'Low carbs: {int(self.macronutrients["lowcarbs"]["protein"])}g protein, {int(self.macronutrients["lowcarbs"]["fat"])}g fat, {int(self.macronutrients["lowcarbs"]["carbs"])}g carbs.')
            self.highprotein_text = Text(450, 350,
                                         f'High protein: {int(self.macronutrients["highprotein"]["protein"])}g protein, {int(self.macronutrients["highprotein"]["fat"])}g fat, {int(self.macronutrients["highprotein"]["carbs"])}g carbs.')

            self.resultstexts.empty()
            self.resultstexts.add(self.bmi, self.desired_bmi, self.maintain_text, self.goal_text, self.balanced_text,
                                  self.lowfat_text, self.lowcarbs_text, self.highprotein_text,
                                  self.macronutrients_title)

            self.screen.fill((255, 255, 255))

            for text in self.resultstexts:
                self.screen.blit(text.text_surface, (text.x, text.y))

            self.buttons.empty()
            self.buttons.add(self.exit_button, self.back_button)
            self.buttons.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)
