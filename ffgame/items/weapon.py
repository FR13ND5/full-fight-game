"""
Abstraction of weapon
"""
from ffgame.items.item import Item


class Weapon(Item):
    """
    Weapon class
    """

    def __init__(self, name, attack):
        """
        Set initial values and call super init
        """
        Item.__init__(self)
        self.name = name
        self.attack = attack
