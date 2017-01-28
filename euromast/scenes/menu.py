from components import stateManagment, formControl
from functools import partial
import pygame as pg

class MenuScene(stateManagment.BaseScene):
    def __init__(self, screen, helpers):
        super(MenuScene, self).__init__()
        # self.title = self.font.render("Splash Screen", True, pg.Color("dodgerblue"))
        # self.title_rect = self.title.get_rect(center=self.screen_rect.center)
        self.screen = screen
        self.vars = helpers['vars']
        self.assets =  helpers['assets']
        self.persist["screen_color"] = "black"
        self.next_state = "GAMEPLAY"
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
            partial(self.goToScene, 'EXIT'),
            text="EXIT",
            hover_color=buttonHoverColor,
            font=buttonFont)

    def goToScene(self, sceneName):
        self.next_state = sceneName
        self.done = True
    def goNext(self, screenName):
        self.persist['screen_color'] = 'gold';
        self.done = True
    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        elif event.type == pg.KEYUP:
            self.persist["screen_color"] = "gold"
            self.done = False
        elif event.type == pg.MOUSEBUTTONUP:
            self.persist["screen_color"] = "dodgerblue"
            self.done = False
        self.startButton.check_event(event)
        self.highscoresButton.check_event(event)
        self.instructionsButton.check_event(event)
        self.settingsButton.check_event(event)
        self.exitButton.check_event(event)

    def draw(self, surface):
        surface.fill(pg.Color("white"))

        surface.blit(self.background.image, self.background.rect)
        self.startButton.update(self.screen)
        self.instructionsButton.update(self.screen)
        self.highscoresButton.update(self.screen)
        self.settingsButton.update(self.screen)
        self.exitButton.update(self.screen)
        # surface.blit(self.title, self.title_rect)
