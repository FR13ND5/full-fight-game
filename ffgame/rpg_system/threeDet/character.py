from rpg_system.threeDet.inventory import Inventory


class Character:

    def __init__(self):
        self.name = None
        self.age = None
        self.inventory = Inventory()

    def speaks(self):
        pass
