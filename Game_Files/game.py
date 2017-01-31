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

    #TODO add line instance
    #changes the current player
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
            player = Player(current_player, self.game.textinput.get_text() or "Player {}".format(current_player), (0, 0)
                            , 0)
            self.game.textinput.input_string = ""
            return player
        if quit.collision():
            return False

    #TODO add line in comment on menu
    #chooses category
    def choose_category(self, player, categories):
        self.player = player
        self.categories = categories
        # background
        self.game.screen.fill((255, 255, 255))
        if "sports"  not in categories:
            self.sports = DrawButton(self.game.screen, (0,0,255), (0,0,0), "Sports", 300, 300, 150, 150)
        if "geography"  not in categories:
            self.geography = DrawButton(self.game.screen, (0,255,0), (0,0,0), "Geography", 300, 300, 750, 150)
        if "entertainment"  not in categories:
            self.entertainment = DrawButton(self.game.screen, (255,0,0), (0,0,0), "Entertainment", 300, 300, 150, 550)
        if "history" not in categories:
            self.history =  DrawButton(self.game.screen, (255,255,0), (0,0,0), "History", 300, 300, 750, 550)
        text = DrawText(self.game.screen, "{} choose a category".format(player.name), (0,0,0), self.game.width*0.5, self.game.height*0.5)

        if "sports"  not in categories:
            if self.sports.collision():
                player.add_category("sports")
                categories.append("sports")
                return categories
        if "geography" not in categories:
            if self.geography.collision():
                player.add_category("geography")
                categories.append("geography")
                return categories
        if "entertainment" not in categories:
            if self.entertainment.collision():
                player.add_category("entertainment")
                categories.append("entertainment")
                return categories

        if "history" not in categories:
            if self.history.collision():
                player.add_category("history")
                categories.append("history")
                return categories

    #chooses direction on line 88 in menu
    def choose_direction(self, player):
        self.game.screen.fill((255, 255, 255))
        self.game.sounds["main_theme"].play()

        directions = [["Left", 150, 150, (0, 0, 255)], ["Right", 750, 150, (0, 255, 0)], ["Up", 150, 550, (255, 0, 0)],
                      ["Down", 750, 550, (255, 255, 0)]]
        DrawText(self.game.screen, "{} choose a direction".format(player.name), (0, 0, 0), self.game.width * 0.5,
                 self.game.height * 0.5)
        #make so that the player can move on screen


        for i in directions:
                direction_choice = DrawButton(self.game.screen, i[3], (0, 0, 0), i[0], 300, 300, i[1], i[2])
                player.directionset(i)
                if direction_choice.collision():
                    return i[0]
