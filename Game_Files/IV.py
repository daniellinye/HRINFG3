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
from game import Game
from Dice import DrawDiceScreen
import pygame_textinput
from libdef import *


class IV:
    def __init__(self):
        # init pygame
        pygame.init()
        # set values to be imported into another file

        # system values
        self.option = 0
        self.mousepos = pygame.mouse.get_pos()

        self.page = 0
        self.ruleslist = Rules().ruleslist


        self.font = pygame.font.SysFont("Arial", 40)
        self.rulesfont = pygame.font.SysFont("Arial", 18)

        self.textinput = pygame_textinput.TextInput()

        self.black = (0, 0, 0)
        self.green = (0, 255, 0)
        self.red = (255, 0, 0)
        self.white = (255,255,255)
        self.blue = (30,144,255)
        self.yellow = (255,255,0)
        self.colors = {
            'black': self.black,
            'green': self.green,
            'yellow': self.yellow,
            'blue': self.blue,
            'red': self.red,
            'white': self.white
        }
        self.colorlist = ((255,0,0), (0,0,255), (255, 255, 0), (0,255, 0))

        # screen values
        self.main_game = Game(self)
        self.dice = DrawDiceScreen(self)
        self.score = 0
        self.width = 1024
        self.height = 720
        self.size = (self.width, self.height)
        self.clock = pygame.time.Clock()
        self.fps = 30

        self.screen = pygame.display.set_mode(self.size)

        self.grid = Sections(self.screen, self.width, self.height, [])

        try:
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

            #dice
            for x in range(1,7):
                self.rdlist = pygame.image.load('./assets/red_dice/{}.png'.format(x))
                self.wdlist = pygame.image.load('./assets/white_dice/{}.png'.format(x))
        except:
            print("Warning: Some files are missing")

        self.dummyQuestions = [{
            'id': 1,
            'name': 'Hoeveel tulpen zitten in een dozijn',
            'type': 'multiple_choice',
            'answers': [
                {'id': 1, 'name': 'Wrong answer 2', 'isCorrect': False},
                {'id': 2, 'name': 'Long ass Wrong answer 20000000000000000000', 'isCorrect': False},
                {'id': 3,  'name': 'Correct answer', 'isCorrect': True}
            ]
        }, {
            'id': 2,
            'name': 'Wat is 1 + 1',
            'type': 'open',
            'answers': [
                {'id': 3,  'name': 'Correct answer', 'isCorrect': True}
            ]
        }, {
            'id': 3,
            'name': 'Hoeveel tulpen zitten in een dozijn',
            'type': 'multiple_choice',
            'answers': [
                {'id': 1, 'name': 'Wrong answer 2', 'isCorrect': False},
                {'id': 2, 'name': 'Long ass Wrong answer 20000000000000000000', 'isCorrect': False},
                {'id': 3,  'name': 'Correct answer', 'isCorrect': True}
            ]
        }, {
            'id': 4,
            'name': 'Wat is 1 + 1',
            'type': 'multiple_choice',
            'answers': [
                {'id': 1, 'name': 'Wrong answer 2', 'isCorrect': False},
                {'id': 2, 'name': 'Long ass Wrong answer 20000000000000000000', 'isCorrect': False},
                {'id': 3,  'name': 'Correct answer', 'isCorrect': True}
            ]
        },
        {
            'id': 5,
            'name': 'Hoeveel tulpen zitten in een dozijn',
            'type': 'open',
            'answers': [
                {'id': 3,  'name': 'Correct answer', 'isCorrect': True}
            ]
        }, {
            'id': 6,
            'name': 'Wat is 1 + 1',
            'type': 'open',
            'answers': [
                {'id': 3,  'name': 'Correct answer', 'isCorrect': True}
            ]
        },
        {
            'id': 7,
            'name': 'Hoeveel tulpen zitten in een dozijn',
            'type': 'multiple_choice',
            'answers': [
                {'id': 1, 'name': 'Wrong answer 2', 'isCorrect': False},
                {'id': 2, 'name': 'Long ass Wrong answer 20000000000000000000', 'isCorrect': False},
                {'id': 3,  'name': 'Correct answer', 'isCorrect': True}
            ]
        }, {
            'id': 8,
            'name': 'Wat is 1 + 1',
            'type': 'multiple_choice',
            'answers': [
                {'id': 1, 'name': 'Wrong answer 2', 'isCorrect': False},
                {'id': 2, 'name': 'Long ass Wrong answer 20000000000000000000', 'isCorrect': False},
                {'id': 3,  'name': 'Correct answer', 'isCorrect': True}
            ]
        },
        {
            'id': 7,
            'name': 'Hoeveel tulpen zitten in een dozijn',
            'type': 'open',
            'answers': [
                {'id': 1, 'name': 'Correct answer', 'isCorrect': True},
            ]
        }, {
            'id': 8,
            'name': 'Wat is 1 + 1',
            'type': 'multiple_choice',
            'answers': [
                {'id': 1, 'name': 'Wrong answer 2', 'isCorrect': False},
                {'id': 2, 'name': 'Long ass Wrong answer 20000000000000000000', 'isCorrect': False},
                {'id': 3,  'name': 'Correct answer', 'isCorrect': True}
            ]
        }]

init = IV()
