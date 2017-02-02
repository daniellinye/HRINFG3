import pygame as pg
from i18n import i18n

class BaseScene(object):
    """
    Parent class for individual game states to inherit from.
    """
    def __init__(self, helpers=None):
        self.done = False
        self.quit = False
        self.sounds = helpers['sounds'] if helpers else None
        self.assets = helpers['assets'] if helpers else None
        self.vars = helpers['vars'] if helpers else None
        self.game = helpers['vars']['pygame'] if helpers else None
        self.i18n = i18n.Localize()
        self.next_state = None
        self.wait = None
        self.screen_rect = pg.display.get_surface().get_rect()
        self.persist = {}
        self.player = None
        self.players = None
        self.font = pg.font.SysFont("Arial", 24)


    def startup(self, persistent):
        """
        Called when a state resumes being active.
        Allows information to be passed between states.

        persistent: a dict passed from state to state
        """
        self.persist = persistent

    def get_event(self, event):
        """
        Handle a single event passed by the Game object.
        """
        pass


    def update(self, dt):
        """
        Update the state. Called by the Game object once
        per frame.

        dt: time since last frame
        """
        pass

    def draw(self, surface):
        """
        Draw everything to the screen.
        """
        pass
