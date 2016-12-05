from ffgame.character.inventory import Inventory

class Character(object):

    def __init__(self):
        self.name = None
        self.hp = None # healing points
        self.mp = None # magic points
        self.f_def = None # defense points
        self.m_def = None
        self.p_attack = None # attack points
        self.m_attack = None
        self.weapon = None
        self.armor = None
        self.inventory = Inventory()
        self.alive = True

    def attacks(self):
        if self.is_dead():
            return '{name} is dead'.format(name=self.name)

    def defends(self):
       if self.is_dead():
            return '{name} is dead'.format(name=self.name)

    def speaks(self):
        pass

    def hit(self, damage):
        if self.is_dead():
            return '{name} is dead'.format(name=self.name)
        self.hp -= damage

    def is_dead(self):
        return self.hp > 0

