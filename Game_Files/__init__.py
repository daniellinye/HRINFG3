# Copyright 2017 Daniel Lin, Jasper Andriessen
"""
Classes in this file:
 - iV(Initialises the game)
 - Background(Draws the background of the game)
 - DrawButton(Draws a clickable button with text)
"""

# Imports
import psycopg2
import pygame  # helps us access pygame
from rules import Rules


class IV:
    def __init__(self):
        # init pygame
        pygame.init()
        # set values to be imported into another file

        # system values
        self.option = 0
        self.mousepos = pygame.mouse.get_pos()

        self.font = pygame.font.SysFont("Times", 40)
        self.rulesfont = pygame.font.SysFont("Times", 20)

        self.black = (0, 0, 0)
        self.green = (0, 255, 0)
        self.red = (255, 0, 0)
        self.white = (255,255,255)


        # screen values
        self.rules = Rules().editedrules
        self.score = 0
        self.width = 1024
        self.height = 768
        self.size = (self.width, self.height)
        self.clock = pygame.time.Clock()
        self.fps = 60

        self.screen = pygame.display.set_mode(self.size)

        #asset imports:
        self.background = Background('./assets/background.jpeg', [0, 0])

        #cardbacks
        self.bbackmul = pygame.image.load('./assets/CBacks/BlueMul.png')
        self.bbackop = pygame.image.load('./assets/CBacks/BlueOp.png')
        self.gbackmul = pygame.image.load('./assets/CBacks/GreenMul.png')
        self.gbackop = pygame.image.load('./assets/CBacks/GreenMul.png')
        self.rbackmul = pygame.image.load('./assets/CBacks/RedMul.png')
        self.rbackop = pygame.image.load('./assets/CBacks/RedOp.png')
        self.ybackmul = pygame.image.load('./assets/CBacks/YellowMul.png')
        self.ybackop = pygame.image.load('./assets/CBacks/YellowOp.png')

        #cardfronts
        self.bfront = pygame.image.load('./assets/CFronts/Blue.png')
        self.gfront = pygame.image.load('./assets/CFronts/Green.png')
        self.rfront = pygame.image.load('./assets/CFronts/Red.png')
        self.yfront = pygame.image.load('./assets/CFronts/Yellow.png')

        #whitedice
        self.wd1 = pygame.image.load('./assets/white_dice/1.png')
        self.wd2 = pygame.image.load('./assets/white_dice/2.png')
        self.wd3 = pygame.image.load('./assets/white_dice/3.png')
        self.wd4 = pygame.image.load('./assets/white_dice/4.png')
        self.wd5 = pygame.image.load('./assets/white_dice/5.png')
        self.wd6 = pygame.image.load('./assets/white_dice/6.png')


        #reddice
        self.rd1 = pygame.image.load('./assets/red_dice/1.png')
        self.rd2 = pygame.image.load('./assets/red_dice/2.png')
        self.rd3 = pygame.image.load('./assets/red_dice/3.png')
        self.rd4 = pygame.image.load('./assets/red_dice/4.png')
        self.rd5 = pygame.image.load('./assets/red_dice/5.png')
        self.rd6 = pygame.image.load('./assets/red_dice/6.png')



class Background(pygame.sprite.Sprite):
    def __init__(self, image, location):
        # Call Sprite initializer
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


class DrawButton:
    def __init__(self, screen, b_color, t_color, text, b_width, b_height, position_x, position_y):
        self.screen = screen
        self.b_color = b_color
        self.t_color = t_color
        self.text = text
        self.b_width = b_width
        self.b_height = b_height
        self.position_x = position_x
        self.position_y = position_y

        self.draw()

    def draw(self, image=""):
        pygame.draw.rect(self.screen, self.b_color or image, [self.position_x, self.position_y, self.b_width, self.b_height], 0)
        text = init.font.render(str(self.text), 1, self.t_color)
        init.screen.blit(text, (self.position_x + self.b_width*0.5 - text.get_width()*0.5,
                                self.position_y + self.b_height*0.5 - text.get_height()*0.5))

    def collision(self, new_color=(0, 0, 0)):
        # Check for collision with mouse and change background color
        mouse = pygame.mouse.get_pos()
        if (mouse[0] in range(int(self.position_x), int(self.position_x + self.b_width))) \
                and (mouse[1] in range(int(self.position_y), int(self.position_y + self.b_height))):
            self.b_color = new_color
            self.draw()

            # If pressed on a button change state
            if pygame.mouse.get_pressed()[0]:
                return True


init = IV()





