from components import stateManagment, formControl, helpers
from model.model import Model
import pygame as pg

SCENE_NAME = "HIGHSCORES"
class Scene(stateManagment.BaseScene):
    def __init__(self, screen, helpers):
        super(Scene, self).__init__(helpers)
        self.current_state = "HIGHSCORES"
        self.vars = helpers['vars']
        self.assets = helpers['assets']
        self.game = game = self.vars['pygame']
        self.list = []
        self.background = formControl.Image((0, 0), self.assets['background-highscore'])
        i18n = self.i18n
        center_of_screen = game['center_of_screen']

        self.header_text = formControl.Text(
            (center_of_screen, 80),
            '',
            self.vars['fonts']['large'],
            pg.Color('black')
        )

        self.players = Model().get_highscores()
        for i in range(1,len(self.players)+1):
            self.list.append(
                formControl.Text(
                (center_of_screen, 80 + 60*i),
                str(i) + '. ' + self.players[i-1]['name'] + '   ' + str(self.players[i-1]['score']),
                self.vars['fonts']['medium'],
                pg.Color('black')
                )
            )

        self.go_back_btn = formControl.Button(
            (center_of_screen / 2 - 100, 650, 200, 50),
            pg.Color('green'),
            self.go_back,
            font=self.vars['fonts']['medium'],
            click_sound=self.sounds.effects['click_sound'],
            hover_color=pg.Color("black")
        )

    def go_back(self, id):
        self.done = True

    def startup(self, persistent):
        self.next_state = 'MENU' 
        self.persist = persistent

    def update(self, dt):
        self.header_text.update_text('Highscores')
        self.go_back_btn.update_text(self.i18n.translate('go back'))

    def get_event(self, event):
        helpers.check_default_events(self, event)
        self.go_back_btn.check_event(event)

    def draw(self, surface):
        surface.blit(self.background.image, self.background.rect)
        self.header_text.draw(surface)
        self.go_back_btn.update(surface)

        for n in self.list:
            n.draw(surface)
