import ffgame.classes.sorcerer


sorcerer = ffgame.classes.sorcerer.Sorcerer("test")


def test_init():
    assert sorcerer.get_name() == "test"
