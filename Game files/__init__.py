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

        self.score = 0
        self.width = 800
        self.height = 600
        self.size = (self.width, self.height)

        self.screen = pygame.display.set_mode(self.size)









