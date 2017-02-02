import pygame as pg
import threading
from functools import wraps
from components import formControl
from i18n import i18n
import copy
def get_state():
    return copy.deepcopy({
        'game_state': {
            "i18n": None,
            "player_count": 0,
            "players": [],
            "start_from_index": 0,
            "current_player_index": 0,
            "reuse_scene": None,
            "skip_to_scene": None,
            "music": True,
            "effects": True,
            "reset_state": False
        }
    })

def set_startup(self, persistent):
    game_state = persistent['game_state']
    self.i18n = game_state['i18n']
    current_player_index = game_state['current_player_index']
    self.players = game_state['players']
    self.player = self.players[current_player_index] if len(self.players) > 0 else None

def check_default_events(self, event):
    if event.type == pg.QUIT:
        self.quit = True

def check_paused_event(self, event):
    check_default_events(self, event)
    if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE \
            and self.current_state != "CHOOSE_QUESTION" and self.current_state != "ANSWER_QUESTION":
        self.next_state = "PAUSED"
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
