from mario import Mario
import pyxel
class Floor:
    def __init__(self, x: int, y: int):
        self.x = 0
        self.y = 224
        self.mario = Mario(self.width//2, 208, True)
        for i in range(self.mario.x + 255):
            self.x += 1
            pyxel.btl(self.x + self.move_sprites, self.y, 0, 32, 104, 16, 16)
