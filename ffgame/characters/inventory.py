"""
Abstraction of Inventory
"""


class Inventory(object):
    """
    Inventory class
    """

    def __init__(self):
        """
        Set initial values of attributes
        """
        self.owner = None
        self.items = []

    def get_owner(self):
        """
        Return owner
        """
        return self.owner

    def get_items(self):
        """
        Get items
        """
        return self.items
