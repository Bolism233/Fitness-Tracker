import pygame
#clock = pygame.time.Clock()
#screen = pygame.display.set_mode([800, 800])

class Textbox(pygame.sprite.Sprite):
    def __init__(self, x, y, user_text = ''):
        pygame.sprite.Sprite.__init__(self)
        pygame.font.init()
        self.black = (0, 0 ,0)
        self.white = (255, 255, 255)
        font_size = 22
        self.x = x
        self.y = y
        self.user_text = user_text
        self.base_font = pygame.font.Font(None, font_size)
        self.text_surface = self.base_font.render(self.user_text, True, self.white)
        self.input_rect = pygame.Rect(self.x, self.y, 140, 32)
        self.active = False # whether it is clicked on or not.

    def update(self):
        self.input_rect.w = max(140, self.text_surface.get_width() + 20)

# textbox = Textbox(500, 150)
# run = True
# while run:
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#         if event.type == pygame.MOUSEBUTTONDOWN:
#                 if textbox.input_rect.collidepoint(event.pos):
#                     textbox.active = True
#         if event.type == pygame.KEYDOWN:
#             if textbox.active == True:
#                 if event.key == pygame.K_BACKSPACE:
#                     textbox.user_text = textbox.user_text[:-1]
#                     print(textbox.user_text)
#                 else:
#                     textbox.user_text += event.unicode
#     screen.fill((255,255,255))
#     pygame.draw.rect(screen, (0, 0, 0), textbox.input_rect, 1)
#     textbox.text_surface = textbox.base_font.render(textbox.user_text, True, (0, 0, 0))
#     screen.blit(textbox.text_surface, (textbox.input_rect.x, textbox.input_rect.y))
#
#     pygame.display.flip()
#     clock.tick(60)