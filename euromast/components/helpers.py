import pygame as pg
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
        self.done = True
