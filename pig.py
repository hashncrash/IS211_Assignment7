Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 

>>> #!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 7 Assignment
	Dave Soto
	- Pig Game"""


import random


class Die(object):
    """A game to simulate dice,
	randomizes number 1-6
    """
    random.seed(0)

    def __init__(self):
        self.rolled = 0

    def roll(self):
        """The dice roll function.

        """
        self.rolled = random.randint(1, 6)
        return self.rolled


class Player(object):
    """
    Stores the player names to be used in the pig game.
    """
    def __init__(self, name):
        self.name = name
        self.totscore = 0
        self.turnscore = 0
        self.turn_status = 0
        print 'Welcome to the game of pig, {}.'.format(self.name)


class Game(object):
    "A pig game class"
    
    def __init__(self, player1, player2):
        self.player1 = Player(player1)
        self.player2 = Player(player2)
        self.die = Die()
        self.turn(self.player1)

    def turn(self, player):
        """The initial turn function for the Pig game."""
        player.turn_status = 1
        print 'It is {}\'s turn.'.format(player.name)
        while player.turn_status == 1 and player.totscore < 100:
            roll = self.die.roll()
            if roll == 1:
                print ('Sorry {}! You rolled a 1 and lose all '
                       'points this turn. Your score is {}. Pass the die '
                       'to the next player.').format(player.name, player.totscore)
                player.turnscore = 0
                self.next_player()
            else:
                print '{} rolled a {}.'.format(player.name, roll)
                player.turnscore += roll
                print ('Your current point total '
                       'for this turn is {}. Your total '
                       'score is {}').format(player.turnscore, player.totscore)
                self.turn_choice(player)
        print ('{} score is {} and'
               'is the WINNER!').format(player.name, player.totscore)

    def turn_choice(self, player):
       
        choice = raw_input('{}, Hold or Roll?'.format(player.name))
        choice = (choice[0])
        if choice.lower() == 'h':
            player.totscore += player.turnscore
            print ('{} points have been '
                   'added to {}\'s total '
                   'score.').format(player.turnscore, player.name)
            if player.totscore >= 100:
                print ('{} wins with '
                       'a score of {}.').format(player.name, player.totscore)
                raise SystemExit
            else:
                player.turnscore = 0
                print ('{}\'s score is now {}.'
                       ' Please pass die to next'
                       'player.').format(player.name, player.totscore)
                self.next_player()
        elif choice.lower() == 'r':
            self.turn(player)
        else:
            print('***Type Hold (H/h) or Roll (R/r) only, please.***')
            self.turn_choice(player)

    def next_player(self):
        """Swithces to the next player in the game.
        Attributes:
            Game (class): Calls the Game() class.
        """
        if self.player1.turn_status == 1:
            self.player1.turn_status = 0
            self.turn(self.player2)
        else:
            self.player2.turn_status = 0
            self.turn(self.player1)
