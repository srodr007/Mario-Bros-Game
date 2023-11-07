import random
class Pipes:
    def __init__(self, x: int, y: int):
        x = random.randint(1,255)
        self.x = x
        self.y = y
        self.sprite = (0, 32, 0, 32, 32)