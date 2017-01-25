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

    def drawScreen1(self):
        # background
        game.screen.fill((255, 255, 255))
        # dice image
        img = './assets/white_dice/{}.png'.format(self.number)
        img2 = './assets/red_dice/{}.png'.format(self.number2)
        self.image = libdef.DrawImage(game.screen, img, game.width-612, game.height*0.2)
        self.image2 = libdef.DrawImage(game.screen, img2, game.width - 412, game.height * 0.2)
        # text beneath image
        self.text = libdef.DrawText(game.screen, "You rolled a {} and a {}!".format(self.number,self.number2), game.red, game.width-512, game.height*0.4)
        # continue button
        self.continu = libdef.DrawButton(game.screen, game.green, game.white, "Continue", 200, 50, (game.width * 0.5),(game.height * 0.5))

    def logicDrawScreen1(self):
        self.continu.collision(game.red)

        # flip updated screen
        if self.continu.collision():
            return 102




# force quit event
def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

class RollDice:
    state = 100
    running = True
    toDraw = DrawDiceScreen()
    while process_events() and running:
        # FPS
        game.clock.tick(game.fps)
        # -----------------------------
        if state == 100:
            # keeps drawing screen
            toDraw.drawScreen()
            # logic0
            if toDraw.logicDrawScreen() == 101:
                state = 101
        # -----------------------------
        elif state == 101:
            toDraw.drawScreen1()
            if toDraw.logicDrawScreen1() == 102:
                state = 102
        elif state == 102:
            running = False
        pygame.display.flip()


rollDice = RollDice()
