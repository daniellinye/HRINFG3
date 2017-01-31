from components import stateManagment, formControl, player
from functools import partial
from model.model import Model
import pygame as pg


class Scene(stateManagment.BaseScene):
    def __init__(self, scene, helpers):
        super(Scene, self).__init__()
        self.vars = helpers['vars']
        self.assets = helpers['assets']
        self.game = game = self.vars['pygame']
        self.next_state = 'TURN_ORDER'
        self.tower = Grid()


    def next_scene(self, id):
        self.done = True

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        self.pick_category_btn.check_event(event)

    def startup(self, persistent):
        self.persist = persistent
        players = self.persist['game_state']['players']
        game = self.vars['pygame']
        for p in players:
            self.tower.addplayer(p)



    def update(self, dt):
        pass

    def draw(self, surface):
        surface.fill((0, 0, 0))
        self.tower.draw(self.game['screen'], self.game['width'], self.game['height'])
        for p in self.tower.players:
            p.draw(self.game['screen'], self.game['width'], self.game['height'])
        self.pick_category_btn.update(surface)

        for order_text in self.player_order:
            order_text.draw(surface)



class Point:
    def __init__(self, x, y, category, highlight):
        self.x = x
        self.y = y
        self.category = category
        self.highlight = highlight


    def highlight(self):
        if self.highlight == 0:
            self.highlight = 1
        else:
            self.highlight = 0

    def drawself(self, screen, width, height, grid_height=10):
        if self.x >= 0 and self.y >= 0:
            pg.draw.rect(screen, (0,0,(0+self.highlight)*255), [width/20 + width/4*self.category + width/8*self.x, height/grid_height *self.y + height/50, 8*(1+self.highlight), 8*(1+self.highlight)], 2)
        else:
            print("Player is not in game yet")



class Grid:
    def __init__(self, grid_width=2, grid_height=10):
        self.points =[]
        self.players =[]

        self.grid_width = grid_width
        self.grid_height = grid_height

        self.colorlist = ((255,0,0), (0,0,255), (255, 255, 0), (0,255, 0))


    def addplayer(self, player):
        if not self.players.__contains__(player):
            self.players.append(player)

#draw the grid and update whilst checking if someone wins
#if someone wins, def returns True
    def draw(self, screen, width, height):

        #draw backgroundcolors
        i = 1
        for counter in range(0,4):
            pygame.draw.rect(screen, self.colorlist[counter], [i, 0, width / 4, height], 0)
            i += width / 4


        #TODO fix player highlight and movement
        for c in range(0,4):
            templist = []
            for x in range(0, self.grid_width):
                for y in range(0, self.grid_height):
                    Point(x, y ,c, 0).drawself(screen, width, height, self.grid_height)
                    templist.append(Point(x, y ,c, 0))
                templist.append(Point(x, y ,c, 1))
            self.points.append(templist)

