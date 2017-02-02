import uuid
import pygame
from components import stateManagment, formControl


class createPlayer(object):
    def __init__(self, name, roll=0, position = (0,11)):
        self.id = uuid.uuid4()
        self.name = name
        self.score = 0
        self.position = position
        self.direction = None
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

    def set_category(self, category):
        self.category = category
        if category['name'] == 'entertainment':
            self.tower['tower_id'] = 't1'
        elif category['name'] == 'sport':
            self.tower['tower_id'] = 't2'
        elif category['name'] == 'geografie':
            self.tower['tower_id'] = 't4'
        elif category['name'] == 'historie':
            self.tower['tower_id'] == 't3'

    def add_type(self, type):
        self.type = type
