from components import stateManagment, player, formControl
from random import randint
import pygame as pg
class Scene(stateManagment.BaseScene):
    def __init__(self, screen, helpers):
        super(Scene, self).__init__()
        self.vars = helpers['vars']
        self.assets = helpers['assets']
        game = self.vars['pygame']
        self.next_state = 'CHOOSE_QUESTION'
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
        self.red_dice_text = formControl.Text(
            (game['width'] *.5, game['height'] / 2 + 50),
            '',
            self.vars['fonts']['medium'],
            pg.Color('red')
        )
        self.white_dice_text = formControl.Text(
            (game['width'] *.5, game['height'] / 2 + 80),
            '',
            self.vars['fonts']['medium'],
            pg.Color('black')
        )
        self.continue_btn = formControl.Button((game['center_of_screen'] - 100, game['height'] - 100, 200, 50),
            pg.Color('green'),
            self.next_scene,
            text='Continue',
            font=self.vars['fonts']['medium']
        )
    def next_scene(self, id):
        self.done = True
    def startup(self, persistent):
        self.persist = persistent
        game_state = self.persist['game_state']
        player = game_state['players'][game_state['current_player_index']]
        whide_dice_number = randint(1,6)
        red_dice_number = randint(1,6)
        self.white_dice_number = 'dice{0}'.format(whide_dice_number)
        self.red_dice_number = 'dice{0}'.format(red_dice_number)
        self.result_text.update_text('you rolled a {0} and a {1}'.format(
            whide_dice_number,
            red_dice_number
        ))
        question_type = None
        if whide_dice_number == 1 or whide_dice_number == 3 or whide_dice_number == 5:
            player.question_type = question_type = "open"
        else:
            question_type = "multiple choice"
            player.question_type = "multiple_choice"
        if red_dice_number == 1 or red_dice_number == 2:
            player.steps = 1
        elif red_dice_number == 3 or red_dice_number == 4:
            player.steps = 2
        else:
            player.steps = 3

        self.white_dice_text.update_text('White dice: you rolled for {0} questions'.format(question_type))
        self.red_dice_text.update_text('Red dice: you rolled for {0} steps'.format(red_dice_number))

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        self.continue_btn.check_event(event)
    def update(self, dt):
        pass

    def draw(self, surface):
        surface.fill((255, 255, 255))
        # dice image
        red_dice = self.assets['rdlist'][self.red_dice_number]
        white_dice = self.assets['wdlist'][self.white_dice_number]
        self.white_dice.draw(surface, white_dice)
        self.red_dice.draw(surface, red_dice)
        self.white_dice_text.draw(surface)
        self.red_dice_text.draw(surface)
        self.result_text.draw(surface)
        self.continue_btn.update(surface)
        # text beneath image
        # self.text = libdef.DrawText(self.game.screen, "You rolled a {} and a {}!".format(self.number,self.number2), self.game.red, self.game.width-512, self.game.height*0.4)
        # text next to dice
        # self.text2 = libdef.DrawText(self.game.screen, "What type of question", (0, 0, 0), 180, self.game.height*0.2)
        # self.text3 = libdef.DrawText(self.game.screen, "How may steps", (0, 0, 0), 824, self.game.height * 0.2)
        # continue button
        # self.continu3 = libdef.DrawButton(self.game.screen, self.game.green, self.game.white, "Are you ready?", 250, 50, (self.game.width * 0.5),(self.game.height * 0.7))
