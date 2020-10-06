# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
import random
import string
import requests
#import enchant

""" Class Game """


class Game:
    """ Init a grid at 9 letters """

    def __init__(self):
        self.grid = []
        for i in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))

    """ check if word is valid and all letters are in the list """

    def is_valid(self, word):
#        dictionnaries = enchant.Dict("en_US")
        letters = self.grid.copy()
        if not word:
            return False
#        if not dictionnaries.check(word):
#            return False
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
        return self.check_dictionnary(word)

    @staticmethod
    def check_dictionnary(word):
        response = requests.get(f"https://wagon-dictionary.herokuapp.com/{word}")
        return response.json()['found']
