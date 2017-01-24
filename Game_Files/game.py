class Game:
    def choose_player(self):
        for i in range(2, 5):
            DrawButton(game.screen, game.green, game.white, i + " Players", 200, 50, game.width - (i * 100), 50)
