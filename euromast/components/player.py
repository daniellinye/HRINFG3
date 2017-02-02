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
        self.moved = True
        self.roll = roll
        self.steps = None
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

    def incr_score(self, score):
        self.score = self.score + score

    def add_steps(self, steps):
        self.steps = steps

    def add_type(self, type):
        self.type = type

    def canmove(self):


        print("Can Move")
        self.moved = False

    def update(self):
        if self.moved == False:
            print(self.direction)
            if self.direction == "left" or self.direction[0] == "left":
                self.x -= 1
                self.moved = True
            elif self.direction == "right" or self.direction[0] == "right":
                self.x += 1
                self.moved = True
            elif self.direction == "up" or self.direction[0] == "up":
                self.y -= 1
                self.moved = True
            elif self.direction == "down" or self.direction[0] == "down":
                self.y += 1
                self.moved = True
        if self.x < 0:
            self.x = 7
        elif self.x > 7:
            self.x = 0
        if self.y < 0:
            self.lower_done = True
        print(self.x)
        print(self.y)


    def draw(self, screen, width, height, grid_height=10):
        if self.x%2 == 0:
            drawPoint = Point(2, self.y, self.x/4, 1)
            drawPoint.highlight
            drawPoint.drawself(screen, width, height, grid_height)
        else:
            drawPoint = Point(1, self.y, self.x/4, 1)

        if self.y < 0:
            TextInRect(screen, "Player {} Wins!".format(self.name), (255,255,255), (width / 2, height / 2),
                           pygame.font.SysFont("Arial", 40))
            return True

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
            pygame.draw.rect(screen, ((self.highlight*255),(self.highlight*255),(self.highlight*255)), [width/20 + width/4*self.category + width/8*self.x, height/grid_height *self.y + height/50, 8*(1+self.highlight), 8*(1+self.highlight)], 2)
        else:
            print("Player is not in game yet")
