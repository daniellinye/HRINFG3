from components import stateManagment, formControl, helpers
from functools import partial
from model.model import Model
import time
import pygame as pg

SCENE_NAME = 'ANSWER_QUESTION'
class Scene(stateManagment.BaseScene):
    def __init__(self, screen, helpers):
        super(Scene, self).__init__(helpers)
        self.vars = helpers['vars']
        self.current_state = SCENE_NAME
        self.assets = helpers['assets']
        self.game = game = self.vars['pygame']
        self.player = None
        self.correct = None
        self.correct_answer_id = None
        self.answer_btns = []
        self.question_type = None
        self.card_color = None
        self.game = game = self.vars['pygame']
        self.text_box = None
        self.counter_font = self.vars['fonts']['large']
        self.timer = 10
        self.next_button = formControl.Button(
            (game['center_of_screen'] - 100, (game['vertical_center_of_screen'] *2)-100, 200, 40),
            pg.Color('green'),
            self.nextPlayer,
            text='next',
            click_sound=self.sounds.effects['click_sound'],
            font=self.vars['fonts']['medium']
        )


    def nextPlayer(self, id):
        # reset values
        self.sounds.stop('question_theme')
        self.correct = None
        self.answer_btns = []
        self.card_color = None
        self.player = None
        self.timer = 10
        self.text_box = None
        self.question_type = None
        self.done = True

    def check_answer_open(self, textId, answer):
        self.check_answer(answer, textId)

    def show_correct(self):
        for answer in self.player.current_question['answers']:
            for answer_btn in self.answer_btns:
                if answer_btn.button_id == answer['id'] and answer['is_correct']:
                    answer_btn.update_font_color(pg.Color('black'))
                elif answer_btn.button_id == answer['id'] and not answer['is_correct']:
                    answer_btn.update_font_color(pg.Color('red'))

    def too_late(self):
        self.sounds.stop("question_theme")
        self.correct = False
        if self.question_type != 'open':
            self.show_correct()
        self.sounds.play("too_slow")

    def check_answer(self, answer, bid):
        self.sounds.stop("question_theme")
        if self.player.question_type != 'open':
            correct_btn = None
            self.correct = False
            if self.correct_answer_id == bid:
                self.correct = True
            self.show_correct()

        elif self.player.question_type =='open':
            ans = self.player.current_question['answers'][0]['name'].lower()
            self.correct = False
            if ans == answer.lower():
                self.correct = True

        if self.correct:
            if self.player.direction == 'up':
                self.player.tower['current_steps'] += self.player.steps
                self.player.move_player_vertical()
            if self.player.direction == 'down':
                self.player.tower['current_steps'] -= self.player.steps
                self.player.move_player_vertical()
            if self.player.direction == 'left' or self.player.direction == 'right':
                self.player.move_player_horizontal()
            self.player.steps = 0
            self.player.score += 1
            self.sounds.play("question_right")
        else:
            self.player.steps = 0
            self.sounds.play("question_wrong")


    def startup(self, persistent):
        self.next_state = 'SHOW_TOWER'
        # stop sounds so we can use them again and play another sound
        self.text_box = None
        self.sounds.stop("choose_question")
        self.sounds.play("question_theme")

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
            start_pos_top = 100;
            abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            c = 0;
            for answer in self.player.current_question['answers']:
                start_pos_top += 100
                button_text = '{0}. {1}'.format(abc[c], answer['name'])
                if answer['is_correct']:
                    self.correct_answer_id = answer['id']
                self.answer_btns.append(
                    formControl.Button(
                        (self.game['center_of_screen'] - 100, start_pos_top, 200, 100),
                        self.card_color,
                        partial(self.check_answer, answer),
                        text=button_text,
                        font_color=(0, 0, 0),
                        button_id=answer['id'],
                        click_sound=self.sounds.effects['click_sound'],
                        font=self.vars['fonts']['large'],
                        outline_color= self.card_color
                    )
                )
                c += 1

    def get_event(self, event):
        helpers.check_paused_event(self, event)

        if event.type == pg.USEREVENT:
            if self.timer != 0 and self.correct == None:
                self.timer -= 1
            elif self.timer == 0 and self.correct == None:
                self.too_late()
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
        surface.blit(self.counter_font.render(str(self.timer), True, (0, 0, 0)), (32, 48))
        if self.text_box and self.question_type == 'open':
            self.text_box.draw(surface)
        if self.correct or self.correct == False:
            self.next_button.update(surface)
        rect = pg.draw.rect(surface, self.card_color, (self.game['center_of_screen'] - 300, 30, 600, self.game['height'] *.25))
        formControl.TextInRect(surface, self.player.current_question['name'], pg.Color('black'), rect, self.vars['fonts']['large'], 1)
        pg.draw.line(surface, pg.Color('black'), (0, self.game['height'] *.15), (self.game['width'], self.game['height'] *.15))

        for answer_btns in self.answer_btns:
            answer_btns.update(surface)
