from libdef import *


class Game:
    def choose_players(self, game):
        game.screen.fill((69, 69, 69))
        self.background = Background('./assets/background.png', [0, 0])
        game.screen.blit(self.background.image, self.background.rect)
        DrawText(game.screen, "Select amount of players", game.white, game.width - 512, 100)
        for i in range(2, 5):
            player_btn = DrawButton(game.screen, game.green, game.white, str(i) + " Players", 200, 50, game.width - 612, i * 100)
            if player_btn.collision():
                return i
