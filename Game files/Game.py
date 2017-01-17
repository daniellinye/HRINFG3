#Copyright 2017 Daniel Lin

import psycopg2
#TODO still need to search for asset imports
#connection = psycopg2.connect

import pygame #help us access pygame

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

        self.enemy = Enemy(self.width * 0.8, self.height * 0.5, self.height * 0.2)
        self.player = Player(self.width * 0.2, self.height * 0.5, self.height * 0.2)



#check function
def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

class Player:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def draw(self, screen):
        pygame.draw.circle(screen, green, (int(self.x), int(self.y)), int(self.r))

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= 2
        elif keys[pygame.K_RIGHT]:
            self.x += 2

        if keys[pygame.K_UP]:
            self.y -= 2
        elif keys[pygame.K_DOWN]:
            self.y += 2


class Enemy:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.health = 255

    def draw(self, screen):
        pygame.draw.circle(screen, red, (int(self.x), int(self.y)), int(self.r))



#Main program logic
def program():



    while process_events():
        #update
        Game.player.update()

        #draw logic
        Game.screen.fill(black)

        #draw entities
        Game.enemy.draw(Game.screen)
        Game.player.draw(Game.screen)

        #draw score
        score_surface = Game.font.render("Score: {}".format(score), 1, (255, 255, 255))

        Game.screen.blit(score_surface, (16,16))

        #must also flip backscreen
        pygame.display.flip()



#run program
program()


