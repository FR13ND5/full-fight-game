from character import Character

class Sorcerer(Character):
    
    def __init__(self, name):
        super(Character, self).__init__()
        self.name = name
