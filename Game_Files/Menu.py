import pygame

#inspection cannot resolve names
from __init__ import *

#starting inits
game = IV()

# TODO sprint 2
# TODO have menu switch
# TODO make menu interactive
# TODO add to sprint backlog database
# TODO make a database
# TODO make a proper game-file

# TODO put class DrawButton in separate file


# TODO make extra buttons interactive

class Menu:
    def __init__(self):
        state = 0
        running = True
        toDraw = DrawMenu()
        while process_events() and running == True:
            #FPS
            game.clock.tick(game.fps)
            if state == 0:
                #keeps drawing menu
                toDraw.draw0()

                #logic0
                if toDraw.logic0() == 2:
                    state = 2
                elif toDraw.logic0() == False:
                    running = False


            elif state == 2:
                toDraw.draw2()
                if toDraw.logic2() == 0:
                    state = 0



            pygame.display.flip()


class DrawMenu:
    def __init__(self):
        self.drawing = True

    #main menu == 0
    def draw0(self):
        # background
        game.screen.fill((0, 0, 0))
        self.background = game.background
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
        game.screen.blit(self.score_surface, (16, 16))


    def logic0(self):

        self.start.collision(game.red)
        self.highscores.collision((20, 40, 100))
        self.settings.collision()

        # flip updated screen

        if self.instructions.collision():
            return 2
            print(state)

        if self.exit.collision(game.red):
            return False
    #--------------------------------------------------------


    #instructions menu
    def draw2(self):
        game.screen.fill((0, 0, 0))
        self.i = 1
        for text in game.rules:
            rRules = game.rulesfont.render(text, 1, game.white)
            game.screen.blit(rRules, (16, 16 * self.i))
            self.i += 1
        self.exit = DrawButton(game.screen, game.green, game.white, "Exit", 200, 50, game.width - 200, 50)

    def logic2(self):

        if self.exit.collision(game.white):
            return 0

    #---------------------------------------------------------





#force quit event
def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

menu = Menu()




