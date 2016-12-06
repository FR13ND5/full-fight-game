from rpg_system.threeDet.actions import roll_dice
from rpg_system.threeDet.adventure import Adventure
from rpg_system.threeDet.character import Character
from rpg_system.threeDet.phrases import give_valid_points, roll_again_for_vital_points
from rpg_system.threeDet.spells import Spells
from rpg_system.threeDet.validations import is_valid_points


class Record(Adventure, Character, Spells):
    def __init__(self, name, age='Unknown'):
        # (1) initial setup
        super(Character, self).__init__()
        super(Adventure, self).__init__()
        self.name = name
        self.age = age
        self.points_to_spend = None  # see adventure self initial points

        # (2) preferences
        self.preferred_arena = None, False

        # (3) character
        self.strength = None
        self.ability = None
        self.resistance = None
        self.armor = None
        self.firepower = None

        # (4) pv's and pm's
        self.vital_points = None
        self.magic_points = None
        self.initiative = None
        self.movements = None

        # information
        self.range = None  # depends on the weapon you are using
        self.ammunition = None  # depends on the weapon you are using
        self.weight_limit = None
        self.close_to_death = False

        # status
        self.hold = False
        self.alive = True

        # abilities
        self.seduction = None
        self.persuasion = None
        self.interrogation = None
        self.intimidation = None

        # spells
        self.battle_area_teleport = False

    def set_strength(self, spent_points):
        if is_valid_points(spent_points):
            self.strength = spent_points
        else:
            print(give_valid_points)

    def set_ability(self, spent_points):
        if is_valid_points(spent_points):
            self.strength = spent_points
        else:
            print(give_valid_points)

    def set_resistance(self, spent_points):
        if is_valid_points(spent_points):
            self.resistance = spent_points
        else:
            print(give_valid_points)

    def set_armor(self, spent_points):
        if is_valid_points(spent_points):
            self.armor = spent_points
        else:
            print(give_valid_points)

    def set_firepower(self, spent_points):
        if is_valid_points(spent_points):
            self.firepower = spent_points
        else:
            print(give_valid_points)

    def is_alive(self):
        """
        validate if a character take a hit() after reach 0 PV's
        :return: boolean
        """
        return self.vital_points > 0

    def set_vital_points(self):
        """
        to set vital points, roll 3x the dice and sum. If the result is 1, you can try again
        :return int
        """
        rolls = 0
        total_vital_points = None
        while rolls == self.resistance:
            result = roll_dice()
            if result > 1:
                total_vital_points += self.vital_points
                rolls += 1
        self.vital_points = total_vital_points

    def set_magic_points(self):
        self.resistance *= 5

    def set_movements(self):
        self.ability *= 2

    def set_weigth_limit(self):
        self.weight_limit = self.weight_limit_table[self.strength]



