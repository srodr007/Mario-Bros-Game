import pyxel
class Sprites:
    def __init__(self, x: int, y: int, type: str):
        """This method establishes the x, y and type parameter for all the objects
        Also we have to initialized a variable for movement"""
        self.x = x
        self.y = y
        self.type = type
        self.move_sprites = 0

    def show_sprites(self):
        """This function makes that each type of object that is gone to be show has each different sprite"""
        if self.type == "floor":
            pyxel.blt(self.x, self.y, 0, 32, 104, 16, 16)
        if self.type == "normal":
            pyxel.blt(self.x, self.y, 0, 0, 16, 16, 16)
        elif self.type == "empty":
            pyxel.blt(self.x, self.y, 0, 16, 16, 16, 16)
        elif self.type == "question":
            pyxel.blt(self.x, self.y, 0, 16, 0, 16, 16)
        elif self.type == "pipe":
            pyxel.blt(self.x, self.y, 0, 32, 0, 32, 32)
        elif self.type == "big pipe":
            pyxel.blt(self.x, self.y , 0, 32, 0, 32, 32)
            pyxel.blt(self.x, self.y + 32, 0, 32, 16, 32, 16)
        elif self.type == "stair":
            pyxel.blt(self.x, self.y, 0, 16, 168, 16, 16)
        elif self.type == "flower":
            pyxel.blt(self.x, self.y, 0, 16, 32, 16, 16)
        elif self.type == "blue":
            pyxel.blt(self.x, self.y, 0, 0, 0, 16, 16, 12)
        elif self.type == "mushroom":
            pyxel.blt(self.x, self.y, 0, 16, 104, 16, 16)
        elif self.type == "coin":
            pyxel.blt(self.x, self.y, 0, 48, 104, 16, 16)
        elif self.type == "flag":
            pyxel.blt(self.x, self.y, 0, 0, 200, 16, 96)


