from components import stateManagment, formControl, helpers
from i18n import i18n
from functools import partial
import pygame as pg

SCENE_NAME = "MENU"

class Scene(stateManagment.BaseScene):
    def __init__(self, surface, helpers):
        super(Scene, self).__init__(helpers)
        self.current_state = SCENE_NAME
        self.surface = surface
        self.vars = helpers['vars']
        self.assets = helpers['assets']
        self.sounds = helpers['sounds']
        self.next_state = ""
        Button = formControl.Button
        game = self.vars['pygame']
        width = game['width']
        height = game['height']
        button_width = 200
        button_font = self.vars['fonts']['large']
        button_hover_color = pg.Color('black')
        center_buttons = (width / 2) - (button_width / 2)
        self.background = formControl.Image((0,0), self.assets['background-erasmus'])
        self.sounds.play('menu_theme')

        self.header_text = formControl.Text(
            (game['center_of_screen'], 140),
            '',
            self.vars['fonts']['extraLarge'],
            pg.Color('black')
        )

        self.start_btn = Button(
            (center_buttons, height * .3, button_width, 50),
            (255,0,0),
            partial(self.go_to_scene, 'SELECT_PLAYER'),
            hover_color=button_hover_color,
            click_sound=self.sounds.effects['click_sound'],
            font=button_font
        )

        self.instruction_btn = Button(
            (center_buttons, height * .4, button_width,50),
            (255, 0, 0),
            partial(self.go_to_scene, 'INSTRUCTIONS'),
            hover_color=button_hover_color,
            click_sound=self.sounds.effects['click_sound'],
            font=button_font
        )

        self.highscore_btn = Button(
            (center_buttons, height * .5, button_width,50),
            (255, 0, 0),
            partial(self.go_to_scene, 'HIGHSCORES'),
            hover_color=button_hover_color,
            click_sound=self.sounds.effects['click_sound'],
            font=button_font
        )
        self.settings_btn = Button(
            (center_buttons, height * .6, button_width,50),
            (255, 0, 0),
            partial(self.go_to_scene, 'SETTINGS'),
            hover_color=button_hover_color,
            click_sound=self.sounds.effects['click_sound'],
            font=button_font
        )
        self.exit_btn = Button(
            (center_buttons, height * .7, button_width, 50),
            (255, 0, 0),
            self.exit,
            hover_color=button_hover_color,
            click_sound=self.sounds.effects['click_sound'],
            font=button_font
        )

    def exit(self, id):
        self.quit = True

    def startup(self, persistent):
        self.persist = persistent
        self.i18n = self.persist['game_state']['i18n']
        if self.persist['game_state']['reset_state']:
            self.persist = helpers.get_state()
            self.persist['game_state']['i18n'] = self.i18n

    def update(self, dt):
        self.header_text.update_text('Euromast')
        self.start_btn.update_text(self.i18n.translate('start'))
        self.instruction_btn.update_text(self.i18n.translate('instructions'))
        self.highscore_btn.update_text(self.i18n.translate('highscores'))
        self.settings_btn.update_text(self.i18n.translate('settings'))
        self.exit_btn.update_text(self.i18n.translate('exit'))

    def go_to_scene(self, sceneName, id):
        self.next_state = sceneName
        self.done = True

    def get_event(self, event):
        helpers.check_default_events(self, event)
        self.start_btn.check_event(event)
        self.highscore_btn.check_event(event)
        self.instruction_btn.check_event(event)
        self.settings_btn.check_event(event)
        self.exit_btn.check_event(event)

    def draw(self, surface):

        surface.fill(pg.Color("white"))
        surface.blit(self.background.image, self.background.rect)
        self.header_text.draw(surface)
        self.start_btn.update(surface)
        self.instruction_btn.update(surface)
        self.highscore_btn.update(surface)
        self.settings_btn.update(surface)
        self.exit_btn.update(surface)
