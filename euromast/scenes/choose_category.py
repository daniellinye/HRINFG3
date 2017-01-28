from components import stateManagment, formControl
from functools import partial
import pygame as pg

class Scene(stateManagment.BaseScene):
    def __init__(self, screen, helpers):
        super(Scene, self).__init__()
        self.vars = helpers['vars']
        self.next_state = 'CHOOSE_DIRECTION'
        self.assets = helpers['assets']
        self.categories = []
        self.player = None
        self.game = game = self.vars['pygame']
        self.turn_text = formControl.Text(
            (game['width']*.5, game['height']*.5),
            '',
            self.vars['fonts']['large'],
            pg.Color('black')
        )

        self.sports_category_btn = formControl.Button(
            (20, 20, 300, 300),
            (0,0,255),
            partial(self.nextPlayer, 'sports'),
            text="Sports",
            font=self.vars['fonts']['large']
        )

        self.entertainment_category_btn = formControl.Button(
            (20, game['height']-310, 300, 300),
            (255,0,0),
            partial(self.nextPlayer, 'entertainment'),
            text="Entertainment",
            font=self.vars['fonts']['large']
        )

        self.geography_category_btn = formControl.Button(
            (game['width'] - 320, 20, 300, 300),
            (0,255,0),
            partial(self.nextPlayer, 'geography'),
            text="Geography",
            font=self.vars['fonts']['large']
        )


        self.history_category_btn = formControl.Button(
            (game['width'] - 320, game['height']-310, 300, 300),
            (255,255,0),
            partial(self.nextPlayer, 'history'),
            text='History',
            font=self.vars['fonts']['large']
        )

    def nextPlayer(self, category):
        self.categories.append(category)
        self.player.set_category(category)
        self.persist['game_state']['currentPlayerIndex'] += 1
        game_state = self.persist['game_state']
        len_players = len(game_state['players'])
        current_index = game_state['currentPlayerIndex']
        if current_index != len_players and current_index < len_players:
            self.player = self.persist['game_state']['players'][current_index]
            return
        self.persist['game_state']['currentPlayerIndex'] = 0
        self.done = True

    def startup(self, persistent):
        self.persist = persistent
        current_player_idx = self.persist['game_state']['currentPlayerIndex']
        self.player = self.persist['game_state']['players'][current_player_idx]

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        self.sports_category_btn.check_event(event)
        self.geography_category_btn.check_event(event)
        self.entertainment_category_btn.check_event(event)
        self.history_category_btn.check_event(event)

    def update(self, dt):
        self.turn_text.updateText('{0} choose a category'.format(self.player.name))

    def draw(self, surface):
        categories = self.categories
        # background
        surface.fill((255, 255, 255))
        if "sports"  not in categories:
            self.sports_category_btn.update(surface)

        if "geography"  not in categories:
            self.geography_category_btn.update(surface)

        if "entertainment"  not in categories:
            self.entertainment_category_btn.update(surface)

        if "history" not in categories:
            self.history_category_btn.update(surface)


        self.turn_text.draw(surface)
