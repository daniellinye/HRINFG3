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
        self.players = None
        self.button = formControl.Button(
            (game['width'] - 200, 300 , 200, 50),
            pg.Color('pink'),
            self.next_scene,
            text="Stuff"
        )

        euromast0 = self.assets['euromast0']
        euromast1 = self.assets['euromast1']
        euromast2= self.assets['euromast2']
        euromast3 = self.assets['euromast3']
        self.between_points = 20
        self.v_between_points = 28
        self.between_towers = 200
        self.first_point_y = game['height'] -43
        self.left_x = 115
        width = 15
        height = 15
        self.begin_middle = 93
        v_center_of_screen = game['vertical_center_of_screen']
        self.t = ['t1','t2', 't3', 't4']
        self.towers = {'t1': {}, 't2': {}, 't3': {}, 't4':{}}
        self.begin = 85
        for t in self.t:
            cat = None
            if t == 't1':
                cat = 'geografie'
            elif t == 't2':
                cat = "entertainment"
            elif t == "t3":
                cat = 'sport'
            elif t == 't4':
                cat = 'historie'

            self.towers[t] = {
                "top_category": cat,
                "left": {
                    "1": (self.begin, self.first_point_y, width, height),
                    "2": (self.begin, (self.first_point_y - 2) - self.v_between_points, width, height),
                    "3": (self.begin, (self.first_point_y - 4) - (self.v_between_points * 2), width, height),
                    "4": (self.begin, (self.first_point_y - 6) - (self.v_between_points * 3), width, height),
                    "5": (self.begin, (self.first_point_y - 8) - (self.v_between_points * 4), width, height),
                    "6": (self.begin, (self.first_point_y - 10) - (self.v_between_points * 5), width, height),
                    "7": (self.begin, (self.first_point_y - 12) - (self.v_between_points * 6), width, height),
                    "8": (self.begin, (self.first_point_y - 14) - (self.v_between_points * 7), width, height),
                    "9": (self.begin, (self.first_point_y - 16) - (self.v_between_points * 8), width, height),
                    "10": (self.begin, (self.first_point_y - 18) - (self.v_between_points * 9), width, height),
                },
                "middle": {
                    "11": (self.begin_middle, v_center_of_screen - 128, width, height),
                    "12": (self.begin_middle, v_center_of_screen - 148, width, height),
                    "13": (self.begin_middle, v_center_of_screen - 178, width, height),
                    "14": (self.begin_middle, v_center_of_screen - 211, width, height),
                    "15": (self.begin_middle, v_center_of_screen - 234, width, height),
                    "16": (self.begin_middle, v_center_of_screen - 262, width, height),
                },
                "right": {
                    "1": (self.begin + self.between_points, self.first_point_y, width, height),
                    "2": (self.begin + self.between_points,  (self.first_point_y - 2) - self.v_between_points , width, height),
                    "3": (self.begin + self.between_points,  (self.first_point_y - 4) - (self.v_between_points * 2), width, height),
                    "4": (self.begin + self.between_points,  (self.first_point_y - 6) - (self.v_between_points * 3), width, height),
                    "5": (self.begin + self.between_points,  (self.first_point_y - 8) - (self.v_between_points * 4), width, height),
                    "6": (self.begin + self.between_points,  (self.first_point_y - 10)- (self.v_between_points * 5), width, height),
                    "7": (self.begin + self.between_points,  (self.first_point_y - 12) - (self.v_between_points * 6), width, height),
                    "8": (self.begin + self.between_points,  (self.first_point_y - 14) - (self.v_between_points * 7), width, height),
                    "9": (self.begin + self.between_points,  (self.first_point_y - 16) - (self.v_between_points * 8), width, height),
                    "10": (self.begin + self.between_points,  (self.first_point_y - 18) - (self.v_between_points * 9), width, height)
                }
            }
            self.begin += self.between_towers
            self.begin_middle += self.between_towers

        self.tower0 = formControl.Image((100, 365), self.assets['euromast0'])
        self.tower1 = formControl.Image((300, 365), self.assets['euromast1'])
        self.tower2 = formControl.Image((500, 365), self.assets['euromast2'])
        self.tower3 = formControl.Image((700, 365), self.assets['euromast3'])


    def next_scene(self):
        self.persist['game_state']['current_player_index'] += 1

    def next_scene(self, id):
        game_state = self.persist['game_state']
        current_player_index = game_state['current_player_index']
        players = game_state['players']
        if len(players) == current_player_index + 1:
            self.persist['game_state']['current_player_index'] = 0
        else:
            self.persist['game_state']['current_player_index'] += 1
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
        for player in self.players:
            if player.tower['current_steps'] > 16:
                self.persist['game_state']['winner'] = player
                self.next_state = "END_SCREEN"
                self.done = True
        self.colors = [pg.Color('darkslategray'), pg.Color('purple'), pg.Color('brown'), pg.Color('black')]

    def update(self, dt):
        pass

    def draw(self, surface):
        surface.fill(pg.Color('white'))
        self.tower0.draw(surface)
        self.tower1.draw(surface)
        self.tower2.draw(surface)
        self.tower3.draw(surface)
        self.button.update(surface)
        x = 0
        for player in self.players:
            if player.tower['current_steps'] > 0:
                if player.tower['current_steps'] > 10:
                    player.tower['current_pos'] = 'middle'
                tower = player.tower
                print(tower['current_steps'])
                print(self.towers[tower['tower_id']][tower['current_pos']])
                if str(tower['current_steps']) in self.towers[tower['tower_id']][tower['current_pos']]:
                    pg.draw.rect(surface, self.colors[x], self.towers[tower['tower_id']][tower['current_pos']][str(tower['current_steps'])])
                    x += 1
