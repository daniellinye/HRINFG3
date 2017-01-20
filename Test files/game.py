#Copyright 2017 Daniel Lin




#TODO THIS IS A TEST FILE
#TODO THIS IS A TEST FILE
#TODO THIS IS A TEST FILE
#TODO THIS IS A TEST FILE
#TODO THIS IS A TEST FILE


import psycopg2

#TODO still need to search for asset imports
#connection = psycopg2.connect

import pygame #helps us access pygame

#RGB values (0-255) can also use other ways
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

class Game:
    def __init__(self):
        # starts pygame
        pygame.init()

        self.font = pygame.font.SysFont("Times", 40)

        self.score = 0
        self.width = 800
        self.height = 600
        self.size = (self.width, self.height)

        self.screen = pygame.display.set_mode(self.size)

        self.enemy = Enemy(self.width * 0.8, self.height * 0.5, self.height * 0.2)
        self.player = Player(self.width * 0.2, self.height * 0.5, self.height * 0.2)

        while process_events():


            # update
            self.player.update()

            # draw logic
            self.screen.fill(black)

            # draw entities


            # draw score
            score_surface = self.font.render("Score: {}".format(self.score), 1, (255, 255, 255))
            start_surface = self.font.render("Start", 1, (255,255,255), (1,1,1))

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
    game = Game()




#run program
program()



class Card:
    def __init__(self, keywords, name):
        self.keywords = keywords
        self.name = name


class Deck:
    def __init__(self, cards):
        i = 0
        self.deck = []
        for card in cards:
            self.deck[i] =+ card


    def addCard(self, card):
        self.deck[self.deck.length] =+ card

    def shuffle(self):
        i = 0
        for cards in self.deck:
            return Deck(cards)


p1 = Deck(Card("lel", "lel"))


