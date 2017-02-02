from components import stateManagment, formControl, helpers
from functools import partial
import pygame as pg

SCENE_NAME = 'CHOOSE_DIRECTION'
class Scene(stateManagment.BaseScene):
    def __init__(self, screen, helpers):
        super(Scene, self).__init__(helpers)
        self.vars = helpers['vars']
        self.current_state = SCENE_NAME
        self.assets = helpers['assets']
        self.player = None
        self.game = game = self.vars['pygame']
        self.turn_text = formControl.Text(
            (game['width']*.5, game['height']*.5),
            '',
            self.vars['fonts']['large'],
            pg.Color('black')
        )

        self.left_direction_btn = formControl.Button(
            (20, 20, 300, 300),
            (0,0,255),
            partial(self.nextPlayer, 'left'),
            click_sound=self.sounds.effects['click_sound'],
            text="left",
            font=self.vars['fonts']['large']
        )

        self.up_direction_btn = formControl.Button(
            (20, game['height']-310, 300, 300),
            (255,0,0),
            partial(self.nextPlayer, 'up'),
            click_sound=self.sounds.effects['click_sound'],
            text="up",
            font=self.vars['fonts']['large']
        )

        self.right_direction_btn = formControl.Button(
            (game['width'] - 320, 20, 300, 300),
            (0,255,0),
            partial(self.nextPlayer, 'right'),
            click_sound=self.sounds.effects['click_sound'],
            text="right",
            font=self.vars['fonts']['large']
        )


        self.down_direction_btn = formControl.Button(
            (game['width'] - 320, game['height']-310, 300, 300),
            (255,255,0),
            partial(self.nextPlayer, 'down'),
            click_sound=self.sounds.effects['click_sound'],
            text='down',
            font=self.vars['fonts']['large']
        )

    def nextPlayer(self, direction, id):
        self.player.set_direction(direction)

        self.persist['game_state']['reuse_scene'] = self.next_state
        self.persist['game_state']['skip_to_scene'] = 'ROLL_DOUBLE_DICE'

        self.done = True

    def startup(self, persistent):
        self.next_state = 'ROLL_DICE.BUTTON'
        self.persist = persistent
        current_player_idx = self.persist['game_state']['current_player_index']
        self.player = self.persist['game_state']['players'][current_player_idx]

    def get_event(self, event):
        helpers.check_paused_event(self, event)
        self.up_direction_btn.check_event(event)
        self.left_direction_btn.check_event(event)
        self.down_direction_btn.check_event(event)
        self.right_direction_btn.check_event(event)


    def update(self, dt):
        self.turn_text.update_text('{0} choose a direction'.format(self.player.name))

    def draw(self, surface):
        # background
        surface.fill((255, 255, 255))

        self.left_direction_btn.update(surface)

        self.right_direction_btn.update(surface)

        self.down_direction_btn.update(surface)

        self.up_direction_btn.update(surface)


        self.turn_text.draw(surface)
