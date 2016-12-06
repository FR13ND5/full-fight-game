import ffgame.items.shield


def test_init():
    weapon = ffgame.items.shield.Shield("test")
    assert weapon.name == "test"
