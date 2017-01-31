from components import stateManagment, formControl, player
from functools import partial
import pygame as pg

class Scene(stateManagment.BaseScene):
    def __init__(self, screen, helpers):
        super(Scene, self).__init__()
        self.screen = screen
        self.done = False
        self.next_state = 'ROLL_DICE.BUTTON'
        self.vars = helpers['vars']
        self.assets =  helpers['assets']
        self.screen_color = pg.Color('white')
        self.player_count = 1
        Button = formControl.Button
        game = self.vars['pygame']
        center_of_screen = game['center_of_screen']

        self.header_text = formControl.Text(
            (center_of_screen - 5, 100),
            'Player {0}, please enter your name'.format(self.player_count),
            self.vars['fonts']['large'],
            pg.Color('black')
        )
        self.next_button = formControl.Button(
            (center_of_screen - 100, game['height'] - 100, 200, 50),
            pg.Color('green'),
            self.next_player,
            font=self.vars['fonts']['medium'],
            hover_color=pg.Color("black"),
            text="Next"
        )
        self.input = formControl.TextBox(
            (center_of_screen - 150,200,300,40),
            command=self.setPlayerName,
            clear_on_enter=True,
            inactive_on_enter=False
        )
    def next_player(self, id):
        self.input.execute()

    def setPlayerName(self, id, pname):
        if not pname:
            pname = "Player {0}".format(self.player_count)

        self.player_count += 1
        game_state = self.persist['game_state']
        game_state['players'].append(player.createPlayer(pname))

        if game_state['player_count'] == len(game_state['players']):
            self.vars["sounds"]["menu_theme"].stop()
            self.done = True
            return

        self.header_text.update_text('Player {0}, please enter your name'.format(self.player_count))
        # self.done = True

    def startup(self, persistent):
        self.persist = persistent

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        self.input.get_event(event)
        self.next_button.check_event(event)
    def update(self, dt):
        self.input.update()

    def draw(self, surface):
        surface.fill(self.screen_color)
        self.input.draw(surface)
        self.header_text.draw(surface)
        self.next_button.update(surface);
