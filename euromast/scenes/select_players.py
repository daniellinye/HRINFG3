from components import stateManagment, formControl
from functools import partial
import pygame as pg

class Scene(stateManagment.BaseScene):
    def __init__(self, screen, helpers):
        super(Scene, self).__init__()
        self.vars = helpers['vars']
        self.assets =  helpers['assets']
        self.background = formControl.Image((0,0), self.assets['background-erasmus'])
        self.done = False
        self.next_state = 'INSERT_PLAYERS_NAMES'

        Button = formControl.Button

        game = self.vars['pygame']
        center_of_screen = game['center_of_screen']
        self.header_text = formControl.Text(
            (center_of_screen, 100),
            '',
            self.vars['fonts']['large'],
            pg.Color('white')
        )
        self.two_players_btn = Button(
            (center_of_screen - 100, 200, 200, 50),
            (255,0,0),
            partial(self.register_player, 2),
            font=self.vars['fonts']['medium'],
            hover_color = pg.Color("black")
        )
        self.three_players_btn = Button(
            (center_of_screen - 100, 300, 200, 50),
            (255,0,0),
            partial(self.register_player, 3),
            font=self.vars['fonts']['medium'],
            hover_color=pg.Color("black")
        )
        self.four_players_btn = Button(
            (center_of_screen - 100, 400, 200, 50),
            (255,0,0),
            partial(self.register_player, 4),
            font=self.vars['fonts']['medium'],
            hover_color=pg.Color("black")
        )

    def register_player(self, amount, id):
        self.persist['game_state']['player_count'] = amount
        self.done = True

    def startup(self, persistent):
        self.persist = persistent
        self.i18n = self.persist['game_state']['i18n']

    def update(self, dt):
        self.header_text.update_text(self.i18n.translate('select amount of players'))
        self.two_players_btn.update_text(self.i18n.translate('2 players'))
        self.three_players_btn.update_text(self.i18n.translate('3 players'))
        self.four_players_btn.update_text(self.i18n.translate('4 players'))
    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        self.two_players_btn.check_event(event)
        self.three_players_btn.check_event(event)
        self.four_players_btn.check_event(event)



    def draw(self, surface):
        surface.blit(self.background.image, self.background.rect)
        self.header_text.draw(surface)
        self.two_players_btn.update(surface)
        self.three_players_btn.update(surface)
        self.four_players_btn.update(surface)
