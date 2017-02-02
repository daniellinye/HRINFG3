import uuid
import pygame
from components import stateManagment, formControl, t1, t2, t3, t4


class createPlayer(object):
    def __init__(self, name, roll=0, position = (0,11)):
        self.id = uuid.uuid4()
        self.name = name
        self.score = 0
        self.streak = 0
        self.position = position
        self.direction = None
        self.category_name = None
        self.category = 0
        self.x = 0
        self.y = 11
        self.rect = (self.x, self.y)
        self.was_correct = None
        self.moved = True
        self.tower = {
            "tower_id": None, #t1 t2 t3 t4
            "current_pos": "left", # middle left right,
            "current_steps": 0
        }
        self.roll = roll
        self.steps = 0
        self.question_type = None
        self.current_question = None
        self.answer_questions_id = ()
        self.lower_done = False
        self.upper_done = False

    def relocate(self, c, x, y):
        self.c = c
        self.x = x
        self.y = y
        self.location = (x,y)
    def set_roll(self, rolled):
        self.roll = rolled

    def get_name(self):
        return self.name
    def set_direction(self, direction):
        self.direction = direction

    def move_player_horizontal(self):
        if self.tower['tower_id'] == 't1':
            t1.set_direction(self)
        elif self.tower['tower_id'] == 't2':
            t2.set_direction(self)
        elif self.tower['tower_id'] == 't3':
            t3.set_direction(self)
        elif self.tower['tower_id'] == 't4':
            t4.set_direction(self)

        if self.tower['tower_id']  == 't1':
            self.category = {'id': 1, 'name': 'entertainment', 'color': 'tomato'}
        elif self.tower['tower_id']  == 't2':
            self.category = {'id': 2, 'name': 'sport', 'color': 'lightsteelblue'}
        elif self.tower['tower_id'] == 't3':
            self.category = {'id': 3, 'name': 'historie', 'color': 'yellow'}
        elif self.tower['tower_id'] == 't4':
            self.category = {'id': 4, 'name': 'geografie', 'color': 'yellowgreen'}

        if self.tower['tower_id'] == 't1' and self.tower['current_pos'] == 'middle':
            self.category = {'id': 4, 'name': 'geografie', 'color': 'yellowgreen'}
        elif self.tower['tower_id'] == 't2' and self.tower['current_pos'] == 'middle':
            self.category = {'id': 1, 'name': 'entertainment', 'color': 'tomato'}
        elif self.tower['tower_id'] == 't3' and self.tower['current_pos'] == 'middle':
            self.category = {'id': 2, 'name': 'sport', 'color': 'lightsteelblue'}
        elif self.tower['tower_id'] == 't4' and self.tower['current_pos'] == 'middle':
            self.category = {'id': 3, 'name': 'historie', 'color': 'yellow'}
    def move_player_vertical(self):
        if self.tower['current_steps'] > 10:
            self.tower['current_pos'] = 'middle'

        if self.tower['tower_id'] == 't1' and self.tower['current_steps'] > 10:
            self.category = {'id': 4, 'name': 'geografie', 'color': 'yellowgreen'}
        elif self.tower['tower_id'] == 't2' and self.tower['current_steps'] > 10:
            self.category = {'id': 1, 'name': 'entertainment', 'color': 'tomato'}
        elif self.tower['tower_id'] == 't3' and self.tower['current_steps'] > 10:
            self.category = {'id': 2, 'name': 'sport', 'color': 'lightsteelblue'}
        elif self.tower['tower_id'] == 't4' and self.tower['current_steps'] > 10:
            self.category = {'id': 3, 'name': 'historie', 'color': 'yellow'}

    def set_category(self, category):
        self.category = category
        if category['name'] == 'entertainment':
            self.tower['tower_id'] = 't1'
        elif category['name'] == 'sport':
            self.tower['tower_id'] = 't2'
        elif category['name'] == 'geografie':
            print('setting to geo')
            self.tower['tower_id'] = 't4'
        elif category['name'] == 'historie':
            print('setting to histor')
            self.tower['tower_id'] = 't3'

    def add_type(self, type):
        self.type = type
