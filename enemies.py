import pyxel
import random
class Enemies:
    def __init__(self, x: int, dir: str, type: str):
        """This method the Enemies objects with each x in the map, the direction of movement and type of enemie.
        The y paramter is not entered because is always the same"""
        self.x = x
        self.y = 208
        self.dir = dir
        self.type = type
        self.bullet_range = random.randint(0, 140)
        self.bullet_y = self.bullet_range
    def show_enemies(self):
        """This function shows the enemies on the screen,
        depending on the type of enemie, it will show a diferent sprite"""
        if self.type == "goomba":
            pyxel.blt(self.x, self.y, 0, 32, 48, 16, 16)
        elif self.type == "turtle":
            pyxel.blt(self.x, self.y - 10, 0, 48, 32, -16, 32, 12)
        elif self.type == "shell":
            pyxel.blt(self.x, self.y, 0, 32, 168, 16, 13)
        elif self.type == "bullet":
            pyxel.blt(self.x, self.bullet_y, 0, 48, 184, 16, 16, 12)








