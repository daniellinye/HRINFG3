from components import stateManagment, formControl
import pygame as pg

class Scene(stateManagment.BaseScene):
    def __init__(self, screen, helpers):
        super(Scene, self).__init__()
        self.screen = screen
        self.done = False
        self.next_state = 'ROLL_DICE.ROLLED'
        self.vars = helpers['vars']
        self.assets =  helpers['assets']
        self.screen_color = pg.Color('white')
        Button = formControl.Button
        game = self.vars['pygame']
        self.centerOfScreen = (game['width'] / 2)
        self.vertical_center_of_screen = (game['height'] / 2)

        self.throwDiceBtn = formControl.Button((self.centerOfScreen - 150, self.vertical_center_of_screen - 50, 300, 100),
            pg.Color('green'),
            self.nextState,
            font=self.vars['fonts']['medium'])

    def nextState(self):
        game_state = self.persist['game_state']
        if game_state['reuse_scene'] == 'ROLL_DICE.BUTTON' and game_state['skip_to_scene']:
            self.next_state = game_state['skip_to_scene']
        self.done = True

    def startup(self, persistent):
        self.persist = persistent
        print(self.persist)
        game_state = self.persist['game_state']
        self.currentPlayer = game_state['players'][game_state['currentPlayerIndex']]
        self.throwDiceBtn.update_text('{0} roll the dice'.format(self.currentPlayer.get_name()))

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        self.throwDiceBtn.check_event(event)

    def update(self, dt):
        pass

    def draw(self, surface):
        surface.fill(self.screen_color)
        self.throwDiceBtn.update(surface);
