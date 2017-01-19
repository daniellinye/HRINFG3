#Copyright 2017 Daniel Lin

import psycopg2
#TODO still need to search for asset imports
#connection = psycopg2.connect

import pygame #helps us access pygame

#RGB values (0-255) can also use other ways
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
score = 0

class Game:
    def __init__(self):
        # starts pygame
        pygame.init()

        self.font = pygame.font.Font(None, 40)

        self.width = 800
        self.height = 600
        self.size = (self.width, self.height)

        self.screen = pygame.display.set_mode(self.size)


        while process_events():

            # draw logic
            self.screen.fill(black)

            # draw score
            pygame.draw.rect(self.screen, red, (int(self.x), int(self.y)), int(self.r))
            score_surface = self.font.render("Score: {}".format(score), 1, (255, 255, 255))

            self.screen.blit(score_surface, (16, 16))

            # must also flip backscreen
            pygame.display.flip()



#check function
def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

#Main program logic
def program():
    game = Game()


#run program
program()


