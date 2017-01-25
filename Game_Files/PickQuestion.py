import pygame
from IV import IV
import libdef
from math import floor
game = IV()

class DrawPickQuestion:
    def __init__(self, questions):
        self.drawing = True
        self.questions = questions
        self.xPosFirstRow = 180
        self.yPosFirstRow = 150
        self.incrRowPosBy = 200
        self.maxCardsPerRow = int(floor((game.width - self.xPosFirstRow) / self.xPosFirstRow))
        print(self.maxCardsPerRow)
    def drawScreen(self):
        rowX = self.xPosFirstRow
        rowY = self.yPosFirstRow
        cardsInRow = 0;
        for question in self.questions:

            if cardsInRow == self.maxCardsPerRow:
                cardsInRow = 0
                rowY += self.incrRowPosBy
                rowX = self.xPosFirstRow
            card = libdef.DrawCard(game.screen, './assets/CBacks/BlueMul.png', rowX, rowY, 12)
            if card.collision():
                print(card.cardId)
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
        'color': game.green
    }, {
        'id': 2,
        'name': 'Wat is 1 + 1',
        'color': game.red
    }, {
        'id': 3,
        'name': 'Hoeveel tulpen zitten in een dozijn',
        'color': game.green
    }, {
        'id': 4,
        'name': 'Wat is 1 + 1',
        'color': game.red
    },
    {
        'id': 5,
        'name': 'Hoeveel tulpen zitten in een dozijn',
        'color': game.green
    }, {
        'id': 6,
        'name': 'Wat is 1 + 1',
        'color': game.red
    },
    {
        'id': 7,
        'name': 'Hoeveel tulpen zitten in een dozijn',
        'color': game.green
    }, {
        'id': 8,
        'name': 'Wat is 1 + 1',
        'color': game.red
    },
    {
        'id': 7,
        'name': 'Hoeveel tulpen zitten in een dozijn',
        'color': game.green
    }, {
        'id': 8,
        'name': 'Wat is 1 + 1',
        'color': game.red
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
