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

    def logicDrawScreen(self):
        self.roll.collision(self.game.red)

        # flip updated screen
        if self.roll.collision():
            self.number = randint(1,6)
            return 1.3

    def drawScreen1(self):
        # background
        self.game.screen.fill((255, 255, 255))
        # dice image
        img = './assets/white_dice/{}.png'.format(self.number)
        self.image = libdef.DrawImage(self.game.screen, img, self.game.width-512, self.game.height*0.2)
        # text beneath image
        self.text = libdef.DrawText(self.game.screen, "You rolled a {}!".format(self.number), self.game.red, self.game.width-512, self.game.height*0.4)
        # continue button
        self.continu = libdef.DrawButton(self.game.screen, self.game.green, self.game.white, "Continue", 200, 50, (self.game.width * 0.5),(self.game.height * 0.5))

    def logicDrawScreen1(self):
        self.continu.collision(self.game.red)

        # flip updated screen
        if self.continu.collision():
            return 102




# force quit event
def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

""""
class RollDice:
    state = 100
    running = True
    toDraw = DrawDiceScreen()
    while process_events() and running:
        # FPS
        self.game.clock.tick(game.fps)
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
"""
