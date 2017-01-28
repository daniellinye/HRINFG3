from components import stateManagment, formControl, player
from functools import partial
import pygame as pg

class InsertNamesScene(stateManagment.BaseScene):
    def __init__(self, screen, helpers):
        super(InsertNamesScene, self).__init__()
        self.screen = screen
        self.done = False
        self.next_state = 'ROLL_DICE_TURNS.ROLL'
        self.vars = helpers['vars']
        self.assets =  helpers['assets']
        self.screen_color = pg.Color('white')
        self.playerCount = 1
        Button = formControl.Button
        game = self.vars['pygame']
        centerOfScreen = (game['width'] / 2)

        self.headerText = formControl.Text((centerOfScreen - 5, 100),
            'Player {0}, please enter your name'.format(self.playerCount),
            self.vars['fonts']['large'],
            pg.Color('black'))
        self.nextButton = formControl.Button((centerOfScreen - 100, game['height'] - 100, 200, 50),
            pg.Color('green'),
            self.setPlayerName,
            font=self.vars['fonts']['medium'],
            text="Next")
        self.input = formControl.TextBox((centerOfScreen - 150,200,300,40),command=self.setPlayerName,
                              clear_on_enter=True, inactive_on_enter=False)

    def setPlayerName(self, id, pname):
        self.playerCount = self.playerCount + 1
        gameState = self.persist['game_state']
        gameState['players'].append(player.createPlayer(pname))
        if gameState['playerCount'] == len(gameState['players']):
            self.done = True
            return

        self.headerText.updateText('Player {0}, please enter your name'.format(self.playerCount))
        # self.done = True

    def startup(self, persistent):
        self.persist = persistent

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        self.input.get_event(event)
        self.nextButton.check_event(event)
    def update(self, dt):
        self.input.update()

    def draw(self, surface):
        surface.fill(self.screen_color)
        self.input.draw(surface)
        self.headerText.draw(surface)
        self.nextButton.update(surface);
        # surface.blit(self.background.image, self.background.rect)
        # self.backButton.update(surface)
