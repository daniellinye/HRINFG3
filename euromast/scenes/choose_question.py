from components import stateManagment, formControl, player, helpers
from functools import partial
from model.model import Model
import pygame as pg
from math import floor

SCENE_NAME = 'CHOOSE_QUESTION'
class Scene(stateManagment.BaseScene):
    """
    Parent class for individual game states to inherit from.
    """
    def __init__(self, screen , helpers):
        super(Scene, self).__init__(helpers)
        self.done = False
        self.current_state = SCENE_NAME
        self.vars = helpers['vars']
        self.assets = helpers['assets']
        self.game = game = self.vars['pygame']
        self.questions = []
        self.xPosFirstRow = 180
        self.opOrMul = {'multiple_choice': 'mul', 'open': 'op'}
        self.background = formControl.Image((0, 0), self.assets['background-dice'])
        self.category_color = None
        self.question_img =None
        self.category_type = None
        self.yPosFirstRow = 150
        self.incrRowPosBy = 200
        self.maxCardsPerRow = int(floor((game['width'] - self.xPosFirstRow) / self.xPosFirstRow))

    def startup(self, persistent):
        self.next_state = 'ANSWER_QUESTION'
        # stop sounds so we can use them again and play another sound
        self.sounds.stop(['dice_roll', 'main_theme'])
        self.sounds.play('choose_question')

        self.persist = persistent
        game_state = self.persist['game_state']
        self.player = game_state['players'][game_state['current_player_index']]
        self.category = self.player.category
        self.question_type = self.player.question_type
        category_color = self.player.category['color']
        op_or_mul = self.opOrMul[self.player.question_type]

        questions = Model().get_question(self.player.category['id'], self.player.question_type, self.player.answer_questions_id)
        img = self.assets['{0}{1}'.format(category_color, op_or_mul)]
        self.question_img = formControl.Image(
            (self.game['center_of_screen'], self.game['vertical_center_of_screen']),
            img,
            self.random_question
        ).scale(1, 1)

    def random_question(self):
        question = Model().get_question(self.player.category['id'], self.player.question_type, self.player.answer_questions_id)
        self.player.current_question = question[0]
        self.done = True

    def next_scene(self, question):
        self.player.current_question = question
        self.done = True

    def get_event(self, event):
        helpers.check_paused_event(self, event)
        self.question_img.check_event(event)

    def update(self, dt):
        pass

    def draw(self, surface):
        surface.fill((255, 255, 255))
        surface.blit(self.background.image, self.background.rect)
        self.question_img.draw(surface)
