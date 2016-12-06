import pytest
import ffgame.characters.character
from ffgame.characters.inventory import Inventory
from ffgame.items.weapon import Weapon


character = ffgame.characters.character.Character("test")


def test_init():
    assert character.get_name() == "test"
    assert character.health_point == 100
    assert isinstance(character.get_inventory(), Inventory)


def test_returns():
    assert character.attacks() == 0
    assert character.defends() == 1
    character.hit(10)
    assert character.health_point == 90
    weapon = Weapon("test", 1)
    character.equip_weapon(weapon)
    assert character.weapon == weapon


def test_raise():
    character.health_point = 0
    with pytest.raises(Exception) as execinfo:
        character.attacks()
    with pytest.raises(Exception) as execinfo:
        character.defends()
    with pytest.raises(Exception) as execinfo:
        character.hit(10)
