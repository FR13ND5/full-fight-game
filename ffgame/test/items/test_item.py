import ffgame.items.item

def test_init():
    item = ffgame.items.item.Item()
    assert item.name is None
    assert item.type is None
    assert item.price is None
    assert item.equip is False

def test_get_functions():
    item = ffgame.items.item.Item()
    assert item.get_name() is None
    assert item.get_type() is None
    assert item.get_price() is None
    assert item.get_equip() is False
