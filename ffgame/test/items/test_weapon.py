import ffgame.items.weapon

def test_init():
    weapon = ffgame.items.weapon.Weapon("test")
    assert weapon.name == "test"
