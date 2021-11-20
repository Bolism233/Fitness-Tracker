import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, img_file, scale):
        """
        Set up buttons on the screen, scale the image and create rectangles for each, set the default status to False.
        :param x: x coordinate of the button
        :param y: y coordinate of the button
        :param img_file: image file of the button
        :param scale: scale of the image
        :return: None
        """
        pygame.sprite.Sprite.__init__(self)
        #scale the image
        self.x = x
        self.y = y
        self.scale = scale
        image = pygame.image.load(img_file).convert_alpha()
        self.width = image.get_width()
        self.height = image.get_height()
        self.originimage = pygame.transform.scale(image, (int(self.width * self.scale), int(self.height) * self.scale))
        self.image = self.originimage
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.status = False

    def zoomIn(self):
        """
        Resize the image of the button to make it bigger
        args: None
        :return: None
        """
        self.scale = 0.3
        self.image = pygame.transform.scale(self.originimage,(int(self.width * self.scale), int(self.height) * self.scale))
        self.rect = self.image.get_rect()
        self.rect.move_ip(self.x, self.y)

    def zoomOut(self):
        """
        Scale the image back to its original size
        args: None
        :return: None
        """
        self.scale = 0.25
        self.image = pygame.transform.scale(self.originimage,(int(self.width * self.scale), int(self.height) * self.scale))
        self.rect = self.image.get_rect()
        self.rect.move_ip(self.x, self.y)
