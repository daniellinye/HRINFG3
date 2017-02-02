from components import stateManagment, formControl, player, helpers
from functools import partial
from model.model import Model
import pygame as pg


SCENE_NAME = "SHOW_TOWER"
class Scene(stateManagment.BaseScene):
    def __init__(self, scene, helpers):
        super(Scene, self).__init__(helpers)
        self.current_state = SCENE_NAME
        self.vars = helpers['vars']
        self.assets = helpers['assets']
        self.game = game = self.vars['pygame']
        self.tower_upper = Grid(1, 5)
        self.tower_lower = Grid()
        self.players = None
        self.button = formControl.Button(
            [0, self.game['height']/5, 200, 50],
            (0, 0, 0),
            self.next_scene(),
            text="Stuff"
        )





    def next_scene(self):

        self.done = True
        self.next_state = "CHOOSE_DIRECTION"


    def get_event(self, event):
        helpers.check_paused_event(self, event)
        self.button.check_event(event)



    def startup(self, persistent):
        self.next_state = 'CHOOSE_DIRECTION'
        self.persist = persistent
        self.players = self.persist['game_state']['players']
        game_state = self.persist['game_state']
        pindex = game_state['current_player_index']
        player = game_state['players'][pindex]
        player.canmove()
        player.update()

        if player.lower_done:
            self.tower_upper.addplayer(player)
            player.y = 4
            player.upper_done = True
            player.lower_done = False
        elif not player.lower_done and player.upper_done:
            self.tower_upper.addplayer(player)
            if player.y < 0:
                player.lower_done = True
        elif player.lower_done and player.upper_done:
            #TODO make victory screen
            pass
        else:
            self.tower_lower.addplayer(player)
            if player.y < 0:
                player.lower_done = True




    #formControl.Button([x,y,w,h],[color],function(where thebuttongoes to), text=something)
    def update(self, dt):
        pass

    def draw(self, surface):
        surface.fill((0,0,0))
        self.tower_upper.draw(surface, self.game['width'], self.game['height']/5, 0)
        self.tower_lower.draw(surface, self.game['width'], self.game['height']/2.5, self.game['height']/4 + 50)
        for p in self.players:
            p.draw(surface, self.game['width'], self.game['height'])
        self.button.update(surface)






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
    def draw(self, screen, width, height, repos):

        #draw backgroundcolors
        i = 1
        for counter in range(0,4):
            pg.draw.rect(screen, self.colorlist[counter], [i, repos, width / 4, height+repos], 0)
            i += width / 4

        for c in range(0,4):
            templist = []
            for x in range(0, self.grid_width):
                for y in range(0, self.grid_height):
                    if not self.players == []:
                        for player in self.players:
                            if (((player.x+2)%(x+2) == 0 or player.x/2%(x+2) == 0) and player.y == y and c == (player.x+2)/2) or \
                                    (((player.x+2)%(x+2) == 0 or player.x/2%(x+2) == 0) and player.y == y and c == (player.x-1)/2):
                                Point(x, y, c, 1).drawself(screen, width, height + repos, self.grid_height, repos)
                            else:
                                Point(x, y ,c, 0).drawself(screen, width, height+repos, self.grid_height, repos)
                                templist.append(Point(x, y ,c, 0))
                    else:
                        Point(x, y, c, 0).drawself(screen, width, height + repos, self.grid_height, repos)
                        templist.append(Point(x, y, c, 0))

                templist.append(Point(x, y ,c, 1))
            self.points.append(templist)
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

    def drawself(self, screen, width, height, grid_height=10, repos=0):
        if self.x >= 0 and self.y >= 0:
            pg.draw.rect(screen, ((self.highlight*255),(self.highlight*255),(self.highlight*255)),
                         [width/20 + width/4*self.category + width/8*self.x,
                          height/grid_height *self.y + height/50 + repos,
                          8*(1+self.highlight),
                          8*(1+self.highlight)], 2)
        else:
            print("Player is not in game yet")
