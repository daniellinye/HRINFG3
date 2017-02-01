from components import stateManagment, formControl
from functools import partial
from model.model import Model
from scenes import rules
import pygame as pg


class Scene(stateManagment.BaseScene):
    def __init__(self, screen, helpers):
        super(Scene, self).__init__()
        self.vars = helpers['vars']
        self.assets = helpers['assets']
        self.next_state = 'MENU'  # should be prev state
        self.game = game = self.vars['pygame']
        self.list = []
        self.i = 1

        center_of_screen = game['center_of_screen']

        self.header_text = formControl.Text(
            (center_of_screen, 80),
            '',
            self.vars['fonts']['large'],
            pg.Color('white')
        )

        self.rules = self.i18n.translate('guide').split("\n")
        for text in self.rules:
            self.list.append(
                formControl.Text(
                    (center_of_screen, 90 + 10*self.i),
                    text,
                    self.vars['fonts']['small'],
                    pg.Color('white')
                )
            )
            self.i += 1

        self.go_back_btn = formControl.Button(
            (center_of_screen / 2 - 100, 650, 200, 50),
            pg.Color('green'),
            self.go_back,
            font=self.vars['fonts']['medium'],
            hover_color=pg.Color("black")
        )

    def go_back(self, id):
            self.done = True

    def startup(self, persistent):
            self.persist = persistent
            self.i18n = self.persist['game_state']['i18n']

    def update(self, dt):
            self.header_text.update_text(self.i18n.translate('rules'))
            self.go_back_btn.update_text(self.i18n.translate('go back'))

            guide = self.i18n.translate('guide').split("\n")
            for item in self.list:
                item.update_text("")
            for (i, item) in enumerate(guide):
                self.list[i].update_text(item)

    def get_event(self, event):
            if event.type == pg.QUIT:
                self.quit = True
            self.go_back_btn.check_event(event)

    def draw(self, surface):
            surface.fill((0, 0, 0))
            self.header_text.draw(surface)
            self.go_back_btn.update(surface)

            for n in self.list:
                n.draw(surface)
