import pygame

#inspection cannot resolve names
from __init__ import *

#starting inits
game = iV()

# TODO sprint 2
# TODO have menu switch
# TODO make menu interactive

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



class Menu:
    def __init__(self):
        state = 0
        running = True
        while process_events() and running == True:

            game.clock.tick(game.fps)
            if state == 0:
                #FPS


                #background
                game.screen.fill((0,0,0))
                background = game.background
                game.screen.blit(background.image, background.rect)

                #fonts
                #title
                score_surface = game.font.render("Euromast", 1, game.white)

                #menu buttons
                start = DrawButton(game.screen, game.green, game.white, "Start", 200, 50, game.width*0.5, game.height*0.3)
                instructions = DrawButton(game.screen, game.green, game.white, "Instructions", 200, 50, game.width * 0.5
                                          , game.height * 0.4)
                highscores = DrawButton(game.screen, game.green, game.white, "Highscores", 200, 50, game.width * 0.5,
                                          game.height * 0.5)
                settings = DrawButton(game.screen, game.green, game.white, "Settings", 200, 50, game.width * 0.5,
                                      game.height * 0.6)
                exit = DrawButton(game.screen, game.green, game.white, "Exit", 200, 50, game.width * 0.5, game.height * 0.7)

                start.follow(game.red)
                highscores.follow((20, 40, 100))
                settings.follow()

                game.screen.blit(score_surface, (16, 16))

                #flip updated screen

                if instructions.follow():
                    state = 2
                    print(state)

                if exit.follow(game.red):
                    running = False



            elif state == 2:
                game.screen.fill((0, 0, 0))
                i = 1
                for text in game.rules:
                    rRules = game.rulesfont.render(text, 1, game.white)
                    game.screen.blit(rRules, (16, 16*i))
                    i += 1
                exit = DrawButton(game.screen, game.green, game.white, "Exit", 200, 50, game.width-200, 50)
                if exit.follow(game.white):
                    state = 0

            pygame.display.flip()


def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

menu = Menu()




