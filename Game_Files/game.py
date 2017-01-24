from libdef import *


class Game:
    def __init__(self, game):
        self.game = game
        self.background = Background('./assets/background.png', [0, 0])

    def choose_players(self):
        self.game.screen.blit(self.background.image, self.background.rect)
        DrawText(self.game.screen, "Select amount of players", self.game.white, self.game.width - 512, 100)

        for i in range(2, 5):
            player_btn = DrawButton(self.game.screen, self.game.green, self.game.white, str(i) + " Players", 200, 50,
                                    self.game.width - 612, i * 100)
            if player_btn.collision():
                return i

    def draw_players(self, players, current_player):
        if current_player <= players:
            self.game.screen.blit(self.background.image, self.background.rect)
            DrawText(self.game.screen, "Player {}, please enter a name:".format(current_player),
                     self.game.white, self.game.width - 512, 100)

            self.game.textinput.update(pygame.event.get())
            self.game.screen.blit(self.game.textinput.get_surface(), (10, 10))

            next = DrawButton(self.game.screen, self.game.green, self.game.white, "Next", 200, 50,
                              self.game.width-200, self.game.height-50)
            quit = DrawButton(self.game.screen, self.game.green, self.game.white, "Quit", 200, 50,
                              200, self.game.height-50)

            if next.collision():
                draw_players(players, current_player+1)
            if quit.collision():
                return 0




