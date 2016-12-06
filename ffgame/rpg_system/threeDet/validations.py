def is_valid_points(points):
    """

    :param points: total points that player want to spent
    :return: boolean
    """
    if points >= 0 or points < 6:
        return True
    else:
        return False


def is_valid_test(total_value, reducing):
    """

    :param total_value: total value for the test
    :param reducing: the reducing value for the test
    :return: boolean
    """
    return total_value - reducing <= 0
