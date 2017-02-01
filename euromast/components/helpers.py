import pygame as pg
import threading
from functools import wraps
from components import formControl


class dotdict(dict):
     """dot.notation access to dictionary attributes"""
     __getattr__ = dict.get
     __setattr__ = dict.__setitem__
     __delattr__ = dict.__delitem__

def set_startup(self, persistent):
    game_state = persistent['game_state']
    self.i18n = game_state['i18n']
    current_player_index = game_state['current_player_index']
    self.players = game_state['players']
    self.player = self.players[current_player_index] if len(self.players) > 0 else None

def check_default_events(self, event):
    if event.type == pg.QUIT:
        self.quit = True
    elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
        self.next_state = "PAUSED"
        self.persist['']
        self.done = True


def delay(delay=0.):
    """
    Decorator delaying the execution of a function for a while.
    """
    def wrap(f):
        @wraps(f)
        def delayed(*args, **kwargs):
            timer = threading.Timer(delay, f, args=args, kwargs=kwargs)
            timer.start()
        return delayed
    return wrap
