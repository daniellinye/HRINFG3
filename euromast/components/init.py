import pygame as pg

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
        self.vars['dummyQuestions'] = [{
            'id': 1,
            'name': 'Hoeveel tulpen zitten in een dozijn',
            'type': 'multiple_choice',
            'color': 'green',
            'answers': [
                {'id': 1, 'name': 'Wrong answer 2', 'isCorrect': False},
                {'id': 2, 'name': 'Long ass Wrong answer 20000000000000000000', 'isCorrect': False},
                {'id': 3,  'name': 'Correct answer', 'isCorrect': True}
            ]
        }]

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
