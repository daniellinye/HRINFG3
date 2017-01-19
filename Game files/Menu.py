import pygame

#inspection cannot resolve names
from __init__ import iV

#starting inits
game = iV()

#TODO sprint 24
#TODO have menu switch
#TODO make menu interactive

class Menu():

    def __init__(self):
        while process_events():
            # update

            # draw logic
            game.screen.fill(game.black)

            # draw entities


            # draw score
            score_surface = game.font.render("Score: {}".format(game.score), 1, game.white)
            start_surface = game.font.render("Start", 1, game.white, (1, 1, 1))

            game.screen.blit(score_surface, (16, 16))
            game.screen.blit(start_surface, (game.width * 0.5, game.height * 0.5))

            # must also flip backscreen
            pygame.display.flip()


def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

menu = Menu()





