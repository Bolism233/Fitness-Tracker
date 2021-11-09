import pygame
pygame.init()

class Button(): #Button(pygame.Sprite.Sprite)
    def __init__(self, color, x, y, width, height, text = ''):
        #super.__init__(self)
        #self.image = pygame.image.load("assets/calculateButton.jpg")
        #self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
        self.text = text

    def draw(self, window, outline = None):
        if outline:
            pygame.draw.rect(window, outline, (self.x-2, self.y-2, self.width+4, self.height+4))
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 20)
            text = font.render(self.text, 1, (0,25,0))
            window.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2) ))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] >self.y and pos[1] < self.y + self.height:
                return True
        return False

    def redrawWindow(self, window, button):
        window.fill(255,255,255)
        button.draw(window, (0,0,0))


class Controller:
    def __init__(self, w, d ):
        self.width= w
        self.height = d
        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Shooter")

    def mainloop(self):
        run = True
        while run:
            turtle = Button("green", 500, 400, 20, 30, "wadad")
            turtle.draw(self.win)
            pygame.display.update()
            for event in pygame.event.get():

                pos = pygame.mouse.get_pos()
                if turtle.isOver(pos):
                    turtle.redrawWindow(self.win, turtle)
                if event.type == pygame.QUIT:
                    run = False


        pygame.quit()

c = Controller(900, 500)
c.mainloop()