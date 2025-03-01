from components import stateManagment, formControl, helpers
from model import model
import pygame as pg

SCENE_NAME = "END_SCREEN"
class Scene(stateManagment.BaseScene):
    def __init__(self, screen, helpers):
        super(Scene, self).__init__(helpers)
        self.current_state = "END_SCREEN"
        self.vars = helpers['vars']
        self.assets = helpers['assets']
        self.game = game = self.vars['pygame']
        self.background = formControl.Image((0, 0), self.assets['background-end'])
        i18n = self.i18n
        center_of_screen = game['center_of_screen']

        self.header_text = formControl.Text(
            (center_of_screen, 625),
            '',
            self.vars['fonts']['large'],
            pg.Color('black')
        )

        self.continue_btn = formControl.Button(
            (center_of_screen / 2 - 100, 650, 200, 50),
            pg.Color('green'),
            self.go_back,
            font=self.vars['fonts']['medium'],
            click_sound=self.sounds.effects['click_sound'],
            hover_color=pg.Color("black")
        )

    def go_back(self, id):
        self.quit = True
        self.done = True

    def startup(self, persistent):
        self.sounds.stop("question_right")
        self.sounds.play("end_game")
        self.next_state = 'MENU'
        self.persist = persistent
        game_state = self.persist['game_state']
        self.header_text.update_text('{}, You Win!'.format(game_state['winner'].name))
        for player in game_state['players']:
            model.Model().add_highscore(player.name, player.score)
    def update(self, dt):

        self.continue_btn.update_text(self.i18n.translate('exit'))

    def get_event(self, event):
        helpers.check_default_events(self, event)
        self.continue_btn.check_event(event)

    def draw(self, surface):
        surface.blit(self.background.image, self.background.rect)
        self.header_text.draw(surface)
        self.continue_btn.update(surface)
