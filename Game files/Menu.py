import pygame

#inspection cannot resolve names
from __init__ import *

#starting inits
game = iV()

#TODO sprint 2
#TODO have menu switch
#TODO make menu interactive


class DrawButton:
    def __init__(self, screen, b_color, t_color, text, b_width, b_height, position_x, position_y):
        pygame.draw.rect(screen, b_color, [position_x, position_y, b_width, b_height], 0)
        text = game.font.render(str(text), 1, t_color)
        game.screen.blit(text, (position_x+(b_width*0.25), position_y+(b_height*0.25)))


class Menu:
    def __init__(self):
        while process_events():
            #FPS
            game.clock.tick(game.fps)

            #updates variables
            mousepos = pygame.mouse.get_pos()

            #background
            game.screen.fill((0,0,0))
            background = game.background
            game.screen.blit(background.image, background.rect)

            #fonts
            #scores
            score_surface = game.font.render("Score: {}".format(game.score), 1, game.white)
            mouse = game.font.render("Mouse: {}".format(mousepos), 1, game.white)


            DrawButton(game.screen, game.green, game.white, "Start", 125, 50, game.width*0.5, game.width*0.3)
            DrawButton(game.screen, game.green, game.white, "Settings", 125, 50, game.width*0.5, game.width*0.5)

            game.screen.blit(mouse, (game.width/2, 16))
            game.screen.blit(score_surface, (16, 16))

            #flip updated screen
            pygame.display.flip()


def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

menu = Menu()




