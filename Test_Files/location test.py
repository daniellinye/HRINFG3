#a beautiful grid pattern on the screen

import pygame

class Player:
    def __init__(self, player_id, name, score, position = (-1,11), roll = 0):
        self.id = player_id
        self.name = name
        self.score = score
        self.position = position
        self.roll = roll
        self.category = 0
        self.x = -1
        self.y = 11
        self.rect = (self.x, self.y)
        self.moved = True

    def relocate(self, c, x, y):
        self.c = c
        self.x = x
        self.y = y
        self.location = (x,y)

    def add_category(self, category):
        self.category = category

    def add_steps(self, steps):
        self.steps = steps

    def add_type(self, type):
        self.type = type


    def update(self, moves):
        if moves > 0:
            set = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and 0 > self.x >= 8:
                self.x -= 1
                set = True
            elif keys[pygame.K_RIGHT] and 0 >= self.x > 8:
                self.x += 1
                set = True
            if keys[pygame.K_UP] and 0 > self.y >= 8:
                self.y -= 1
                set = True
            elif keys[pygame.K_DOWN] and 0 >= self.y > 8:
                self.y += 1
                set = True

            if set == True:
                moves =- 1
                time.sleep(0.3)


class Point:
    def __init__(self, x, y, category):
        self.x = x
        self.y = y
        self.category = category
        self.highlight = 0


    def highlight(self):
        if self.highlight == 0:
            self.highlight = 1
        else:
            self.highlight = 0

    def drawself(self, screen, width, height, grid_height):
        if self.x >= 0 and self.y >= 0:
            pygame.draw.rect(screen, (0,0,0), [width/20 + width/4*self.category + width/8*self.x, height/grid_height *self.y + height/50, 8*(1+self.highlight), 8*(1+self.highlight)], 2)
        else:
            print("Player is not in game yet")



#call Sections to draw grid and players
#
class Sections:
    def __init__(self, screen, width, height, categories=4, grid_width=2, grid_heigth=10):
        self.listc = []
        self.listx = []
        self.listy = []
        self.players = []

        self.screen = screen
        self.width = width
        self.height = height
        self.categories = categories
        self.grid_width = grid_width
        self.grid_height = grid_heigth

        #colors are: red, blue, yellow, green
        self.colorlist = ((255,0,0), (0,0,255), (255, 255, 0), (0,255, 0))
        i = 1


        for counter in range(0, 4):
            i += self.width / 4
        if not self.players == None:
            for player in self.players:
                self.updateplayer(player)
        for category in range(0, self.categories):
            for x in range(0, self.grid_width):
                for y in range(0, self.grid_height):
                    self.listc.append(self.listx.append(self.listy.append(Point(x, y, category))))


    def draw(self, player):
        i = 1

        self.updateplayer(player)
        for counter in range(0, 4):
            pygame.draw.rect(self.screen, self.colorlist[counter], [i, 0, self.width / 4, self.height], 0)
            i += self.width / 4
        for category in range(0, self.categories):
            for x in range(0, self.grid_width):
                for y in range(0, self.grid_height):
                    Point(x, y, category).drawself(self.screen, self.width, self.height, self.grid_height)


    def getpoint(self, category, x, y):
        return self.listc[category]


    def updateplayer(self, player):
        if player.y >= 0:
            self.getpoint(player.category, player.x, player.y).highlight()
        else:
            print("player wins!")

    def moveplayer(self, player):
        self.players[player].update(self.steps)

    def addplayer(self, player):
        self.players.append(player)




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

        bob = Player(1, "Bob", 0)

        menu = Sections(self.screen, self.width, self.height)
        menu.addplayer(bob)

        while process_events():

            # draw logic
            self.screen.fill((0,0,0))

            menu.draw(menu.players[0])

            # must also flip backscreen
            pygame.display.flip()


def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True





game = Game()