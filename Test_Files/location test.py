import pygame

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
        pygame.draw.rect(screen, (0,0,0), [50 + width/4*self.category + width/8*self.x, 50 + height/10 *self.y + 10, 4, 4], 0)

    def hightlight(self):
        self.highlight = 1

class Sections:
    def __init__(self, screen, width, height):
        self.totallist = [0,50]
        self.screen = screen
        for category in range(0, 4):
            for x in range(0,2):
                for y in range(0,10):
                    Point(x, y, category).drawself(self.screen, width, height)




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


        self.colorlist = ((255,0,0), (0,0,255), (255, 255, 0), (0,255, 0))

        while process_events():

            # draw logic
            self.screen.fill((0,0,0))
            i = 1
            for counter in range(0,4):
                pygame.draw.rect(self.screen, self.colorlist[counter], [i, 0, self.width/4,self.height], 0)
                i += self.width/4


            menu = Sections(self.screen, self.width, self.height)


            # must also flip backscreen
            pygame.display.flip()


def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True





game = Game()