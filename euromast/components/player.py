import uuid

class createPlayer(object):
    def __init__(self, name, roll=0, position = (-1,11)):
        self.id = uuid.uuid4()
        self.name = name
        self.score = 0
        self.position = position
        self.direction = None
        self.category = 0
        self.x = -1
        self.y = 11
        self.rect = (self.x, self.y)
        self.moved = True
        self.roll = roll

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
