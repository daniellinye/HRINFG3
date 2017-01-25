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

        self.roll.collision((0, 0, 0))

        # flip updated screen
        if self.roll.collision():
            self.number = randint(1, 6)
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

        self.continu.collision((0,0,0))

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

        self.continu2.collision((0,0,0))

        if self.continu2.collision():
            return 500





