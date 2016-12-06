class Adventure:
    def __init__(self):
        """
        initial_points = dict with adventurer level and points to spend
        weight_limit = dict with table of kg that the char can lift
        """
        self.adventurer_level = {
            'novice': 5,
            'fighter': 7,
            'champion': 10,
            'legend': 12,
        }

        self.weight_limit_table = {
            0: 20,
            1: 50,
            2: 100,
            3: 200,
            4: 400,
            5: 800,
        }


