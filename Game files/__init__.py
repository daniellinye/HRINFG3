#Copyright 2017 Daniel Lin

import psycopg2


import pygame #helps us access pygame

#RGB values (0-255) can also use other ways


class initValues:
    def __init__(self):
        #init pygame
        pygame.init()
        #set values to be imported into another file

        self.font = pygame.font.SysFont("Times", 40)

        self.black = (0, 0, 0)
        self.green = (0, 255, 0)
        self.red = (255, 0, 0)
        self.white = (255,255,255)

        self.score = 0
        self.width = 800
        self.height = 600
        self.size = (self.width, self.height)

        self.screen = pygame.display.set_mode(self.size)


        while process_events():
            # update
            self.player.update()

            # draw logic
            self.screen.fill(self.black)

            # draw entities


            # draw score
            score_surface = self.font.render("Score: {}".format(self.score), 1, self.white)
            start_surface = self.font.render("Start", 1, self.white, (1,1,1))

            self.screen.blit(score_surface, (16, 16))
            self.screen.blit(start_surface, (self.width*0.5, self.height*0.5))

            # must also flip backscreen
            pygame.display.flip()



#check function
def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True





