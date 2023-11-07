import pyxel
class Back:
    def __init__(self, x: int, y: int):
        """This method establishes the x and y of the background"""
        self.x = x
        self.y = y
        self.move_background = 0
    def movement(self):
        """This function establishes the movement of the backgrounf when mario moves"""
        pyxel.bltm(0, 0, 0, self.move_background, 66, 64, 64)



