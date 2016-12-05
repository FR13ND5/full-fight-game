from character import Character

class Warrior(Character):
    
    def __init__(self, name):
        super(Character, self).__init__()
        self.name = name
