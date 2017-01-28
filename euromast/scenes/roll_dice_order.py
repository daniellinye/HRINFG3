from components import stateManagment, formControl, player
from functools import partial
from random import randint
import pygame as pg

class Start(stateManagment.BaseScene):
    def __init__(self, screen, helpers):
        super(Start, self).__init__()
        self.screen = screen
        self.done = False
        self.next_state = 'ROLL_DICE_TURNS.ROLLED'
        self.vars = helpers['vars']
        self.assets =  helpers['assets']
        self.screen_color = pg.Color('white')
        Button = formControl.Button
        game = self.vars['pygame']
        self.centerOfScreen = (game['width'] / 2)
        self.vertical_center_of_screen = (game['height'] / 2)

        self.throwDiceBtn = formControl.Button((self.centerOfScreen - 150, self.vertical_center_of_screen - 50, 300, 100),
            pg.Color('green'),
            self.nextState,
            font=self.vars['fonts']['medium'])



    # def next_player(self):
    #     game_state = self.persist['game_state']
    #     self.playerIndex = self.playerIndex + 1
    #     print('triggered next player')
    #     if self.playerIndex != len(game_state['players']) and self.playerIndex < len(game_state['players']):
    #         self.next_state = 'ROLL_DICE_TURNS'
    #         self.currentPlayer = game_state['players'][self.playerIndex]
    #         self.throwDiceBtn.update_text('{0} roll the dice'.format(self.currentPlayer.get_name()))
    #         return
    #
    #     self.next_state = 'ROLL_DICE_TURNS.SHOW_ORDER'

    def nextState(self):
        print('triggered throw dice')
        self.done = True

    # def renderShowOrder(self, surface):
    #     surface.fill((255, 255, 255))
    #
    #     players = self.persist['game_state']['players']
    #
    #     game = self.vars['pygame']
    #
    #     sort = sorted(players, key = lambda player: player.roll, reverse = True)
    #     self.playingOrderText.draw(surface)
    #     self.pickCategoryBtn = formControl.Button((self.centerOfScreen - 100, game['height'] - 100, 200, 50),
    #         pg.Color('green'),
    #         self.nextScene,
    #         text='Continue',
    #         font=self.vars['fonts']['medium']).update(surface)
    #     x = 0.3
    #     for i in range(len(sort)):
    #         formControl.Text((game['width']*0.5, game['height']*x),
    #             "{}".format(sort[i].name),
    #             self.vars['fonts']['medium'],
    #             pg.Color('black')).draw(surface)
    #         x += 0.1


    # def renderThrownDice(self, surface):
    #     # background
    #     surface.fill((255, 255, 255))
    #     # dice image
    #     img = self.assets['wdlist']['dice{0}'.format(self.thrownNumber)]
    #
    #     formControl.Image((self.vars['pygame']['width'] - 512, self.vars['pygame']['height'] * .4), img).draw(surface)
    #
    #     self.thrownText.draw(surface)
    #     self.thrownText.updateText( "You rolled a {}!".format(self.thrownNumber))
    #     #add roll to player
    #
    #     self.continueBtn.update(surface);

    def startup(self, persistent):
        self.persist = persistent
        game_state = self.persist['game_state']
        self.currentPlayer = game_state['players'][game_state['currentPlayerIndex']]
        self.throwDiceBtn.update_text('{0} roll the dice'.format(self.currentPlayer.get_name()))

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        self.throwDiceBtn.check_event(event)

    def update(self, dt):
        pass

    def draw(self, surface):
        surface.fill(self.screen_color)
        self.throwDiceBtn.update(surface);

class Roll(stateManagment.BaseScene):
    def __init__(self, screen, helpers):
        super(Roll, self).__init__()
        self.screen = screen
        self.done = False
        self.next_state = 'ROLL_DICE_TURNS.ROLLED'
        self.vars = helpers['vars']
        self.assets =  helpers['assets']
        self.screen_color = pg.Color('white')
        Button = formControl.Button
        game = self.vars['pygame']
        self.centerOfScreen = (game['width'] / 2)
        self.vertical_center_of_screen = (game['height'] / 2)

        self.thrownText = formControl.Text((self.centerOfScreen - 100, self.vertical_center_of_screen - 100),
            '',
            self.vars['fonts']['medium'],
            pg.Color('red')
        )
        self.continueBtn = formControl.Button((self.centerOfScreen - 150, self.vertical_center_of_screen - 50, 300, 100),
            pg.Color('green'),
            self.next_player,
            text='Continue',
            font=self.vars['fonts']['medium'])

    def next_player(self):
        self.persist['game_state']['currentPlayerIndex'] = self.persist['game_state']['currentPlayerIndex'] + 1
        playerIndex = self.persist['game_state']['currentPlayerIndex']
        if playerIndex != len(self.persist['game_state']['players']) and playerIndex < len(self.persist['game_state']['players']):
            self.next_state = 'ROLL_DICE_TURNS.ROLL'
            self.done = True
            return

        self.next_state = 'ROLL_DICE_TURNS.SHOW_ORDER'
        self.done = True
    def startup(self, persistent):
        self.persist = persistent
        self.thrownNumber = randint(1,6)

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        self.continueBtn.check_event(event)

    def update(self, dt):
        pass

    def draw(self, surface):
        # background
        surface.fill((255, 255, 255))
        # dice image
        img = self.assets['wdlist']['dice{0}'.format(self.thrownNumber)]

        formControl.Image((self.vars['pygame']['width'] - 512, self.vars['pygame']['height'] * .4), img).draw(surface)

        self.thrownText.draw(surface)
        self.thrownText.updateText("You rolled a {}!".format(self.thrownNumber))
        #add roll to player

        self.continueBtn.update(surface);
