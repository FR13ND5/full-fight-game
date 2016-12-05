import ffgame.items.item
def test_answer():
    item = ffgame.items.item.Item()
    assert item.name is None
    assert item.type is None
    assert item.price is None
    assert item.equip is False
