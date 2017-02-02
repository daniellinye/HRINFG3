from components import stateManagment, formControl, helpers
from functools import partial
from model.model import Model
import pygame as pg

SCENE_NAME = "INSTRUCTIONS"
class Scene(stateManagment.BaseScene):
    def __init__(self, screen, helpers):
        super(Scene, self).__init__(helpers)
        self.vars = helpers['vars']
        self.assets = helpers['assets']
        self.game = game = self.vars['pygame']
        self.list = []
        self.i = 1
        self.guide_part = 1

        center_of_screen = game['center_of_screen']

        self.header_text = formControl.Text(
            (center_of_screen, 80),
            '',
            self.vars['fonts']['large'],
            pg.Color('white')
        )

        self.rules = self.i18n.translate("guide" + str(self.guide_part)).split("\n")
        for text in self.rules:
            self.list.append(
                formControl.Text(
                    (center_of_screen, 90 + 17*self.i),
                    text,
                    self.vars['fonts']['small'],
                    pg.Color('white')
                )
            )
            self.i += 1

        self.go_back_btn = formControl.Button(
            (0, 650, 200, 50),
            pg.Color('green'),
            self.go_back,
            font=self.vars['fonts']['medium'],
            click_sound=self.sounds.effects['click_sound'],
            hover_color=pg.Color("black")
        )

        self.next_btn = formControl.Button(
            (game["width"]-200, 650, 200, 50),
            pg.Color('green'),
            self.next,
            font=self.vars['fonts']['medium'],
            click_sound=self.sounds.effects['click_sound'],
            hover_color=pg.Color("black")
        )

    def go_back(self, id):
        if self.guide_part > 1:
            self.guide_part -= 1
        else:
            if self.persist['game_state']['skip_to_scene'] == 'PAUSED':
                self.next_state = 'PAUSED'
            self.done = True

    def next(self, id):
        if self.guide_part < 2:
            self.guide_part += 1

    def startup(self, persistent):
        self.next_state = 'MENU'  # should be prev state
        self.persist = persistent
        self.i18n = self.persist['game_state']['i18n']

    def update(self, dt):
        self.header_text.update_text(self.i18n.translate('rules'))
        self.go_back_btn.update_text(self.i18n.translate('go back'))
        self.next_btn.update_text(self.i18n.translate('next'))

        guide = self.i18n.translate('guide' + str(self.guide_part)).split("\n")
        for item in self.list:
            item.update_text("")
        for (i, item) in enumerate(guide):
            self.list[i].update_text(item)

    def get_event(self, event):
        helpers.check_default_events(self, event)
        self.go_back_btn.check_event(event)
        self.next_btn.check_event(event)

    def draw(self, surface):
        surface.fill((0, 0, 0))
        self.header_text.draw(surface)
        self.go_back_btn.update(surface)
        if self.guide_part < 2:
            self.next_btn.update(surface)

        for n in self.list:
            n.draw(surface)
