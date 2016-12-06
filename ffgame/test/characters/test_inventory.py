import pytest
import ffgame.characters.inventory


inv = ffgame.characters.inventory.Inventory()


def test_init():
    assert inv.owner is None
    assert inv.items == []


def test_get_functions():
    assert inv.get_owner() is None
    assert inv.get_items() == []
