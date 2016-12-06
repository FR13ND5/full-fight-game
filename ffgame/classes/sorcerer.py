"""
Abstraction of Sorcerer
"""
from ffgame.characters.character import Character


class Sorcerer(Character):
    """
    Sorcerer class
    """

    def __init__(self, name):
        """
        Set initial values of attributes
        """
        Character.__init__(self, name)
