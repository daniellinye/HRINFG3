from components import stateManagment, formControl
from functools import partial
import pygame as pg

class Scene(stateManagment.BaseScene):
    """
    Parent class for individual game states to inherit from.
    """
    def __init__(self, screen, helpers):
        super(Scene, self).__init__()
        self.vars = helpers['vars']
        self.assets =  helpers['assets']
        self.next_state = 'MENU' #should be prev state
        self.game = game = self.vars['pygame']
        i18n = self.i18n
        center_of_screen = game['center_of_screen']
        self.header_text = formControl.Text(
            (center_of_screen, 80),
            '',
            self.vars['fonts']['large'],
            pg.Color('white')
        )

        self.lang_setting_text = formControl.Text(
            (center_of_screen / 2, 150),
            '',
            self.vars['fonts']['medium'],
            pg.Color('white')
        )

        self.dutch_lang_btn = formControl.Button(
            (center_of_screen/2 - 100, 180, 200, 50),
            pg.Color('red'),
            partial(self.change_lang, 'nl'),
            text="Nederlands",
            font=self.vars['fonts']['medium']
        )

        self.go_back_btn = formControl.Button(
            (center_of_screen/2-100, 400, 200, 50),
            pg.Color('green'),
            self.go_back,
            font=self.vars['fonts']['medium']
        )

        self.english_lang_btn = formControl.Button(
            (center_of_screen/2 - 100, 250, 200, 50),
            pg.Color('red'),
            partial(self.change_lang, 'en'),
            text="English",
            font=self.vars['fonts']['medium']
        )

    def change_lang(self, lang, id):
        self.persist['game_state']['i18n'] = self.i18n.load(lang)

    def go_back(self, id):
        self.done = True

    def startup(self, persistent):
        self.persist = persistent

    def update(self, dt):
        self.lang_setting_text.update_text(self.i18n.translate('language'))
        self.header_text.update_text(self.i18n.translate('settings'))
        self.go_back_btn.update_text(self.i18n.translate('go back'))
        self.english_lang_btn.color = pg.Color('red')
        self.dutch_lang_btn.color = pg.Color('red')
        if self.i18n.current_lang == 'en':
            self.english_lang_btn.update_color(pg.Color('green'))
        elif self.i18n.current_lang == 'nl':
            self.dutch_lang_btn.update_color(pg.Color('green'))

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        self.dutch_lang_btn.check_event(event)
        self.english_lang_btn.check_event(event)
        self.go_back_btn.check_event(event)



    def draw(self, surface):
        surface.fill((0,0,0))
        self.header_text.draw(surface)
        self.lang_setting_text.draw(surface)
        self.dutch_lang_btn.update(surface)
        self.english_lang_btn.update(surface)
        self.go_back_btn.update(surface)
