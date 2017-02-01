from components import stateManagment, formControl
from functools import partial
import pygame as pg

class Scene(stateManagment.BaseScene):
    """
    Parent class for individual game states to inherit from.
    """
    def __init__(self, screen, helpers):
        super(Scene, self).__init__(helpers)
        self.vars = helpers['vars']
        self.assets =  helpers['assets']
        self.next_state = 'MENU' #should be prev state
        self.game = game = self.vars['pygame']
        self.sounds = helpers['sounds']
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
            click_sound=self.sounds.effects['click_sound'],
            font=self.vars['fonts']['medium']
        )

        self.go_back_btn = formControl.Button(
            (center_of_screen/2-100, 400, 200, 50),
            pg.Color('green'),
            self.go_back,
            click_sound=self.sounds.effects['click_sound'],
            font=self.vars['fonts']['medium'],
            hover_color = pg.Color("black")
        )

        self.english_lang_btn = formControl.Button(
            (center_of_screen/2 - 100, 250, 200, 50),
            pg.Color('red'),
            partial(self.change_lang, 'en'),
            click_sound=self.sounds.effects['click_sound'],
            text="English",
            font=self.vars['fonts']['medium']
        )

        self.sound_setting_text = formControl.Text(
            (center_of_screen * 1.5, 150),
            '',
            self.vars['fonts']['medium'],
            pg.Color('white')
        )

        self.music_sound_btn = formControl.Button(
            (center_of_screen * 1.5 - 100, 180, 200, 50),
            pg.Color('green'),
            self.toggle_music,
            click_sound=self.sounds.effects['click_sound'],
            font=self.vars['fonts']['medium']
        )

        self.effects_sound_btn = formControl.Button(
            (center_of_screen * 1.5 - 100, 250, 200, 50),
            pg.Color('green'),
            self.toggle_effects,
            click_sound=self.sounds.effects['click_sound'],
            font=self.vars['fonts']['medium']
        )

    def change_lang(self, lang, id):
        self.persist['game_state']['i18n'] = self.i18n.load(lang)

    def toggle_music(self, id):
        if self.persist['game_state']['music'] == True:
            self.sounds.stop_music()
            self.persist['game_state']['music'] = False
        else:
            self.sounds.play_music()
            self.persist['game_state']['music'] = True

    def toggle_effects(self, id):
        if self.persist['game_state']['effects'] == True:
            self.persist['game_state']['effects'] = False
            self.sounds.stop_effects()
        else:
            self.sounds.play_effects()
            self.persist['game_state']['effects'] = True

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
        self.sound_setting_text.update_text(self.i18n.translate('sound'))
        self.music_sound_btn.update_text(self.i18n.translate('music'))
        self.effects_sound_btn.update_text(self.i18n.translate('effects'))
        if self.i18n.current_lang == 'en':
            self.english_lang_btn.update_color(pg.Color('green'))
        elif self.i18n.current_lang == 'nl':
            self.dutch_lang_btn.update_color(pg.Color('green'))
        if self.persist['game_state']['music'] == False:
            self.music_sound_btn.color = pg.Color('red')
        if self.persist['game_state']['music'] == True:
            self.music_sound_btn.color = pg.Color('green')
        if self.persist['game_state']['effects'] == False:
            self.effects_sound_btn.color = pg.Color('red')
        if self.persist['game_state']['effects'] == True:
            self.effects_sound_btn.color = pg.Color('green')

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        self.dutch_lang_btn.check_event(event)
        self.english_lang_btn.check_event(event)
        self.go_back_btn.check_event(event)
        self.effects_sound_btn.check_event(event)
        self.music_sound_btn.check_event(event)




    def draw(self, surface):
        surface.fill((0,0,0))
        self.header_text.draw(surface)
        self.lang_setting_text.draw(surface)
        self.dutch_lang_btn.update(surface)
        self.english_lang_btn.update(surface)
        self.go_back_btn.update(surface)
        self.sound_setting_text.draw(surface)
        self.music_sound_btn.update(surface)
        self.effects_sound_btn.update(surface)
