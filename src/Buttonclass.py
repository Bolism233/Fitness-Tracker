import pygame

screen_width = 800
screen_height = 500
btn_image = pygame.image.load("calculateButton2.jpg")
btn_image= pygame.transform.rotate(pygame.transform.scale(btn_image, (80,50)), 0)
screen = pygame.display.set_mode((screen_width, screen_height))

class Button:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def draw(self):
        #draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

start_button = Button(100, 200, btn_image)
exit_button = Button(450, 200, btn_image)

run = True
while run:
    screen.fill((202, 229, 241))
    start_button.draw()
    exit_button.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()

