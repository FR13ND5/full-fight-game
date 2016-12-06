"""
Abstraction of Warrior
"""
from ffgame.characters.character import Character

class Warrior(Character):
    """
    Warrior class
    """

    def __init__(self, name):
        """
        Set initial values of attributes
        """
        Character.__init__(self)
        self.name = name
