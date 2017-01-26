import pygame
import time
import PickQuestion
import Question
from os.path import join, dirname
from os import environ
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

#inspection cannot resolve names
from IV import *
from libdef import *


#starting inits
game = IV()


class Menu:
    def __init__(self):
        state = 0
        counter = 1
        rollbuttonscreen = True
        players = []
        categories = []
        running = True
        toDraw = DrawMenu()
        while process_events() and running:
            #FPS
            game.clock.tick(game.fps)
            #-----------------------------
            if state == 0:
                #keeps drawing menu
                toDraw.draw0()
                #logic0
                if toDraw.logic0() == 1:
                    state = 1
                elif toDraw.logic0() == 2:
                    state = 2
                elif toDraw.logic0() is False:
                    running = False
            #-----------------------------
            elif 1 <= state < 2:
                if state == 1 and toDraw.draw1():
                    state = 1.1
                    player_amount = toDraw.draw1()
                elif state == 1.1:
                    if counter <= player_amount:
                        new_player = game.main_game.customize_players(counter)
                        if new_player:
                            players.append(new_player)
                            counter += 1
                        elif new_player is False:
                            state = 0
                    else:
                        counter = 1
                        state = 1.2
                elif state == 1.2:
                    if counter <= player_amount:
                        if rollbuttonscreen:
                            dice_roll = toDraw.draw1_1(players[counter-1])
                            if dice_roll:
                                rollbuttonscreen = False
                        else:
                            dice_click = toDraw.draw1_2()
                            if dice_click:
                                rollbuttonscreen = True
                                counter += 1
                    else:
                        order = toDraw.draw1_3(players)
                        if order:
                            counter = 0
                            state = 1.3
                elif state == 1.3:
                    if len(categories) != len(order):
                        catScreen = toDraw.draw1_4(order[counter], categories)
                        if catScreen:
                            categories = catScreen
                            counter += 1
                    else:
                        counter = 1
                        state = 1.4
                elif 1.4 <= state < 1.5:
                    if counter <= player_amount:
                        if state == 1.4:
                            direction = game.main_game.choose_direction(order[counter-1])
                            if direction:
                                players[counter-1].direction = direction
                                state = 1.41
                        if state == 1.41:
                            dice2_roll = toDraw.draw1_1(order[counter - 1])
                            if dice2_roll:
                                state = 1.42
                        if state == 1.42:
                            dice2_click = toDraw.draw1_5(order[counter - 1])
                            if dice2_click:
                                state = 1.43
                        if state == 1.43:
                            question = PickQuestion.DrawPickQuestion(order[counter -1].category, game.dummyQuestions).drawScreen()
                            if question:
                                state = 1.44
                        if state == 1.44:
                            isCorrectAnswer = Question.DrawQuestion(game.dummyQuestions[0], game.dummyQuestions[0].get('answers'))
                            if isCorrectAnswer:
                                Sections().moveplayer(order[counter -1])
                                
                            counter += 1
                            state = 1.4
                    else:
                        counter = 1

            #-----------------------------
            elif state == 2:
                toDraw.draw2()
                if toDraw.logic2() == 0:
                    state = 0
            #-----------------------------
            pygame.display.flip()


class DrawMenu:
    def __init__(self):
        self.drawing = True

    #main menu == 0
    def draw0(self):
        # background
        game.screen.fill((0, 0, 0))
        self.background = Background('./assets/background.png', [0, 0])
        game.screen.blit(self.background.image, self.background.rect)

        # fonts:
        # -menu buttons
        self.start = DrawButton(game.screen, game.green, game.white, "Start", 200, 50, game.width * 0.5, game.height * 0.3)
        self.instructions = DrawButton(game.screen, game.green, game.white, "Instructions", 200, 50, game.width * 0.5 , game.height * 0.4)
        self.highscores = DrawButton(game.screen, game.green, game.white, "Highscores", 200, 50, game.width * 0.5, game.height * 0.5)
        self.settings = DrawButton(game.screen, game.green, game.white, "Settings", 200, 50, game.width * 0.5, game.height * 0.6)
        self.exit = DrawButton(game.screen, game.green, game.white, "Exit", 200, 50, game.width * 0.5, game.height * 0.7)


        # -title
        self.score_surface = game.font.render("Euromast", 1, game.white)
        game.screen.blit(self.score_surface, (512-(self.score_surface.get_width()*0.5), 16))

    def logic0(self):
        self.start.collision(game.red)
        self.highscores.collision((20, 40, 100))
        self.settings.collision()

        # flip updated screen
        if self.start.collision():
            return 1

        if self.instructions.collision():
            return 2

        if self.exit.collision(game.red):
            return False

    #--------------------------------------------------------
    def draw1(self):
        return game.main_game.choose_players()
    #--------------------------------------------------------
    def draw1_1(self, player):
        return game.dice.drawScreen(player)

    def draw1_2(self):
        return game.dice.drawScreen1()

    def draw1_3(self, players):
        return game.dice.drawScreen2(players)

    def draw1_4(self, player, categories):
        return game.main_game.choose_category(player, categories)

    def draw1_5(self,player):
        return game.dice.drawScreen3(player)

    #instructions menu
    def draw2(self):

        game.screen.fill((0, 0, 0))
        self.i = 1

        if game.page > 0:
            self.back = DrawButton(game.screen, game.green, game.white, "Back", 200, 50, 16, game.height - 50)
        else:
            self.back = DrawButton(game.screen, game.green, game.white, "Back", 200, 50, -200, -50)

        if len(game.ruleslist) == (game.page+1):
            self.next = DrawButton(game.screen, game.green, game.white, "Next", 200, 50, -200, -50)
        else:
            self.next = DrawButton(game.screen, game.green, game.white, "Next", 200, 50, game.width-200, game.height-50)

        for text in game.ruleslist[game.page]:
            rRules = game.rulesfont.render(text, 1, game.white)
            game.screen.blit(rRules, (16, 16 *self.i))
            self.i += 1
        self.exit = DrawButton(game.screen, game.green, game.white, "Exit", 200, 50, game.width - 200, 50)

    def logic2(self):

        if self.exit.collision(game.white):
            return 0
        if self.next.collision(game.white):
            time.sleep(.1)
            game.page += 1

        if self.back.collision(game.white):
            time.sleep(.1)
            game.page -= 1


    #---------------------------------------------------------





#force quit event
def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

menu = Menu()
