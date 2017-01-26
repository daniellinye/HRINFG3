#a beautiful grid pattern on the screen

import pygame

class Point:
    def __init__(self, x, y, category):
        self.x = x
        self.y = y
        self.category = category
        self.highlight = 0


    def returnx(self):
        return self.x

    def returny(self):
        return self.y

    def returnc(self):
        return self.category

    def drawself(self, screen, width, height, grid_height):
        pygame.draw.rect(screen, (0,0,0), [width/20 + width/4*self.category + width/8*self.x, height/grid_height *self.y + height/50, 8*(1+self.highlight), 8*(1+self.highlight)], 2)

    def highlight(self):
        if self.highlight == 0:
            self.highlight = 1
        else:
            self.highlight = 0

class Sections:
    def __init__(self, screen, width, height, categories=4, grid_width=2, grid_heigth=10):
        self.listc = []
        self.listx = []
        self.listy = []
        self.screen = screen
        #colors are: red, blue, yellow, green
        self.colorlist = ((255,0,0), (0,0,255), (255, 255, 0), (0,255, 0))
        i = 1
        for counter in range(0, 4):
            pygame.draw.rect(self.screen, self.colorlist[counter], [i, 0, width / 4, height], 0)
            i += width / 4
        for category in range(0, categories):
            for x in range(0, grid_width):
                for y in range(0, grid_heigth):
                    Point(x, y, category).drawself(self.screen, width, height, grid_heigth)
                    self.listc.append(self.listx.append(self.listy.append(Point(x, y, category))))


        #to get a point do: listc[<category>][<x>][<y>]

    def getpoint(self, category, x, y):
        return self.listc[category][x][y]



class Game:
    def __init__(self):
        # starts pygame
        pygame.init()

        self.font = pygame.font.SysFont("Times", 40)

        self.score = 0
        self.width = 800
        self.height = 600
        self.size = (self.width, self.height)
        self.font = pygame.font.SysFont("Arial", 40)

        self.screen = pygame.display.set_mode(self.size)
        running = True
        # check function




        while process_events():

            # draw logic
            self.screen.fill((0,0,0))


            menu = Sections(self.screen, self.width/2, self.height/2)


            # must also flip backscreen
            pygame.display.flip()


def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True





game = Game()