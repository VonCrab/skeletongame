#! /usr/bin/python

##################
# Main file for the skeletongame
# Pulls most story elements from the lore module
# Please refer to license.txt for details about distro
##################

from sys import exit
from random import choice

import lore

class Scene(object):
    def start(self):
        pass

class Intro(Scene):
    def start(self):
        print(lore.intro)

class Room(Scene):
    def start(self, score):
        print("Day {0}\n".format(score))
        print(choice(lore.room))
        return self.decision(raw_input("What do you do?\n"))

    def decision(self, player_choice):
        if player_choice == 'open closet':
            return 'closet'
        elif player_choice == 'don\'t open closet':
            return 'day'
        else:
            print("\nNot sure what that is, there's always tomorrow.")
            print("You can choose to either open the closet or don't open the closet.")
            return 'day'

class Day(Scene):
    def start(self, score):
        print("The reset of the day occurs with incident.\n")

class Closet(Scene):
    def start(self, score):
        print(lore.closet.format(score))
        exit(1)

class Engine(object):
    def __init__(self, story, game_map):
        self.story = story
        self.world = game_map
        self.score = 1

    def play(self):
        print("-" * 25)
        print("Closet Skeleton: Survival Edition\n")
        self.world.get('intro').start()
        game_state = True
        while game_state:
            player_choice = self.world.get('room').start(self.score)
            self.world.get(player_choice).start(self.score)
            self.score += 1

def main():
    game_map = {
        'intro': Intro(),
        'room': Room(),
        'day': Day(),
        'closet': Closet(),
    }
    game = Engine('skeleton', game_map)
    game.play()

if __name__ == '__main__':
    main()
