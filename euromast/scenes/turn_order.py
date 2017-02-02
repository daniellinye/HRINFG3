from components import stateManagment, formControl, helpers
import pygame as pg

SCENE_NAME = "SHOW_TURN_ORDER"
class Scene(stateManagment.BaseScene):
    def __init__(self, scene, helpers):
        super(Scene, self).__init__(helpers)
        self.vars = helpers['vars']
        self.assets = helpers['assets']
        self.current_state = SCENE_NAME
        self.game = game = self.vars['pygame']
        self.background = formControl.Image((0, 0), self.assets['background-dice'])
        self.player_order = []
        self.playing_order_text = formControl.Text((game['center_of_screen'] , 100),
            '',
            self.vars['fonts']['medium'],
            pg.Color('black')
        )

        self.pick_category_btn = formControl.Button((game['center_of_screen'] - 100, game['height'] - 100, 200, 50),
            pg.Color('green'),
            self.next_scene,
            text='Continue',
            font=self.vars['fonts']['medium'],
            click_sound=self.sounds.effects['click_sound'],
            hover_color=pg.Color("black")
        )

    def next_scene(self, id):
        self.done = True

    def get_event(self, event):
        helpers.check_paused_event(self, event)
        self.pick_category_btn.check_event(event)

    def startup(self, persistent):
        self.next_state = 'CHOOSE_CATEGORY'
        self.persist = persistent
        self.i18n = self.persist['game_state']['i18n']
        players = self.persist['game_state']['players']
        self.persist['game_state']['reuse_scene'] = self.current_state
        game = self.vars['pygame']
        sort = sorted(players, key = lambda player: player.roll, reverse = True)
        x = 0.2
        self.persist['game_state']['players'] = sort
        for i in range(len(sort)):
            x += 0.1
            self.player_order.append(formControl.Text((game['width']*0.5, game['height']*x),
                "{}".format(sort[i].name),
                self.vars['fonts']['medium'],
                pg.Color('black')))

    def update(self, dt):
        pass

    def draw(self, surface):
        surface.blit(self.background.image, self.background.rect)
        self.playing_order_text.draw(surface)
        self.pick_category_btn.update(surface)
        self.playing_order_text.update_text(self.i18n.translate('the playing order will be'))
        self.pick_category_btn.update_text(self.i18n.translate('continue'))
        for order_text in self.player_order:
            order_text.draw(surface)
