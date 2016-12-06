"""
Abstraction of Character
"""
from ffgame.characters.inventory import Inventory
from ffgame.items.weapon import Weapon

class Character(object):
    """
    Character class
    """

    #pylint: disable=too-many-instance-attributes
    #TODO: verify number of attributes

    def __init__(self, name):
        """
        Set initial values of attributes
        """
        self.name = name
        self.health_point = 100 # healing points
        self.f_def = 1 # defense points
        self.m_def = 1
        self.p_attack = 1 # attack points
        self.m_attack = 1
        self.weapon = Weapon("", 0)
        self.inventory = Inventory()

    def get_name(self):
        """
        Return character name
        """
        return self.name

    def equip_weapon(self, weapon):
        """
        Equip a weapon
        """
        self.weapon = weapon

    def get_inventory(self):
        """
        Return character inventory
        """
        return self.inventory

    def attacks(self):
        """
        Return attack point
        """
        if self.is_dead():
            raise Exception('{name} is dead'.format(name=self.name))
        return self.p_attack + self.m_attack + self.weapon.attack

    def defends(self):
        """
        Return defends point
        """
        if self.is_dead():
            raise Exception('{name} is dead'.format(name=self.name))
        return self.f_def + self.m_def

    def hit(self, damage):
        """
        Decrement damage of health point
        """
        if self.is_dead():
            raise Exception('{name} is dead'.format(name=self.name))
        self.health_point -= damage

    def is_dead(self):
        """
        Verify the character is live or dead
        """
        return self.health_point <= 0
