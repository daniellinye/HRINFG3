from components import stateManagment, formControl, helpers
from functools import partial
from model.model import Model
import pygame as pg

SCENE_NAME = 'CHOOSE_CATEGORY'
class Scene(stateManagment.BaseScene):
    def __init__(self, screen, helpers):
        super(Scene, self).__init__(helpers)
        self.vars = helpers['vars']
        self.current_state = SCENE_NAME
        self.assets = helpers['assets']
        self.categories = []
        self.background = formControl.Image((0, 0), self.assets['game-category'])

        self.selected_categories = []
        self.player = None
        self.game = game = self.vars['pygame']
        self.category_btns = []
        self.turn_text = formControl.Text(
            (game['width']*.5, game['height']*.5),
            '',
            self.vars['fonts']['large'],
            pg.Color('black')
        )


    def nextPlayer(self, category, button_id):
        self.selected_categories.append(button_id)
        self.player.set_category(category)
        self.persist['game_state']['current_player_index'] += 1
        game_state = self.persist['game_state']
        len_players = len(game_state['players'])
        current_index = game_state['current_player_index']
        if current_index != len_players and current_index < len_players:
            self.player = self.persist['game_state']['players'][current_index]
            return
        self.persist['game_state']['current_player_index'] = 0
        self.done = True

    def startup(self, persistent):
        self.next_state = 'CHOOSE_DIRECTION'
        self.persist = persistent
        self.i18n = self.persist['game_state']['i18n']
        self.persist['game_state']['reuse_scene'] = self.current_state
        game_state = self.persist['game_state']
        self.categories = Model().get_categories()

        x = .1
        for category in self.categories:
            self.category_btns.append(formControl.Button(
                (x * 300, 20, 200, 200),
                pg.Color(category['color']),
                partial(self.nextPlayer, category),
                click_sound=self.sounds.effects['click_sound'],
                text=category['name'],
                font=self.vars['fonts']['large']
            ))
            x += .8

        current_player_idx = self.persist['game_state']['current_player_index']
        self.player = self.persist['game_state']['players'][current_player_idx]

    def get_event(self, event):
        helpers.check_paused_event(self, event)
        for category_btn in self.category_btns:
            category_btn.check_event(event)


    def update(self, dt):
        self.turn_text.update_text(self.i18n.translate('choose a category').format(player=self.player.name))

    def draw(self, surface):
        # background
        surface.blit(self.background.image, self.background.rect)
        for category_btn in self.category_btns:
            if category_btn.button_id not in self.selected_categories:
                category_btn.update(surface)

        self.turn_text.draw(surface)
