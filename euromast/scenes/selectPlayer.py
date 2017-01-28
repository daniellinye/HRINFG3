from components import stateManagment, formControl
from functools import partial
import pygame as pg

class SelectPlayerScene(stateManagment.BaseScene):
    def __init__(self, screen, helpers):
        super(SelectPlayerScene, self).__init__()
        self.screen = screen
        self.vars = helpers['vars']
        self.assets =  helpers['assets']
        self.background = formControl.Background(self.assets['background-erasmus'], [0,0])
        self.done = False
        self.next_state = 'INSERT_PLAYERS_NAMES'

        Button = formControl.Button

        game = self.vars['pygame']
        centerOfScreen = (game['width'] / 2)
        self.selectPlayerText = formControl.Text((centerOfScreen, 100),
            'Select amount of Players',
            self.vars['fonts']['large'],
            pg.Color('white'))
        self.towPlayersBtn = Button((centerOfScreen - 100, 200, 200, 50),
            (255,0,0),
            partial(self.registerPlayers, 2),
            text="2 Players",
            font=self.vars['fonts']['medium'])
        self.threePlayersBtn = Button((centerOfScreen - 100, 300, 200, 50),
            (255,0,0),
            partial(self.registerPlayers, 3),
            text="3 Players",
            font=self.vars['fonts']['medium'])
        self.fourPlayersBtn = Button((centerOfScreen - 100, 400, 200, 50),
            (255,0,0),
            partial(self.registerPlayers, 4),
            text="4 Players",
            font=self.vars['fonts']['medium'])

    def registerPlayers(self, amount):

        self.persist['game_state'] = {
            "playerCount": amount,
            "players": [],
            "startFromIndex": 0,
            "currentPlayerIndex": 0
        }
        self.done = True

    def startup(self, persistent):
        pass

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        self.towPlayersBtn.check_event(event)
        self.threePlayersBtn.check_event(event)
        self.fourPlayersBtn.check_event(event)

    def update(self, dt):
        pass

    def draw(self, surface):
        surface.blit(self.background.image, self.background.rect)
        self.selectPlayerText.draw(surface)
        self.towPlayersBtn.update(surface)
        self.threePlayersBtn.update(surface)
        self.fourPlayersBtn.update(surface)
