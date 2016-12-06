"""
Abstraction of item
"""


class Item(object):
    """
    Base class of itens
    """

    def __init__(self):
        """
        Set initial values of attributes
        """
        self.name = None
        self.type = None
        self.price = None
        self.equip = False

    def get_name(self):
        """
        Get item name
        """
        return self.name

    def get_type(self):
        """
        Get item type
        """
        return self.type

    def get_price(self):
        """
        Get item price
        """
        return self.price

    def get_equip(self):
        """
        Verify is item has equiped
        """
        return self.equip
