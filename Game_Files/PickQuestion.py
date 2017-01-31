import pygame
from IV import IV
import libdef
import random
import time
from math import floor
game = IV()

class DrawPickQuestion:
    def __init__(self, category, questions):
        self.drawing = True
        self.questions = questions
        self.colorOfCat = {
            'sports':{ 'name': 'Blue', 'rgb': game.colors.get('blue')},
            'entertainment': { 'name': 'Red', 'rgb': game.colors.get('red')},
            'history': { 'name': 'Yellow', 'rgb':game.colors.get('yellow')},
            'geography': { 'name':'Green', 'rgb':game.colors.get('green')}
        }
        self.color = self.colorOfCat.get(category);
        self.xPosFirstRow = 180
        self.opOrMul = {'multiple_choice': 'Mul', 'open': 'Op'}
        self.yPosFirstRow = 150
        self.incrRowPosBy = 200
        self.maxCardsPerRow = int(floor((game.width - self.xPosFirstRow) / self.xPosFirstRow))

    def drawScreen(self):
        game.screen.fill((255, 255, 255))
        game.sounds["choose_question"].play()
        rowX = self.xPosFirstRow
        rowY = self.yPosFirstRow
        cardsInRow = 0;
        for question in self.questions:

            if cardsInRow == self.maxCardsPerRow:
                cardsInRow = 0
                rowY += self.incrRowPosBy
                rowX = self.xPosFirstRow
            img = './assets/CBacks/{0}{1}.png'.format(self.color.get('name'), self.opOrMul.get(question.get('type')))
            card = libdef.DrawCard(game.screen,img, rowX, rowY, 12)
            if card.collision():
                game.sounds["choose_question"].stop()
                return {'questionId': question.get('id'), 'question': question}

            rowX += self.incrRowPosBy
            cardsInRow = cardsInRow + 1
# force quit event
def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def PickQuestion():
    state = 1
    running = True
    toDraw = DrawPickQuestion('entertainment', game.dummyQuestions)
    while process_events() and running:
        # FPS
        game.clock.tick(game.fps)
        # -----------------------------
        if state == 1:
            # keeps drawing screen
            toDraw.drawScreen()

        pygame.display.flip()

# PickQuestion()
