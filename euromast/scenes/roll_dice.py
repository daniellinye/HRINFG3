from components import stateManagment, formControl
from random import randint
import pygame as pg

class Scene(stateManagment.BaseScene):
    def __init__(self, screen, helpers):
        super(Scene, self).__init__()
        self.screen = screen
        self.done = False
        self.next_state = 'SHOW_TURN_ORDER'
        self.vars = helpers['vars']
        self.assets =  helpers['assets']
        self.screen_color = pg.Color('white')
        Button = formControl.Button
        game = self.vars['pygame']
        self.centerOfScreen = (game['width'] / 2)
        self.vertical_center_of_screen = (game['height'] / 2)

        self.thrownText = formControl.Text((self.centerOfScreen - 100, self.vertical_center_of_screen - 100),
            '',
            self.vars['fonts']['medium'],
            pg.Color('red')
        )
        self.continueBtn = formControl.Button((self.centerOfScreen - 150, self.vertical_center_of_screen - 50, 300, 100),
            pg.Color('green'),
            self.next_player,
            text='Continue',
            font=self.vars['fonts']['medium'])

    def next_player(self):
        current_player_index = self.persist['game_state']['currentPlayerIndex']

        self.persist['game_state']['players'][current_player_index].roll = self.thrownNumber

        self.persist['game_state']['currentPlayerIndex'] += 1

        playerIndex = self.persist['game_state']['currentPlayerIndex']

        if playerIndex != len(self.persist['game_state']['players']) and playerIndex < len(self.persist['game_state']['players']):
            self.next_state = 'ROLL_DICE.BUTTON'
            self.done = True
            return
        self.persist['game_state']['currentPlayerIndex'] = 0
        self.next_state = 'SHOW_TURN_ORDER'
        self.done = True

    def startup(self, persistent):
        self.persist = persistent
        self.thrownNumber = randint(1,6)

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        self.continueBtn.check_event(event)

    def update(self, dt):
        pass

    def draw(self, surface):
        # background
        surface.fill((255, 255, 255))
        # dice image
        img = self.assets['wdlist']['dice{0}'.format(self.thrownNumber)]

        formControl.Image((self.vars['pygame']['width'] - 512, self.vars['pygame']['height'] * .4), img).draw(surface)

        self.thrownText.draw(surface)
        self.thrownText.updateText("You rolled a {}!".format(self.thrownNumber))
        #add roll to player
        self.continueBtn.update(surface);
