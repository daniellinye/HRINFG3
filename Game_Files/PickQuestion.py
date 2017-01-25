import pygame
from IV import IV
import libdef
import random
from math import floor
game = IV()

class DrawPickQuestion:
    def __init__(self, questions, onQuestionPicked = lambda x, y: None):
        self.drawing = True
        self.questions = questions
        self.onQuestionPicked = onQuestionPicked
        self.xPosFirstRow = 180
        self.opOrMul = {'multiple_choice': 'Mul', 'open': 'Op'}
        self.yPosFirstRow = 150
        self.incrRowPosBy = 200
        self.maxCardsPerRow = int(floor((game.width - self.xPosFirstRow) / self.xPosFirstRow))

    def drawScreen(self):
        rowX = self.xPosFirstRow
        rowY = self.yPosFirstRow
        cardsInRow = 0;
        for question in self.questions:

            if cardsInRow == self.maxCardsPerRow:
                cardsInRow = 0
                rowY += self.incrRowPosBy
                rowX = self.xPosFirstRow
            img = './assets/CBacks/{0}{1}.png'.format(question.get('color').title(), self.opOrMul.get(question.get('type')))
            card = libdef.DrawCard(game.screen,img, rowX, rowY, 12)
            if card.collision():
                self.onQuestionPicked(question.get('id'), question)
                print(question.get('id'))
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
    toDraw = DrawPickQuestion([{
        'id': 1,
        'name': 'Hoeveel tulpen zitten in een dozijn',
        'type': 'multiple_choice',
        'color': 'yellow'
    }, {
        'id': 2,
        'name': 'Wat is 1 + 1',
        'type': 'open',
        'color': 'red'
    }, {
        'id': 3,
        'name': 'Hoeveel tulpen zitten in een dozijn',
        'type': 'multiple_choice',
        'color': 'green'
    }, {
        'id': 4,
        'name': 'Wat is 1 + 1',
        'type': 'multiple_choice',
        'color': 'red'
    },
    {
        'id': 5,
        'name': 'Hoeveel tulpen zitten in een dozijn',
        'type': 'open',
        'color': 'green'
    }, {
        'id': 6,
        'name': 'Wat is 1 + 1',
        'type': 'open',
        'color': 'yellow'
    },
    {
        'id': 7,
        'name': 'Hoeveel tulpen zitten in een dozijn',
        'type': 'multiple_choice',
        'color': 'green'
    }, {
        'id': 8,
        'name': 'Wat is 1 + 1',
        'type': 'multiple_choice',
        'color': 'blue'
    },
    {
        'id': 7,
        'name': 'Hoeveel tulpen zitten in een dozijn',
        'type': 'open',
        'color': 'green'
    }, {
        'id': 8,
        'name': 'Wat is 1 + 1',
        'type': 'multiple_choice',
        'color': 'blue'
    }])
    while process_events() and running:
        # FPS
        game.clock.tick(game.fps)
        # -----------------------------
        if state == 1:
            # keeps drawing screen
            toDraw.drawScreen()

        pygame.display.flip()

PickQuestion()
