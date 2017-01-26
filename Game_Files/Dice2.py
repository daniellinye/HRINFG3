import pygame
import time
from random import randint

#inspection cannot resolve names
from IV import *
import libdef

#starting inits
game = IV()


class DrawDiceScreen:
    def __init__(self):
        self.drawing = True

    def drawScreen(self):
        # background
        game.screen.fill((255, 255, 255))

        # roll button
        self.roll = libdef.DrawButton(game.screen, game.green, game.white, "Roll Dice", 500, 125, (game.width * 0.5),
                               (game.height * 0.5))

    def logicDrawScreen(self):
        self.roll.collision(game.red)

        # flip updated screen
        if self.roll.collision():
            self.number = randint(1,6)
            self.number2 = randint(1,6)
            return 101

    def drawScreen3(self):
        # background
        game.screen.fill((255, 255, 255))
        # dice image
        img = './assets/white_dice/{}.png'.format(self.number)
        img2 = './assets/red_dice/{}.png'.format(self.number2)
        self.image = libdef.DrawImage(game.screen, img, game.width-612, game.height*0.2)
        self.image2 = libdef.DrawImage(game.screen, img2, game.width - 412, game.height * 0.2)
        # text beneath image
        self.text = libdef.DrawText(game.screen, "You rolled a {} and a {}!".format(self.number,self.number2), game.red, game.width-512, game.height*0.4)
        # text next to dice
        self.text2 = libdef.DrawText(game.screen, "What kind of question", (0, 0, 0), 180, game.height*0.2)
        self.text3 = libdef.DrawText(game.screen, "How may steps", (0, 0, 0), 824, game.height * 0.2)
        # continue button
        self.continu = libdef.DrawButton(game.screen, game.green, game.white, "Are you ready?", 200, 50, (game.width * 0.5),(game.height * 0.5))

        # flip updated screen
        if self.continu.collision():
            if self.number == 1 or self.number == 3 or self.number == 5:
                kind = "open"
            else:
                kind = "mul"
            if self.number2 == 1 or self.number2 == 2:
                steps = 1
            elif self.number2 == 3 or self.number2 == 4:
                steps = 2
            else:
                steps = 3
            return [kind, steps]


