import pygame


class Background(pygame.sprite.Sprite):
    def __init__(self, image, location):
        # Call Sprite initializer
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


class DrawButton:
    def __init__(self, screen, b_color, t_color, text, b_width, b_height, position_x, position_y):
        self.screen = screen
        self.b_color = b_color
        self.t_color = t_color
        self.text = text
        self.b_width = b_width
        self.b_height = b_height
        self.position_x = position_x
        self.position_y = position_y

        self.font = pygame.font.SysFont("Times", 40)

        self.draw()

    def draw(self, image=""):
        pygame.draw.rect(self.screen, self.b_color or image,
                         [self.position_x, self.position_y, self.b_width, self.b_height], 0)
        text = self.font.render(str(self.text), 1, self.t_color)
        self.screen.blit(text, (self.position_x + self.b_width*0.5 - text.get_width()*0.5,
                                self.position_y + self.b_height*0.5 - text.get_height()*0.5))

    def collision(self, new_color=(0, 0, 0)):
        # Check for collision with mouse and change background color
        mouse = pygame.mouse.get_pos()
        if (mouse[0] in range(int(self.position_x), int(self.position_x + self.b_width))) \
                and (mouse[1] in range(int(self.position_y), int(self.position_y + self.b_height))):
            self.b_color = new_color
            self.draw()

            # If pressed on a button change state
            if pygame.mouse.get_pressed()[0]:
                return True


class DrawText:
    def __init__(self, screen, text, color, position_x, position_y, transparent=1):
        self.screen = screen
        self.text = text
        self.color = color
        self.position_x = position_x
        self.position_y = position_y
        self.transparent = transparent

        self.font = pygame.font.SysFont("Times", 40)

        self.draw()

    def draw(self):
        self.text = self.font.render(self.text, self.transparent, self.color)
        self.screen.blit(self.text,
                         (self.position_x - self.text.get_width()*0.5, self.position_y - self.text.get_height()*0.5))
