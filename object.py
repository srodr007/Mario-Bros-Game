import math
class Point:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y
    def show(self):
        return self.x, self.y
    def move(self, move_x : int, move_y : int):
        self.x += move_x
        self.y += move_y
    def dist(self, point):
        return math.sqrt(pow(point.x - self.x,2) + pow(point.y - self.y,2))
