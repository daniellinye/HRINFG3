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
        self.background = formControl.Image((0, 0), self.assets['game-category'])
        self.turn_text = formControl.Text(
            (game['width']*.5, game['height']*.5),
            '',
            self.vars['fonts']['large'],
            pg.Color('black')
        )

        self.left_direction_btn = formControl.Button(
            (10, game["height"]/2-150, 300, 300),
            (142, 96, 175),
            partial(self.nextPlayer, 'left'),
            click_sound=self.sounds.effects['click_sound'],
            font=self.vars['fonts']['large']
        )

        self.up_direction_btn = formControl.Button(
            (game['width']/2-150, 10, 300, 300),
            (142, 96, 175),
            partial(self.nextPlayer, 'up'),
            click_sound=self.sounds.effects['click_sound'],
            font=self.vars['fonts']['large']
        )

        self.right_direction_btn = formControl.Button(
            (game['width']-310, game["height"]/2-150, 300, 300),
            (142, 96, 175),
            partial(self.nextPlayer, 'right'),
            click_sound=self.sounds.effects['click_sound'],
            font=self.vars['fonts']['large']
        )


        self.down_direction_btn = formControl.Button(
            (game['width']/2-150, game["height"]-310, 300, 300),
            (142, 96, 175),
            partial(self.nextPlayer, 'down'),
            click_sound=self.sounds.effects['click_sound'],
            font=self.vars['fonts']['large']
        )

    def nextPlayer(self, direction, id):
        self.player.set_direction(direction)
        self.persist['game_state']['reuse_scene'] = self.next_state
        self.persist['game_state']['skip_to_scene'] = 'ROLL_DOUBLE_DICE'

        self.done = True

    def startup(self, persistent):
        self.sounds.play('main_theme')
        self.next_state = 'ROLL_DICE.BUTTON'
        self.persist = persistent
        current_player_idx = self.persist['game_state']['current_player_index']
        self.player = self.persist['game_state']['players'][current_player_idx]
        self.persist['game_state']['reuse_scene'] = self.current_state
        self.i18n = self.persist['game_state']['i18n']

    def get_event(self, event):
        helpers.check_paused_event(self, event)
        self.up_direction_btn.check_event(event)
        self.left_direction_btn.check_event(event)
        self.down_direction_btn.check_event(event)
        self.right_direction_btn.check_event(event)

    def update(self, dt):
        self.turn_text.update_text(self.i18n.translate('choose_direction').format(self.player.name))
        self.left_direction_btn.update_text(self.i18n.translate('left'))
        self.right_direction_btn.update_text(self.i18n.translate('right'))
        self.down_direction_btn.update_text(self.i18n.translate('down'))
        self.up_direction_btn.update_text(self.i18n.translate('up'))

    def draw(self, surface):
        # background
        surface.blit(self.background.image, self.background.rect)

        self.left_direction_btn.update(surface)

        self.right_direction_btn.update(surface)

        self.down_direction_btn.update(surface)

        self.up_direction_btn.update(surface)


        self.turn_text.draw(surface)
