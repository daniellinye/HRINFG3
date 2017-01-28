import sys
import pygame as pg
from scenes import menu, selectPlayer, insertPlayerNames, roll_dice_order
from components import init

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
        self.done = False
        self.screen = screen
        self.clock = pg.time.Clock()
        self.fps = 60
        self.states = states
        self.state_name = states['__sartScene__']
        self.state = self.states[self.state_name]

    def event_loop(self):
        """Events are passed for handling to the current state."""
        for event in pg.event.get():
            self.state.get_event(event)

    def flip_state(self):
        """Switch to the next game state."""
        if(self.state.next_state == 'EXIT'):
            self.done = True
            return

        current_state = self.state_name
        next_state = self.state.next_state
        self.state.done = False
        self.state_name = next_state
        persistent = self.state.persist
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

    screen = pg.display.set_mode((variables['pygame']['width'], variables['pygame']['height']))

    helpers = {
        "assets": assets,
        "vars": variables
    }
    states = {
                "SPLASH": menu.MenuScene(screen, helpers),
                "SELECT_PLAYER": selectPlayer.SelectPlayerScene(screen, helpers),
                "INSERT_PLAYERS_NAMES": insertPlayerNames.InsertNamesScene(screen, helpers),
                "ROLL_DICE_TURNS.ROLL": roll_dice_order.Start(screen, helpers),
                "ROLL_DICE_TURNS.ROLLED": roll_dice_order.Roll(screen, helpers),
                "EXIT": None,
                "__sartScene__": "SPLASH"
             }

    game = Game(screen, states)
    game.run()
    pg.quit()
    sys.exit()
