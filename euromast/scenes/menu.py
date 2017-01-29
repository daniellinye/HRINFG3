from components import stateManagment, formControl
from functools import partial
import pygame as pg

class Scene(stateManagment.BaseScene):
    def __init__(self, surface, helpers):
        super(MenuScene, self).__init__()
        self.surface = surface
        self.vars = helpers['vars']
        self.assets =  helpers['assets']
        self.next_state = ""
        self.persist['game_state'] = {
            "playerCount": 0,
            "players": [],
            "startFromIndex": 0,
            "currentPlayerIndex": 0,
            "reuse_scene": None,
            "skip_to_scene": None
        }
        Button = formControl.Button
        gameWidth = self.vars['pygame']['width']
        gameHeight = self.vars['pygame']['height']
        buttonWidths = 200
        buttonFont = self.vars['fonts']['large']
        buttonHoverColor = pg.Color('black')
        centerOfScreen = (gameWidth / 2) - (buttonWidths / 2)
        self.background = formControl.Background(self.assets['background-erasmus'], [0,0])
        self.startButton = Button((centerOfScreen, gameHeight * .3, buttonWidths, 50),
            (255,0,0),
            partial(self.goToScene, 'SELECT_PLAYER'),
            text='Start',
            hover_color=buttonHoverColor,
            font=buttonFont)
        self.instructionsButton = Button((centerOfScreen, gameHeight * .4, buttonWidths,50),
            (255, 0, 0),
            partial(self.goToScene, 'INSTRUCTIONS'),
            text="Instructions",
            hover_color=buttonHoverColor,
            font=buttonFont)
        self.highscoresButton = Button((centerOfScreen, gameHeight * .5, buttonWidths,50),
            (255, 0, 0),
            partial(self.goToScene, 'HIGHSCORES'),
            text="Highscores",
            hover_color=buttonHoverColor,
            font=buttonFont)
        self.settingsButton = Button((centerOfScreen, gameHeight * .6, buttonWidths,50),
            (255, 0, 0),
            partial(self.goToScene, 'SETTINGS'),
            text="Settings",
            hover_color=buttonHoverColor,
            font=buttonFont)
        self.exitButton = Button((centerOfScreen, gameHeight * .7, buttonWidths,50),
            (255, 0, 0),
            self.exit,
            text="EXIT",
            hover_color=buttonHoverColor,
            font=buttonFont)

    def exit(self):
        self.quit = True

    def goToScene(self, sceneName):
        self.next_state = sceneName
        self.done = True

    def goNext(self, screenName):
        self.done = True

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        self.startButton.check_event(event)
        self.highscoresButton.check_event(event)
        self.instructionsButton.check_event(event)
        self.settingsButton.check_event(event)
        self.exitButton.check_event(event)

    def draw(self, surface):
        surface.fill(pg.Color("white"))
        surface.blit(self.background.image, self.background.rect)
        self.startButton.update(surface)
        self.instructionsButton.update(surface)
        self.highscoresButton.update(surface)
        self.settingsButton.update(surface)
        self.exitButton.update(surface)
