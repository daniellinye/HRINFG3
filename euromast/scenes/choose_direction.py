from components import stateManagment, formControl
from functools import partial
import pygame as pg

class Scene(stateManagment.BaseScene):
    def __init__(self, screen, helpers):
        super(Scene, self).__init__()
        self.vars = helpers['vars']
        self.next_state = 'ROLL_DICE.BUTTON'
        self.assets = helpers['assets']
        self.directions = []
        self.player = None
        self.game = game = self.vars['pygame']
        self.turn_text = formControl.Text(
            (game['width']*.5, game['height']*.5),
            '',
            self.vars['fonts']['large'],
            pg.Color('black')
        )

        self.left_direction_btn = formControl.Button(
            (20, 20, 300, 300),
            (0,0,255),
            partial(self.nextPlayer, 'left'),
            text="left",
            font=self.vars['fonts']['large']
        )

        self.up_direction_btn = formControl.Button(
            (20, game['height']-310, 300, 300),
            (255,0,0),
            partial(self.nextPlayer, 'up'),
            text="up",
            font=self.vars['fonts']['large']
        )

        self.right_direction_btn = formControl.Button(
            (game['width'] - 320, 20, 300, 300),
            (0,255,0),
            partial(self.nextPlayer, 'right'),
            text="right",
            font=self.vars['fonts']['large']
        )


        self.down_direction_btn = formControl.Button(
            (game['width'] - 320, game['height']-310, 300, 300),
            (255,255,0),
            partial(self.nextPlayer, 'down'),
            text='down',
            font=self.vars['fonts']['large']
        )

    def nextPlayer(self, direction):
        self.directions.append(direction)
        self.player.set_direction(direction)
        self.persist['game_state']['currentPlayerIndex'] += 1
        game_state = self.persist['game_state']
        len_players = len(game_state['players'])
        current_index = game_state['currentPlayerIndex']
        if current_index != len_players and current_index < len_players:
            self.player = self.persist['game_state']['players'][current_index]
            return

        self.persist['game_state']['currentPlayerIndex'] = 0
        self.persist['game_state']['reuse_scene'] = self.next_state
        self.persist['game_state']['skip_to_scene'] = 'ROLL_DOUBLE_DICE'

        self.done = True

    def startup(self, persistent):
        self.persist = persistent
        current_player_idx = self.persist['game_state']['currentPlayerIndex']
        self.player = self.persist['game_state']['players'][current_player_idx]

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        self.up_direction_btn.check_event(event)
        self.left_direction_btn.check_event(event)
        self.down_direction_btn.check_event(event)
        self.right_direction_btn.check_event(event)


    def update(self, dt):
        self.turn_text.updateText('{0} choose a direction'.format(self.player.name))

    def draw(self, surface):
        directions = self.directions
        # background
        surface.fill((255, 255, 255))
        if "left"  not in directions:
            self.left_direction_btn.update(surface)

        if "right"  not in directions:
            self.right_direction_btn.update(surface)

        if "down"  not in directions:
            self.down_direction_btn.update(surface)

        if "up" not in directions:
            self.up_direction_btn.update(surface)


        self.turn_text.draw(surface)
