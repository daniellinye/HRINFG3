from IV import IV
import pygame
import libdef

game = IV()

class DrawQuestion:
    def __init__(self, question, answers):
        self.drawing = True
        self.ins = game.height * .25
        self.handleAnswered = handleAnswered
        self.middleOfScreen = game.width * .5
        self.questionAsked = question;
        self.answers = answers;
        self.questionFont = pygame.font.SysFont('Arial', 35);
        self.answeredId = None;
        self.question = question.get('name')
        self.cardColor = question.get('color')


    def drawScreen(self):
        name = self.question

        cardColor = game.colors.get(self.cardColor)
        font = self.questionFont
        textColor = game.colors.get('black')
        game.screen.fill(cardColor)
        rect = pygame.draw.rect(game.screen, cardColor, (self.middleOfScreen - 300,1,600,self.ins))
        libdef.drawTextInRect(game.screen, name, game.black, rect, font)

        pygame.draw.line(game.screen, textColor, (0, self.ins), (game.width, self.ins))
        startPosTop = 200;
        abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        c = 0;
        for answer in self.answers:
            startPosTop = startPosTop + 100
            buttonColor = game.black
            buttonText = '{0}. {1}'.format(abc[c], answer.get('name'))
            if self.answeredId == answer.get('id') and answer.get('isCorrect'):
                buttonColor = game.green
            button = libdef.DrawButton(game.screen, cardColor, buttonColor, buttonText, 200, 100, self.middleOfScreen, startPosTop)
            if button.collision(cardColor):
                return self.checkCorrect(answer)
            c = c + 1

    def checkCorrect(self, answer):
        self.answeredId = answer.get('id')
        if answer.get('isCorrect'):
            return True
        else:
            return False

# force quit event
def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def Question():
    state = 1
    running = True
    toDraw = DrawQuestion({
        'id':1,
        'name': 'Wat was tijdens de Tweede Wereldoorlog de enige weg naar het centrum die de Duitsers probeerden te bereiken',
        'color': 'red'
        }, [
            {'id': 1, 'name': 'Wrong answer 2', 'isCorrect': False},
            {'id': 2, 'name': 'Long ass Wrong answer 20000000000000000000', 'isCorrect': False},
            {'id': 3,  'name': 'Correct answer', 'isCorrect': True}
        ])
    while process_events() and running:
        # FPS
        game.clock.tick(game.fps)
        # -----------------------------
        if state == 1:
            # keeps drawing screen
            toDraw.drawScreen()

        pygame.display.flip()

Question()
