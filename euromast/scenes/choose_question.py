from components import stateManagment, formControl, player
from functools import partial
from model.model import Model
import pygame as pg
from math import floor

class Scene(stateManagment.BaseScene):
    """
    Parent class for individual game states to inherit from.
    """
    def __init__(self, screen , helpers):
        super(Scene, self).__init__()
        self.done = False
        self.vars = helpers['vars']
        self.assets = helpers['assets']
        self.game = game = self.vars['pygame']
        self.next_state = 'ANSWER_QUESTION'
        self.questions = []
        self.xPosFirstRow = 180
        self.opOrMul = {'multiple_choice': 'mul', 'open': 'op'}
        self.category_color = None
        self.category_type = None
        self.yPosFirstRow = 150
        self.incrRowPosBy = 200
        self.maxCardsPerRow = int(floor((game['width'] - self.xPosFirstRow) / self.xPosFirstRow))

    def startup(self, persistent):
        # stop sounds so we can use them again and play another sound
        self.vars["sounds"]["dice_roll"].stop()
        self.vars["sounds"]["main_theme"].stop()
        self.vars["sounds"]["choose_question"].play()

        self.persist = persistent
        game_state = self.persist['game_state']
        self.player = game_state['players'][game_state['current_player_index']]
        self.category = self.player.category
        self.question_type = self.player.question_type
        category_color = self.player.category['color']
        op_or_mul = self.opOrMul[self.player.question_type]

        questions = Model().get_questions(self.player.category['id'], self.player.question_type)

        rowX = self.xPosFirstRow
        rowY = self.yPosFirstRow
        cardsInRow = 0;
        for question in questions:
            if cardsInRow == self.maxCardsPerRow:
                cardsInRow = 0
                rowY += self.incrRowPosBy
                rowX = self.xPosFirstRow

            img = self.assets['{0}{1}'.format(category_color, op_or_mul)]
            self.questions.append(
                formControl.Image(
                    (rowX, rowY),
                    img,
                    partial(self.next_scene, question)
                ).scale()
            )

            rowX += self.incrRowPosBy
            cardsInRow = cardsInRow + 1

    def next_scene(self, question):
        self.player.current_question = question
        self.done = True

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        for question in self.questions:
            question.check_event(event)

    def update(self, dt):
        pass

    def draw(self, surface):
        surface.fill((255, 255, 255))
        for question in self.questions:
            question.draw(surface)
