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
        self.correct = None
        self.answer_btns = []
        self.question_type = None
        self.card_color = None
        self.game = game = self.vars['pygame']
        self.text_box = None
        self.next_button = formControl.Button(
            (game['center_of_screen'] - 100, (game['vertical_center_of_screen'] *2)-100, 200, 40),
            pg.Color('green'),
            self.nextPlayer,
            text='next',
            font=self.vars['fonts']['medium']
        )


    def nextPlayer(self, id):
        self.done = True

    def check_answer_open(self, textId, answer):
        self.check_answer(answer, textId)

    def check_answer(self, answer, id):
        if self.player.question_type !='open':
            correct_btn = None
            for answer in self.player.current_question['answers']:
                for answer_btn in self.answer_btns:
                    if answer_btn.button_id == answer['id'] and answer['is_correct']:
                        answer_btn.update_font_color(pg.Color('black'))
                        self.correct = True
                    elif answer_btn.button_id == answer['id']:
                        answer_btn.update_font_color(pg.Color('red'))
                        self.correct = False
            return
        ans = self.player.current_question['answers'][0]['name'].lower()
        print(answer)
        if ans == answer.lower():
            self.correct = True
        else:
            self.correct = False

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

        self.question_type = self.player.question_type
        if self.question_type == 'open':
            self.text_box = formControl.TextBox(
                (self.game['center_of_screen'] - 150, self.game['vertical_center_of_screen'], 300, 40),
                command=self.check_answer_open,
                font=self.vars['fonts']['medium'])

        if self.question_type != 'open':
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
                        outline_color= self.card_color
                    )
                )
                c += 1

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        if self.text_box:
            self.text_box.get_event(event)

        if self.correct == None:
            for answer_btn in self.answer_btns:
                answer_btn.check_event(event)
        self.next_button.check_event(event)

    def update(self, dt):
        if self.text_box:
            self.text_box.update()
        if self.question_type == 'open' and self.correct == False:
            self.text_box.outline_color = pg.Color('red')
        elif self.question_type == 'open' and self.correct:
            self.text_box.outline_color = pg.Color('green')

    def draw(self, surface):
        # background
        surface.fill(self.card_color)

        if self.text_box:
            self.text_box.draw(surface)
        if self.correct or self.correct == False:
            self.next_button.update(surface)
        rect = pg.draw.rect(surface, self.card_color, (self.game['center_of_screen'] - 300, 10, 600, self.game['height'] *.25))
        formControl.TextInRect(surface, self.player.current_question['name'], pg.Color('black'), rect, self.vars['fonts']['medium'])
        pg.draw.line(surface, pg.Color('black'), (0, self.game['height'] *.25), (self.game['width'], self.game['height'] *.25))

        for answer_btns in self.answer_btns:
            answer_btns.update(surface)
