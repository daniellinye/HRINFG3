from libdef import *
import time


class Game:
    def __init__(self, game):
        self.game = game
        self.background = Background('./assets/background.png', [0, 0])

    def choose_players(self):
        self.game.screen.blit(self.background.image, self.background.rect)
        DrawText(self.game.screen, "Select amount of players", self.game.white, self.game.width - 512, 100)

        for i in range(2, 5):
            player_btn = DrawButton(self.game.screen, self.game.green, self.game.white, str(i) + " Players", 200, 50,
                                    512, i * 100)
            if player_btn.collision():
                return i

    def customize_players(self, current_player):
        self.game.screen.blit(self.background.image, self.background.rect)
        DrawText(self.game.screen, "Player {}, please enter a name:".format(current_player),
                 self.game.white, self.game.width - 512, 100)

        self.game.textinput.update(pygame.event.get())
        self.game.screen.blit(self.game.textinput.get_surface(), (512, 175))

        next = DrawButton(self.game.screen, self.game.green, self.game.white, "Next", 200, 50,
                          self.game.width-200, self.game.height-50)
        quit = DrawButton(self.game.screen, self.game.green, self.game.white, "Quit", 200, 50,
                          200, self.game.height-50)

        if next.collision():
            return Player(current_player, self.game.textinput.get_text() or "Player {}".format(current_player), (0, 0), 0)
        if quit.collision():
            return False




