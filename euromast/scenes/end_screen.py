from components import stateManagment, formControl, helpers
import pygame as pg

SCENE_NAME = "ENDSCREEN"
class Scene(stateManagment.BaseScene):
    def __init__(self, screen, helpers):
        super(Scene, self).__init__(helpers)
        self.current_state = "ENDSCREEN"
        self.vars = helpers['vars']
        self.assets = helpers['assets']
        self.game = game = self.vars['pygame']
        self.background = formControl.Image((0, 0), self.assets['background-highscore'])
        i18n = self.i18n
        center_of_screen = game['center_of_screen']

        self.header_text = formControl.Text(
            (center_of_screen, 80),
            '',
            self.vars['fonts']['large'],
            pg.Color('black')
        )