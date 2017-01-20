import pygame

#inspection cannot resolve names
from __init__ import *

#starting inits
game = iV()

# TODO sprint 2
# TODO have menu switch
# TODO make menu interactive
# TODO add to sprint backlog database
# TODO make a database
# TODO make a proper game-file

# TODO put class DrawButton in separate file


class DrawButton:
    def __init__(self, screen, b_color, t_color, text, b_width, b_height, position_x, position_y):
        self.screen = screen
        self.b_color = b_color
        self.t_color = t_color
        self.text = text
        self.b_width = b_width
        self.b_height = b_height
        self.position_x = position_x
        self.position_y = position_y

        self.draw()

    def draw(self, image=""):
        pygame.draw.rect(self.screen, self.b_color or image, [self.position_x, self.position_y, self.b_width, self.b_height], 0)
        text = game.font.render(str(self.text), 1, self.t_color)
        game.screen.blit(text, (self.position_x + self.b_width*0.5 - text.get_width()*0.5,
                                self.position_y + self.b_height*0.5 - text.get_height()*0.5))

    def follow(self, new_color=(0, 0, 0)):
        # Check for collision with mouse and change background color
        mouse = pygame.mouse.get_pos()
        if (mouse[0] in range(int(self.position_x), int(self.position_x + self.b_width))) \
                and (mouse[1] in range(int(self.position_y), int(self.position_y + self.b_height))):
            self.b_color = new_color
            self.draw()

            # If pressed on a button change state
            if pygame.mouse.get_pressed()[0]:

                return True

#TODO make extra buttons interactive

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

        self.start.follow(game.red)
        self.highscores.follow((20, 40, 100))
        self.settings.follow()

        # flip updated screen

        if self.instructions.follow():
            return 2
            print(state)

        if self.exit.follow(game.red):
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

        if self.exit.follow(game.white):
            return 0

    #---------------------------------------------------------





#force quit event
def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

menu = Menu()




