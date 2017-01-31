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
        self.current_player = None
        self.screen_color = pg.Color('white')
        Button = formControl.Button
        game = self.vars['pygame']
        center_of_screen = game['center_of_screen']
        vertical_center_of_screen = game['vertical_center_of_screen']

        self.throw_dice_btn = formControl.Button(
            (center_of_screen - 150, vertical_center_of_screen - 50, 300, 100),
            pg.Color('green'),
            self.go_next_state,
            font=self.vars['fonts']['medium']
        )

    def go_next_state(self, id):
        game_state = self.persist['game_state']
        if game_state['reuse_scene'] == 'ROLL_DICE.BUTTON' and game_state['skip_to_scene']:
            self.next_state = game_state['skip_to_scene']
        self.done = True

    def startup(self, persistent):
        self.persist = persistent
        game_state = self.persist['game_state']
        self.current_player = game_state['players'][game_state['current_player_index']]
        self.throw_dice_btn.update_text('{0} roll the dice'.format(self.current_player.get_name()))

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        self.throw_dice_btn.check_event(event)

    def update(self, dt):
        pass

    def draw(self, surface):
        surface.fill(self.screen_color)
        self.throw_dice_btn.update(surface);
