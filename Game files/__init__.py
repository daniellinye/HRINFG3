#Copyright 2017 Daniel Lin

import psycopg2


import pygame #helps us access pygame

#RGB values (0-255) can also use other ways


class iV:
    def __init__(self):
        #init pygame
        pygame.init()
        #set values to be imported into another file

        self.font = pygame.font.SysFont("Times", 40)

        self.black = (0, 0, 0)
        self.green = (0, 255, 0)
        self.red = (255, 0, 0)
        self.white = (255,255,255)
        self.background = Background('./assets/background.PNG', [0,0])

        self.score = 0
        self.width = 800
        self.height = 600
        self.size = (self.width, self.height)

        self.screen = pygame.display.set_mode(self.size)

class Background(pygame.sprite.Sprite):
    def __init__(self, image, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class Main():
    def __init__(self):
        self.option = 0
        self.

init = iV()





