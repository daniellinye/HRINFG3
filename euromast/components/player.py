import uuid
import pygame
from components import stateManagment, formControl

class createPlayer(object):
    def __init__(self, name, roll=0, position = (-1,11)):
        self.id = uuid.uuid4()
        self.name = name
        self.score = 0
        self.position = position
        self.direction = None
        self.category = None
        self.x = -1
        self.y = 11
        self.rect = (self.x, self.y)
        self.moved = True
        self.roll = roll
        self.steps = None
        self.question_type = None
        self.current_question = None
        self.answer_questions_id = ()

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

    def incr_score(self, score):
        self.score = self.score + score

    def add_steps(self, steps):
        self.steps = steps

    def add_type(self, type):
        self.type = type

    def canmove(self):
        self.moved = False

    def update(self):
        print(self.direction)
        if self.moved == False:
            if self.direction == "Left" or self.direction[0] == "Left":
                self.x -= 1
                self.moved = True
            elif self.direction == "Right" or self.direction[0] == "Right":
                self.x += 1
                self.moved = True
            elif self.direction == "Up" or self.direction[0] == "Up":
                self.y -= 1
                self.moved = True
            elif self.direction == "Down" or self.direction[0] == "Down":
                self.y += 1
                self.moved = True

        print(self.x)
        print(self.y)


    def draw(self, screen, width, height, grid_height=10):
        pygame.draw.rect(screen, (255, 255,255),
                         [width / 20 + width / 8 * self.x,
                          height / grid_height * self.y + height / 50, 8,
                          8], 2)

        if self.y < 0:
            TextInRect(screen, "Player {} Wins!".format(self.name), (0, 0, 0), (width / 2, height / 2),
                           pygame.font.SysFont("Arial", 40))
            return True