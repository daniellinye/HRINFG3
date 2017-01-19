#Copyright 2017 Daniel Lin

import psycopg2


import pygame #helps us access pygame

#RGB values (0-255) can also use other ways


class iV:
    def __init__(self):
        #init pygame
        pygame.init()
        #set values to be imported into another file

        #system values
        self.option = 0

        self.mousepos = pygame.mouse.get_pos()

        self.font = pygame.font.SysFont("Times", 40)

        self.black = (0, 0, 0)
        self.green = (0, 255, 0)
        self.red = (255, 0, 0)
        self.white = (255,255,255)
        self.background = Background('./assets/background.PNG', [0,0])

        #screen values
        self.score = 0
        self.width = 1024
        self.height = 768
        self.size = (self.width, self.height)
        self.clock = pygame.time.Clock()
        self.fps = 60

        self.screen = pygame.display.set_mode(self.size)


class Background(pygame.sprite.Sprite):
    def __init__(self, image, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location



class MouseInput():
    def __init__(self, x, y, input):
        #TODO have a mouserange
        if init.mousepos == (x,y) and pygame.mouse.get_pressed():
            return True
        else:
            return False



init = iV()





