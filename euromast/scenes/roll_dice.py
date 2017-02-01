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
        self.rolled_number = None
        Button = formControl.Button
        game = self.vars['pygame']
        center_of_screen = game['center_of_screen']
        vertical_center_of_screen = game['vertical_center_of_screen']

        self.thrown_text = formControl.Text(
            (center_of_screen, vertical_center_of_screen + 100),
            '',
            self.vars['fonts']['medium'],
            pg.Color('red')
        )

        self.continue_btn = formControl.Button(
            (center_of_screen - 150, vertical_center_of_screen + 200, 300, 100),
            pg.Color('green'),
            self.next_player,
            text='Continue',
            font=self.vars['fonts']['medium'],
            hover_color = pg.Color("black")
        )

        self.dice = formControl.Image((self.vars['pygame']['width'] - 512, self.vars['pygame']['height'] * .4))

    def next_player(self, id):
        # stop sounds so we can use them again
        self.vars["sounds"]["dice_roll"].stop()

        current_player_index = self.persist['game_state']['current_player_index']

        self.persist['game_state']['players'][current_player_index].roll = self.rolled_number

        self.persist['game_state']['current_player_index'] += 1

        player_index = self.persist['game_state']['current_player_index']

        if player_index != len(self.persist['game_state']['players']) and player_index < len(self.persist['game_state']['players']):
            self.next_state = 'ROLL_DICE.BUTTON'
            self.done = True
            return
        self.persist['game_state']['current_player_index'] = 0
        self.next_state = 'SHOW_TURN_ORDER'
        self.done = True

    def startup(self, persistent):
        self.persist = persistent
        self.rolled_number = randint(1,6)

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        self.continue_btn.check_event(event)

    def update(self, dt):
        pass

    def draw(self, surface):
        # background
        surface.fill((255, 255, 255))

        # dice sound
        self.vars["sounds"]["dice_roll"].play()

        # dice image
        img = self.assets['wdlist']['dice{0}'.format(self.rolled_number)]

        self.dice.draw(surface, img)

        self.thrown_text.draw(surface)
        self.thrown_text.update_text("You rolled a {}!".format(self.rolled_number))
        #add roll to player
        self.continue_btn.update(surface);
