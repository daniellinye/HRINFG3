from components import stateManagment, formControl, helpers
from functools import partial
import pygame as pg

SCENE_NAME = "PAUSED"
class Scene(stateManagment.BaseScene):
    def __init__(self, surface, helpers):
        super(Scene, self).__init__(helpers)
        self.vars = helpers['vars']
        self.assets = helpers['assets']
        self.current_state = SCENE_NAME
        self.game = game = helpers['vars']['pygame']
        self.buttons = ['resume', 'instructions', 'settings', 'go to menu'];
        self.btns = {}
        self.background = formControl.Image((0,0), self.assets['background-erasmus'])
        button_width = 200
        button_font = self.vars['fonts']['large']
        button_hover_color = pg.Color('black')
        center_buttons = self.vars['pygame']['center_of_screen'] - (button_width / 2)
        height = self.vars['pygame']['height']
        y = .3
        for butname in self.buttons:
            self.btns[butname] = formControl.Button(
                (center_buttons, height * y, button_width, 50),
                (255,0,0),
                partial(self.go_to_scene, butname),
                hover_color=button_hover_color,
                text=self.i18n.translate(butname),
                click_sound=self.sounds.effects['click_sound'],
                font=button_font
            )
            y += .1


    def go_to_scene(self, scene, id):
        if scene == 'go to menu':
            self.next_state = 'MENU'
            self.persist['game_state']['reset_state'] = True 
            self.done= True


    def update(self, dt):
        pass

    def get_event(self, event):
        helpers.check_default_events(self, event)
        for key, button in self.btns.items():
            button.check_event(event)

    def startup(self, persistent):
        self.next_state = 'MENU'
        self.persist = persistent
        helpers.set_startup(self, self.persist)

    def draw(self, surface):
        surface.fill(pg.Color('white'))
        surface.blit(self.background.image, self.background.rect)
        for key, button in self.btns.items():
            button.update(surface)
