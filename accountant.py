import time
class Accountant:
    def __init__(self, end: int):
        """This function establishes the data for all the accountant but it does not work properly"""
        self.score = 0
        self.coins = 0
        self.start = time.time()
        self.end = end
        self.time = None
        self.sprite_coin = (0, 48, 104, 16, 16)
        self.sprite_heart = (0, 0, 120, 16, 16)
        self.x = 32
        self.y = 20

