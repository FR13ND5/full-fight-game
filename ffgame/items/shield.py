"""
Abstraction of item
"""
from ffgame.items.item import Item


class Shield(Item):
    """
    Shield class
    """

    def __init__(self, name):
        """
        Set initial values and call super init
        """
        Item.__init__(self)
        self.name = name
