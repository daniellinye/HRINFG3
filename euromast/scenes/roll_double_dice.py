from components import stateManagment, player, formControl
from random import randint
import pygame as pg
class Scene(stateManagment.BaseScene):
    def __init__(self, screen, helpers):
        super(Scene, self).__init__()
        self.vars = helpers['vars']
        self.assets = helpers['assets']
        game = self.vars['pygame']
        self.white_dice_number = 0
        self.red_dice_number = 0
        self.white_dice = formControl.Image((game['width'] - 612, game['height']*.2))
        self.red_dice = formControl.Image((game['width'] - 412, game['height']*.2))
        self.result_text = formControl.Text(
            (game['width'] *.5  , (game['height'] / 2) + 20),
            '',
            self.vars['fonts']['medium'],
            pg.Color('black')
        )
    def startup(self, persistent):
        self.persist = persistent
        n1 = randint(1,6)
        n2 = randint(1,6)
        self.white_dice_number = 'dice{0}'.format(n1)
        self.red_dice_number = 'dice{0}'.format(n2)
        self.result_text.updateText('you rolled a {0} and a {1}'.format(
            n1,
            n2
        ))

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True

    def update(self, dt):
        pass

    def draw(self, surface):
        # formControl.Image((self.vars['pygame']['width'] - 512, self.vars['pygame']['height'] * .4), img).draw(surface)
        # self.player = player
        # background
        surface.fill((255, 255, 255))
        # dice image
        red_dice = self.assets['rdlist'][self.red_dice_number]
        white_dice = self.assets['wdlist'][self.white_dice_number]
        self.white_dice.draw(surface, white_dice)
        self.red_dice.draw(surface, red_dice)

        self.result_text.draw(surface)

        # text beneath image
        # self.text = libdef.DrawText(self.game.screen, "You rolled a {} and a {}!".format(self.number,self.number2), self.game.red, self.game.width-512, self.game.height*0.4)
        # text next to dice
        # self.text2 = libdef.DrawText(self.game.screen, "What type of question", (0, 0, 0), 180, self.game.height*0.2)
        # self.text3 = libdef.DrawText(self.game.screen, "How may steps", (0, 0, 0), 824, self.game.height * 0.2)
        # continue button
        # self.continu3 = libdef.DrawButton(self.game.screen, self.game.green, self.game.white, "Are you ready?", 250, 50, (self.game.width * 0.5),(self.game.height * 0.7))

        # flip updated screen
        # if self.continu3.collision():
        #     if self.number == 1 or self.number == 3 or self.number == 5:
        #         player.type = "open"
        #     else:
        #         player.type = "mul"
        #     if self.number2 == 1 or self.number2 == 2:
        #         player.steps = 1
        #     elif self.number2 == 3 or self.number2 == 4:
        #         player.steps = 2
        #     else:
        #         player.steps = 3
        #     return 10
