import ffgame.classes.warrior


warrior = ffgame.classes.warrior.Warrior("test")


def test_init():
    assert warrior.get_name() == "test"
