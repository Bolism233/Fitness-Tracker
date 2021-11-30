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
        
        #set up buttons
        self.start_button = Button(580, 400, "assets/start_btn.png", 0.25)
        self.back_button = Button(((253+580)/2)-5,400, "assets/start_btn.png", 0.25)
        self.exit_button = Button(253, 400, "assets/exit_btn.png", 0.25)
        self.buttons = pygame.sprite.Group() #button sprite group
        self.buttons.add(self.start_button, self.exit_button)
        
        #set up textboxes
        self.textboxes = pygame.sprite.Group() # textbox sprite group
        num_textboxes = 3
        x = 175
        y = 150
        second_row_y = 300
        for number in range(1, num_textboxes + 1):
            self.textboxes.add(Textbox(x, y, ""))
            self.textboxes.add(Textbox(x, second_row_y, ""))
            x += 200
        
        #set up text above textboxes
        self.texts = pygame.sprite.Group()  # text sprite group
        self.title = Text(375, 50, "Fitness Tracker", (0,0,0), 28)
        self.texts.add(self.title)
        categories = ["Gender", "Weight (in kg)", "Age", "Activity Level (1-6)", "Height (in cm)", "Desired Weight (in kg)"]
        index = 0
        for textbox in self.textboxes:
            self.texts.add(Text(textbox.x, textbox.y -35, categories[index]))
            index += 1

        #set up text for calculation screen
        self.calctexts = pygame.sprite.Group()


    def mainloop(self):
        while True:
            if self.state == "Start":
                self.startloop()
            elif self.state == "Menu":
                self.menuloop()
            elif self.state == "Calculation":
                self.calculationloop()


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
            #drawing buttons
            self.buttons.remove(self.back_button)
            self.buttons.draw(self.screen)
            self.start_title=Text(320,200,"Fitness Calculator",font_size=40)
            self.screen.blit(self.start_title.text_surface, (self.start_title.x, self.start_title.y))

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
                        self.user.gender = self.textboxes.sprites()[0].user_text
                        self.user.age = self.textboxes.sprites()[2].user_text
                        self.user.weight = self.textboxes.sprites()[1].user_text
                        self.user.height = self.textboxes.sprites()[4].user_text
                        self.user.activity_level = f'level_{self.textboxes.sprites()[3].user_text}'
                        self.user.desired_weight = self.textboxes.sprites()[5].user_text
                        self.start_button.zoomOut()
                        self.state = "Calculation"

                    elif self.back_button.rect.collidepoint(event.pos):
                        self.back_button.zoomOut()
                        self.state = "Start"
                        # self.buttons.empty()
                        # self.buttons.remove(self.back_button)

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
                            #for deleting userinput
                            if event.key == pygame.K_BACKSPACE:
                                textbox.user_text = textbox.user_text[:-1]
                                textbox.setDefaultLen()
                            # for entering userinput
                            else:
                                textbox.user_text += event.unicode
                                textbox.setDefaultLen()

            #Set the screen for textinput
            self.screen.fill((255, 255, 255))
            #drawing buttons
            self.buttons.add(self.back_button)
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


    def calculationloop(self):
        while self.state == "Calculation":

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    # #write Userdata into the json file
                    # writer = open("src/data.json", "w")
                    # #example
                    # new_text = "Hello World"
                    # writer.write(new_text)
                    # #for result in User data, write it into the data.son
                    sys.exit()

                # if event.type == pygame.MOUSEBUTTONDOWN:
                #     # if self.start_button.rect.collidepoint(event.pos): #Check if its clicked on the buttons
                #     #     #Save User Data
                #     #     self.user.gender = self.textboxes.sprites()[0].user_text
                #     #     self.user.age = self.textboxes.sprites()[2].user_text
                #     #     self.user.weight = self.textboxes.sprites()[1].user_text
                #     #     self.user.height = self.textboxes.sprites()[4].user_text
                #     #     self.user.activity_level = f'level_{self.textboxes.sprites()[3].user_text}'
                #     #     self.user.desired_weight = self.textboxes.sprites()[5].user_text
                        
                #     #     self.state = "Calculation"

                #     if self.back_button.rect.collidepoint(event.pos):
                #         self.state = "Calculation"
                #         # self.buttons.empty()
                #         # self.buttons.remove(self.back_button)

                #     elif self.exit_button.rect.collidepoint(event.pos):
                #         sys.exit()

                #     for textbox in self.textboxes:
                #         textbox.active = False
                #         if textbox.input_rect.collidepoint(event.pos):
                #             textbox.active = True

                # if event.type == pygame.MOUSEMOTION:
                #     for button in self.buttons:
                #         if button.rect.collidepoint(event.pos) and button.status == False:
                #             button.zoomIn()
                #             button.status = True
                #         if not button.rect.collidepoint(event.pos) and button.status == True:
                #             button.zoomOut()
                #             button.status = False

            crnt_bmi = self.user.bmi(self.user.weight,'BMI')
            dsrd_bmi = self.user.bmi(self.user.desired_weight,'Desired BMI')
            calory_maintain = self.user.calories(5)
            
            if crnt_bmi < 18.5:
                weight_status = 'underweight.'
            elif 18.5 <= crnt_bmi < 25:
                weight_status = 'healthy. Nice job!'
            elif 25 <= crnt_bmi:
                weight_status = 'overweight.'

            # if DESIRED_BMI < 18.5:
            #     desired_weight_status = 'underweight.'
            # elif 18.5 <= BMI < 25:
            #     desired_weight_status = 'healthy. Nice job!'
            # elif 25 <= BMI:
            #     desired_weight_status = 'overweight.'

            self.bmi = Text(100,100, f'Your current BMI is {crnt_bmi}, which is considered {weight_status}',font_size=30)
            self.desired_bmi = Text(100,150, f'Your desired BMI is {dsrd_bmi}.',font_size=30)
            self.maintain = Text(100,200, f'To maintain your current weight, you should consume {calory_maintain[0]} calories a day.')
            #self.loss = Text(100,200, f'To reach this ')
            self.calctexts.add(self.bmi, self.desired_bmi,self.maintain)

            self.screen.fill((255, 255, 255))
            for text in self.calctexts:
                self.screen.blit(text.text_surface, (text.x, text.y))
            # self.buttons.draw(self.screen)
            
            pygame.display.flip()
            self.clock.tick(60)
