import pygame
import time


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
                         [self.position_x - self.b_width*0.5, self.position_y - self.b_height*0.5, self.b_width, self.b_height], 0)
        text = self.font.render(str(self.text), 1, self.t_color)
        self.screen.blit(text, (self.position_x - self.b_width*0.5 + self.b_width*0.5 - text.get_width()*0.5,
                                self.position_y - self.b_height * 0.5 + self.b_height*0.5 - text.get_height()*0.5))

    def collision(self, new_color=(0, 0, 0)):
        # Check for collision with mouse and change background color
        mouse = pygame.mouse.get_pos()
        if (mouse[0] in range(int(self.position_x - self.b_width*0.5), int(self.position_x - self.b_width*0.5 + self.b_width))) \
                and (mouse[1] in range(int(self.position_y - self.b_height * 0.5), int( self.position_y - self.b_height * 0.5 + self.b_height))):
            self.b_color = new_color
            self.draw()

            # If pressed on a button change state
            if pygame.mouse.get_pressed()[0]:
                time.sleep(0.3)
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


class DrawImage:
    def __init__(self, screen, image, position_x, position_y):
        self.screen = screen
        self.image = pygame.image.load(image)
        self.position_x = position_x
        self.position_y = position_y

        self.draw()

    def draw(self):
        self.screen.blit(self.image, (self.position_x - self.image.get_rect().size[0]*0.5,
                                      self.position_y - self.image.get_rect().size[1]*0.5))


class Player:
    def __init__(self, player_id, name, score, position, roll = 0):
        self.id = player_id
        self.name = name
        self.score = score
        self.position = position
        self.roll = roll


class Point:
    def __init__(self, x, y, category):
        self.x = x
        self.y = y
        self.category = category
        self.hightlight = 0


    def returnx(self):
        return self.x

    def returny(self):
        return self.y

    def returnc(self):
        return self.category

    def drawself(self, screen, width, height):
        pygame.draw.rect(screen, (0,0,0), [width/4*self.category + width/8*self.x + 50,height/10 *self.y + 30, 8*(1+self.highlight), 8*(1+self.highlight)], 2)

    def hightlight(self):
        if self.highlight == 0:
            self.highlight = 1
        else:
            self.highlight = 0

class Sections:
    def __init__(self, screen, width, height):
        self.listc = []
        self.listx = []
        self.listy = []
        self.screen = screen
        for category in range(0, 4):
            for x in range(0,2):
                for y in range(0,11):
                    Point(x, y, category).drawself(self.screen, width, height)
                    self.listc.append(self.listx.append(self.listy.append(Point(x, y, category))))

        #to get a point do: listc[<category>][<x>][<y>]

    def getpoint(self, category, x, y):
        return self.listc[category][x][y]



