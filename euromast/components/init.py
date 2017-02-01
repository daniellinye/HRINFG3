import pygame as pg
from components import sound


class LoadVariables(object):
    def __init__(self):
        self.vars = {}
        self.vars['fonts'] = {
            "small": pg.font.SysFont('Arial', 18),
            "medium": pg.font.SysFont('Arial', 25),
            "large": pg.font.SysFont('Arial', 35),
            "extraLarge": pg.font.SysFont('Arial', 40)
        }
        self.vars['pygame'] = {
            'width': 1024,
            'height': 720,
            'center_of_screen': 1024 / 2,
            'vertical_center_of_screen': 720 / 2
        }
        
        self.vars["sounds"] = {
            "menu_theme": sound.LoadSound("./assets/sounds/menu_theme.wav", 0.7, -1),
            "main_theme": sound.LoadSound("./assets/sounds/main_theme.wav", 0.4, -1),
            "dice_roll": sound.LoadSound("./assets/sounds/dice_roll.wav"),
            "choose_question": sound.LoadSound("./assets/sounds/choose_question.wav", 1.0, -1),
            "question_theme": sound.LoadSound("./assets/sounds/question_theme.wav", 1.0, -1),
            "question_wrong": sound.LoadSound("./assets/sounds/question_wrong.wav"),
            "question_right": sound.LoadSound("./assets/sounds/question_right.wav")
        }

class LoadAssets(object):
    def __init__(self):
        self.assets = {'rdlist':{}, 'wdlist':{}}
        try:
            #cardbacks
            self.assets['lightsteelbluemul'] = pg.image.load('./assets/CBacks/BlueMul.png')
            self.assets['lightsteelblueop'] = pg.image.load('./assets/CBacks/BlueOp.png')
            self.assets['yellowgreenmul'] = pg.image.load('./assets/CBacks/GreenMul.png')
            self.assets['yellowgreenop'] = pg.image.load('./assets/CBacks/GreenMul.png')
            self.assets['tomatomul'] = pg.image.load('./assets/CBacks/RedMul.png')
            self.assets['tomatoop'] = pg.image.load('./assets/CBacks/RedOp.png')
            self.assets['yellowmul'] = pg.image.load('./assets/CBacks/YellowMul.png')
            self.assets['yellowop'] = pg.image.load('./assets/CBacks/YellowOp.png')
            self.assets['background-erasmus'] = pg.image.load('./assets/background.png')
            #cardfronts
            self.assets['bfront'] = pg.image.load('./assets/CFronts/Blue.png')
            self.assets['gfront'] = pg.image.load('./assets/CFronts/Green.png')
            self.assets['rfront'] = pg.image.load('./assets/CFronts/Red.png')
            self.assets['yfront'] = pg.image.load('./assets/CFronts/Yellow.png')

            #dice
            for x in range(1,7):
                self.assets['rdlist']['dice{0}'.format(x)] = pg.image.load('./assets/red_dice/{0}.png'.format(x))
                self.assets['wdlist']['dice{0}'.format(x)] = pg.image.load('./assets/white_dice/{0}.png'.format(x))
        except Exception as e:
            print(e)
            print("Warning: Some files are missing")
