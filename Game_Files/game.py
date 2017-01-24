from libdef import *

class Game:
    def choose_players(self, game):
        game.screen.fill((69, 69, 69))
        DrawText(game.screen, "Select amount of players", game.white, game.width - 612, 300)
        for i in range(2, 5):
            DrawButton(game.screen, game.green, game.white, str(i) + " Players", 200, 50, game.width - 612, i * 100)
