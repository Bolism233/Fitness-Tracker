import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, img_file, scale):
        pygame.sprite.Sprite.__init__(self)
        #scale the image
        self.scale = scale
        image = pygame.image.load(img_file).convert_alpha()
        self.width = image.get_width()
        self.height = image.get_height()
        self.image = pygame.transform.scale(image, (int(self.width * self.scale), int(self.height) * self.scale))
        self.scale += 0.1
        self.scale2 = self.scale - 0.2
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    # def zoomin(self):
    #     self.image = self.image = pygame.transform.scale(self.image,(int(self.width * self.scale), int(self.height) * self.scale))
    # def zoomout(self):
    #     self.image = self.image = pygame.transform.scale(self.image,(int(self.width * self.scale2), int(self.height) * self.scale2))