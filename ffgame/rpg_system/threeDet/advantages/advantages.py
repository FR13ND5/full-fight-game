def acceleration(active_player):
    """
    gives one more point to use in movements (ability)
    cost: 1
    :param active_player:
    """
    active_player.points_to_spend -= 1
    active_player.persuasion += 1
    active_player.acceleration = True


def great_appearance(active_player):
    """
    gives one more point to (atuacao, labia and seduction)
    cost: 1
    :param active_player:
    """
    active_player.points_to_spend -= 1
    active_player.acting += 1
    active_player.persuasion += 1
    active_player.seduction += 1
    active_player.great_appearance = True


def inofensive_appearance(active_player):
    """
    gives you one more point to initiative on the first turn (initiative)
    cost: 1
    :param active_player:
    """
    active_player.points_to_spend -= 1
    active_player.initiative += 1
    active_player.inofensive_appearance = True


def monstruous_appearance(active_player):
    """
    gives you some bonus, in other hand reducers too
    cost: -1
    :param active_player:
    """
    active_player.points_to_spend -= 1
    active_player.interrogation += 1
    active_player.intimidation += 1
    active_player.persuasion -= 1
    active_player.seduction -= 1
    active_player.monstruous_appearance = True


def arcane(active_player):
    """
    gives you one more point on all six paths of magic
    cost: 4
    :param active_player:
    """
    # TODO: put the six paths here
    active_player.points_to_spend -= 4
    active_player.arcane = True


def battle_area_teleport(active_player):
    """
    teleports the active player or two more players (or enemies) to a place on the battlefield
    cost: 2 points
    note: 4 mp to use, you can use again only 1d turns after
    :param active_player:
    """
    active_player.points_to_spend -= 2
    active_player.battle_area_teleport = True


def preferred_arena(active_player, arena):
    """
    teleports the active player or two more players (or enemies) to a place on the battlefield
    cost: 1 points
    note: gives two more points on ability if active player fights on the specific arena
    :param arena: the preferred arena
    :param active_player:
    """
    active_player.points_to_spend -= 1
    active_player.preferred_arena = arena, True

    # TODO: stopped in page 17
