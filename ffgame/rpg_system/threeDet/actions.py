from random import randint


def its_heavy(target_balance, active_player):
    """
    add/reduce bonus to lift an item on battlefield (deduce from your lift max weigth property)
    :param active_player: the char that want to lift an item
    :param target_balance: the weight of the target
    :return: int
    """
    if target_balance <= active_player.lift_limit:
        return 1
    else:
        return randint(-3, -1)


def can_breach_the_door(type_of_targeted_door):
    """
    add/reduce bonus to breach a door (deduce from strength)
    :param type_of_targeted_door: the type of the door
    :return: int
    """
    if type_of_targeted_door == 'wood_door':
        return 2
    if type_of_targeted_door == 'brick_door':
        return randint(-2, -1)
    if type_of_targeted_door == 'blinded_door':
        return randint(-3, -5)


def do_a_back_attack():
    """
    add/reduce bonus to give a back attack (deduce from armor)
    :return: int
    """
    return randint(-2, -1)


def is_enemy_too_far():
    """
    add/reduce to give a shoot after you line of sight (deduce from firepower)
    :return: int
    """
    return randint(-1, -3)


def can_avoid_the_trap():
    """
    add/reduce chances to avoid a trap (deduce from ability)
    :return: int
    """
    return randint(-2, 0)


def can_see_the_enemy_in_your_back(self):
    """
    add/reduce bonus to see an enemy that want to give a back attack (deduce from ability)
    note: if you have special sensitivity, you Don't have a minus
    :return: int
    """
    if self.advantages['special_sensitivity']:
        return 0
    else:
        return randint(-3, -1)


def hold_a_friend():
    """
    add/reduce bonus to save a friend to fall in a trap
    note: if you fail in the test, you fall too
    :return: int
    """
    return 1


def attemp_to_hold_an_enemy():
    """
    add/reduce bonus to hold an enemy
    :return: int
    """
    return -1


def can_holding_avoid(active_player, enemy):
    """
    add/reduce bonus to avoid a holding action
    :param active_player: the char that want to break
    :param enemy: the char that holds them
    :return: int
    """
    return active_player.strength - enemy.strength


def close_to_death(active_player):
    """
    add bonus if a char is close to the death (strength or ability)
    :param active_player: the char that is close to the death
    :return: int
    """
    if active_player.close_to_death:
        return randint(0, 3)


def attributes_test_mod(level):
    """
    add/reduce bonus to pure attributes testing
    :param level: if the task is easy, medium or hard
    :return: int
    """
    if level == 'hard':
        return randint(-3, -1)
    elif level == 'medium':
        return randint(0, 1)
    else:
        return randint(2, 4)


def roll_dice():
    return randint(1, 6)
