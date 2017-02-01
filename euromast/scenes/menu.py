from components import stateManagment, formControl
from i18n import i18n
from functools import partial
import pygame as pg

class Scene(stateManagment.BaseScene):
    def __init__(self, surface, helpers):
        super(Scene, self).__init__()
        self.surface = surface
        self.vars = helpers['vars']
        self.assets = helpers['assets']
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
        self.vars["sounds"]["menu_theme"].play()

        self.start_btn = Button(
            (center_buttons, height * .3, button_width, 50),
            (255,0,0),
            partial(self.go_to_scene, 'SELECT_PLAYER'),
            hover_color=button_hover_color,
            font=button_font
        )

        self.instruction_btn = Button(
            (center_buttons, height * .4, button_width,50),
            (255, 0, 0),
            partial(self.go_to_scene, 'INSTRUCTIONS'),
            hover_color=button_hover_color,
            font=button_font
        )

        self.highscore_btn = Button(
            (center_buttons, height * .5, button_width,50),
            (255, 0, 0),
            partial(self.go_to_scene, 'HIGHSCORES'),
            hover_color=button_hover_color,
            font=button_font
        )
        self.settings_btn = Button(
            (center_buttons, height * .6, button_width,50),
            (255, 0, 0),
            partial(self.go_to_scene, 'SETTINGS'),
            hover_color=button_hover_color,
            font=button_font
        )
        self.exit_btn = Button(
            (center_buttons, height * .7, button_width, 50),
            (255, 0, 0),
            self.exit,
            hover_color=button_hover_color,
            font=button_font
        )

    def exit(self, id):
        self.quit = True

    def startup(self, persistent):
        self.persist = persistent
        self.i18n = self.persist['game_state']['i18n']

    def update(self, dt):
        self.start_btn.update_text(self.i18n.translate('start'))
        self.instruction_btn.update_text(self.i18n.translate('instructions'))
        self.highscore_btn.update_text(self.i18n.translate('highscores'))
        self.settings_btn.update_text(self.i18n.translate('settings'))
        self.exit_btn.update_text(self.i18n.translate('exit'))

    def go_to_scene(self, sceneName, id):
        self.next_state = sceneName
        self.done = True

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        self.start_btn.check_event(event)
        self.highscore_btn.check_event(event)
        self.instruction_btn.check_event(event)
        self.settings_btn.check_event(event)
        self.exit_btn.check_event(event)

    def draw(self, surface):
        surface.fill(pg.Color("white"))
        surface.blit(self.background.image, self.background.rect)
        self.start_btn.update(surface)
        self.instruction_btn.update(surface)
        self.highscore_btn.update(surface)
        self.settings_btn.update(surface)
        self.exit_btn.update(surface)
