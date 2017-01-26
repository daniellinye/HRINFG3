import pygame
import time
from random import randint

#inspection cannot resolve names
import libdef



class DrawDiceScreen:
    def __init__(self, game):
        self.drawing = True
        self.game = game


    def drawScreen(self, player):
        # background
        self.game.screen.fill((255, 255, 255))
        self.player = player

        # roll button
        self.roll = libdef.DrawButton(self.game.screen, self.game.green, self.game.white, "Player {} Roll Dice".format(self.player.id), 500, 125, (self.game.width * 0.5),
                               (self.game.height * 0.5))

        # flip updated screen
        if self.roll.collision():
            self.number = randint(1,6)
            self.number2 = randint(1,6)
            self.player.roll = self.number
            return 500


    def drawScreen1(self):
        # background
        self.game.screen.fill((255, 255, 255))
        # dice image
        img = './assets/white_dice/{}.png'.format(self.number)
        self.image = libdef.DrawImage(self.game.screen, img, self.game.width-512, self.game.height*0.2)
        # text beneath image
        self.text = libdef.DrawText(self.game.screen, "You rolled a {}!".format(self.number), self.game.red, self.game.width-512, self.game.height*0.4)
        #add roll to player

        # continue button
        self.continu = libdef.DrawButton(self.game.screen, self.game.green, self.game.white, "Continue", 200, 50, (self.game.width * 0.5),(self.game.height * 0.5))

        # flip updated screen
        if self.continu.collision():
            return 500


    def drawScreen2(self, players):
        self.players = players
        # background
        self.game.screen.fill((255, 255, 255))
        sort = sorted(self.players, key = lambda player: player.roll, reverse = True)
        self.text2 = libdef.DrawText(self.game.screen, "The playing order will be:", (0,0,0), self.game.width*0.5, self.game.height*0.2)
        x = 0.3
        y = 0
        for i in range(len(self.players)) :
            self.text3 = libdef.DrawText(self.game.screen, "{}".format(sort[y].name), (0,0,0), self.game.width*0.5, self.game.height*x)
            x += 0.1
            y += 1
        self.continu2 = libdef.DrawButton(self.game.screen, self.game.green, self.game.white, "Continue", 200, 50,
                                         (self.game.width * 0.5), (self.game.height * 0.8))

        if self.continu2.collision():
            return sort


    def drawScreen3(self, player):
        self.player = player
        # background
        self.game.screen.fill((255, 255, 255))
        # dice image
        img = './assets/white_dice/{}.png'.format(self.number)
        img2 = './assets/red_dice/{}.png'.format(self.number2)
        self.image = libdef.DrawImage(self.game.screen, img, self.game.width-612, self.game.height*0.2)
        self.image2 = libdef.DrawImage(self.game.screen, img2, self.game.width - 412, self.game.height * 0.2)
        # text beneath image
        self.text = libdef.DrawText(self.game.screen, "You rolled a {} and a {}!".format(self.number,self.number2), self.game.red, self.game.width-512, self.game.height*0.4)
        # text next to dice
        self.text2 = libdef.DrawText(self.game.screen, "What type of question", (0, 0, 0), 180, self.game.height*0.2)
        self.text3 = libdef.DrawText(self.game.screen, "How may steps", (0, 0, 0), 824, self.game.height * 0.2)
        # continue button
        self.continu3 = libdef.DrawButton(self.game.screen, self.game.green, self.game.white, "Are you ready?", 250, 50, (self.game.width * 0.5),(self.game.height * 0.5))

        # flip updated screen
        if self.continu3.collision():
            if self.number == 1 or self.number == 3 or self.number == 5:
                player.type = "open"
            else:
                player.type = "mul"
            if self.number2 == 1 or self.number2 == 2:
                player.steps = 1
            elif self.number2 == 3 or self.number2 == 4:
                player.steps = 2
            else:
                player.steps = 3
            return 10




