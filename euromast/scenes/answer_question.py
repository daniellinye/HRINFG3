from components import stateManagment, formControl
from functools import partial
from model.model import Model
import time
import pygame as pg

class Scene(stateManagment.BaseScene):
    def __init__(self, screen, helpers):
        super(Scene, self).__init__()
        self.vars = helpers['vars']
        self.next_state = 'SHOW_TOWER'
        self.assets = helpers['assets']
        self.player = None
        self.game = game = self.vars['pygame']
        self.player = None
        self.answer_btns = []
        self.card_color = None

    def nextPlayer(self, category, button_id):
        pass
    def check_answer(self, answer, id):
        correct_btn = None
        for answer in self.player.current_question['answers']:
            for answer_btn in self.answer_btns:
                if answer_btn.button_id == answer['id'] and answer['is_correct']:
                    self.vars["sounds"]["question_right"].play()
                    correct_btn = answer_btn
                else:
                    self.vars["sounds"]["question_wrong"].play()
        #correct_btn.update_font_color(pg.Color('black'))
        #self.done = True


    def startup(self, persistent):
        # stop sounds so we can use them again and play another sound
        self.vars["sounds"]["question_wrong"].stop()
        self.vars["sounds"]["question_right"].stop()
        self.vars["sounds"]["choose_question"].stop()
        self.vars["sounds"]["question_theme"].play()

        self.persist = persistent
        game_state = self.persist['game_state']

        self.player = game_state['players'][game_state['current_player_index']]
        self.card_color = pg.Color(self.player.category['color'])
        start_pos_top = 200;
        abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        c = 0;
        for answer in self.player.current_question['answers']:
            start_pos_top += 100
            button_text = '{0}. {1}'.format(abc[c], answer['name'])
            self.answer_btns.append(
                formControl.Button(
                    (self.game['center_of_screen'] - 100, start_pos_top, 200, 100),
                    self.card_color,
                    partial(self.check_answer, answer),
                    text=button_text,
                    button_id=answer['id'],
                    font=self.vars['fonts']['medium'],
                    outline_color= self.card_color,
                    click_sound=None
                )
            )
            c += 1

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        for answer_btn in self.answer_btns:
            answer_btn.check_event(event)

    def update(self, dt):
        pass

    def draw(self, surface):
        # background
        surface.fill(self.card_color)


        rect = pg.draw.rect(surface, self.card_color, (self.game['center_of_screen'] - 300, 10, 600, self.game['height'] *.25))
        formControl.TextInRect(surface, self.player.current_question['name'], pg.Color('black'), rect, self.vars['fonts']['medium'])
        pg.draw.line(surface, pg.Color('black'), (0, self.game['height'] *.25), (self.game['width'], self.game['height'] *.25))

        for answer_btns in self.answer_btns:
            answer_btns.update(surface)
