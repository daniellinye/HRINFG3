from IV import IV
import pygame
import libdef
from textwrap import fill
game = IV()

class DrawQuestion:
    def __init__(self):
        self.drawing = True
        self.ins = game.height * 0.25

    def draw(self, question, anwers):
        name = fill(question.get('name'), 5)
        game.screen.fill(game.colors.get(question.get('color')))
        libdef.DrawText(game.screen, name, game.white, game.width * .5, game.height * .08)
        lineColor = game.white if question.get('color') == 'black' else game.black
        pygame.draw.line(game.screen, lineColor, (0, self.ins), (game.width, self.ins))
        # libdef.DrawImage(game.screen, img, (game.width * 0.5), (game.height * 0.5))


# force quit event
def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def Question():
    state = 1
    running = True
    toDraw = DrawQuestion()
    while process_events() and running:
        # FPS
        game.clock.tick(game.fps)
        # -----------------------------
        if state == 1:
            # keeps drawing screen
            toDraw.draw({'name': 'Wat was tijdens de Tweede Wereldoorlog de enige weg naar het centrum die de Duitsers probeerden te bereiken', 'color': 'black'}, ['anwer1', 'answer2'])

        pygame.display.flip()

Question()
