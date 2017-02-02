from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)
import time
import sys
import pygame as pg
from i18n import i18n
from scenes import menu, select_players, insert_player_name, roll_dice, \
    choose_category, choose_direction, roll_dice_button, turn_order, \
    roll_double_dice, choose_question, answer_question, settings, highscores, \
    display_tower, pause_menu, instructions, end_screen
from components import init, sound_manager, helpers as hp

from model import model

class Game(object):
    """
    A single instance of this class is responsible for
    managing which individual game state is active
    and keeping it updated. It also handles many of
    pygame's nuts and bolts (managing the event
    queue, framerate, updating the display, etc.).
    and its run method serves as the "game loop".
    """
    def __init__(self, screen, states):
        """
        Initialize the Game object.
        screen: the pygame display surface
        states: a dict mapping state-names to GameState objects
        start_state: name of the first active game state
        """
        pg.time.set_timer(pg.USEREVENT, 1000)
        self.done = False
        self.screen = screen
        self.clock = pg.time.Clock()
        self.fps = 60
        self.states = states
        self.state_name = states['__sartScene__']
        self.state = self.states[self.state_name]
        self.startup_persist = hp.get_state()
        self.startup_persist['game_state']['i18n'] = i18n.Localize()

        self.state.startup(self.startup_persist)

    def event_loop(self):
        """Events are passed for handling to the current state."""
        for event in pg.event.get():
            self.state.get_event(event)

    def flip_state(self):
        """Switch to the next game state."""
        current_state = self.state_name
        next_state = self.state.next_state
        self.state.done = False
        self.state_name = next_state

        persistent = self.state.persist if self.state.persist != 0 else self.startup_persist
        self.state = self.states[self.state_name]
        self.state.startup(persistent)

    def update(self, dt):
        """
        Check for state flip and update active state.

        dt: milliseconds since last frame
        """
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state()
        self.state.update(dt)

    def draw(self):
        """Pass display surface to active state for drawing."""
        self.state.draw(self.screen)

    def run(self):
        """
        Pretty much the entirety of the game's runtime will be
        spent inside this while loop.
        """
        while not self.done:
            dt = self.clock.tick(self.fps)
            self.event_loop()
            self.update(dt)
            self.draw()
            pg.display.update()

if __name__ == "__main__":
    pg.init()
    assets = init.LoadAssets().assets
    variables = init.LoadVariables().vars
    sounds = sound_manager.Manager(variables['sounds'])
    screen = pg.display.set_mode((variables['pygame']['width'], variables['pygame']['height']))
    helpers = {
        "assets": assets,
        "vars": variables,
        "sounds": sounds
    }
    #TODO add rules
    states = {
                "MENU": menu.Scene(screen, helpers),
                "INSTRUCTIONS": instructions.Scene(screen, helpers),
                "SETTINGS": settings.Scene(screen, helpers),
                "PAUSED": pause_menu.Scene(screen, helpers),
                "HIGHSCORES": highscores.Scene(screen,helpers),
                "SELECT_PLAYER": select_players.Scene(screen, helpers),
                "INSERT_PLAYERS_NAMES": insert_player_name.Scene(screen, helpers),
                "ROLL_DICE.BUTTON": roll_dice_button.Scene(screen, helpers),
                "ROLL_DICE.ROLLED": roll_dice.Scene(screen, helpers),
                "SHOW_TURN_ORDER": turn_order.Scene(screen, helpers),
                "CHOOSE_CATEGORY": choose_category.Scene(screen, helpers),
                "CHOOSE_DIRECTION": choose_direction.Scene(screen, helpers),
                "ROLL_DOUBLE_DICE": roll_double_dice.Scene(screen, helpers),
                "CHOOSE_QUESTION": choose_question.Scene(screen, helpers),
                "ANSWER_QUESTION": answer_question.Scene(screen, helpers),
                "SHOW_TOWER": display_tower.Scene(screen, helpers),
                "END_SCREEN": end_screen.Scene(screen,helpers),
                "__sartScene__": "MENU"
             }

    game = Game(screen, states)
    game.run()
    pg.quit()
    sys.exit()
