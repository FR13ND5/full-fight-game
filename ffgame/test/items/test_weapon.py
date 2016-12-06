import ffgame.items.weapon


def test_init():
    weapon = ffgame.items.weapon.Weapon("test", 0)
    assert weapon.name == "test"
    assert weapon.attack == 0
