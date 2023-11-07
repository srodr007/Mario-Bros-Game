from mario import Mario
from back import Back
from accountant import Accountant
from blocks import Blocks
from enemies import Enemies
import pyxel
import time
import random

class Board:
    """ This class contains all the information needed to represent the
    board"""
    def __init__(self, w: int, h: int):
        """ The parameters are the width and height of the board"""
        self.width = w
        self.height = h
        # This creates a Mario at the middle of the screen in x and at y = 200
        # facing right
        self.mario = Mario(self.width//2, 208, True)
        self.back = Back(self.width, 224)
        self.accountant = Accountant(400)
        self.blocks = Blocks(self.mario)

    def update(self):
        """This function updates the constants each pyxel"""
        # Mario update
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.mario.move('right', self.width)
            if self.mario.x >= 128:
                self.mario.x = 128
                self.back.move_background += 0.4
                self.blocks.movement(3)
                self.blocks.movement_enemies(4)
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.mario.move('left', self.width)

        if pyxel.btn(pyxel.KEY_UP) and not self.mario.jumping and not self.mario.falling:
            self.mario.move("up", self.width)
        elif pyxel.btn(pyxel.KEY_SPACE) and not self.mario.jumping and not self.mario.falling:
            self.mario.move("up", self.width)
        elif self.mario.jumping == True and not self.mario.falling:
            self.mario.move("up", self.width)
        elif self.mario.falling == True and not self.mario.jumping:
            self.mario.move("down", self.width)

        enemies_chance = random.randint(0, 900)
        if enemies_chance < 30:
            type_chance = random.randint(0, 10)
            if type_chance == 1:
                self.blocks.enemies.append(Enemies(256, "left", "bullet"))


        self.blocks.down_collision()
        self.blocks.right_collision()
        self.blocks.left_collision()
        self.blocks.up_collision()
        self.blocks.gravity()
        self.blocks.collision_enemies()
        self.blocks.movement_enemies(2)

        if self.mario.lives < 1 or self.accountant.time < 0:
            self.mario.loose = True



    def draw(self):
        """This functions draws the objects each pyxel"""
        pyxel.cls(12)
        # The background
        self.back.movement()
        # The sprites
        for i in self.blocks.sprites:
            i.show_sprites()
        for i in self.blocks.enemies:
            i.show_enemies()
        # We draw Mario taking the values from the mario object
        # Parameters are x, y, image bank, the starting x and y and the size
        pyxel.blt(self.mario.x, self.mario.y, self.mario.sprite[0],
                  self.mario.sprite[1], self.mario.sprite[2], self.mario.sprite[3],
                  self.mario.sprite[4], colkey = 12)
        # Mario world
        pyxel.text(self.accountant.x, self.accountant.y, "MARIO", 7)
        pyxel.text(self.accountant.x * 2, self.accountant.y, "WORLD", 7)
        pyxel.text(self.accountant.x * 2, self.accountant.x, "1/1", 7)
        # Score
        pyxel.text(self.accountant.x, self.accountant.x, str(self.accountant.score).zfill(6), 7)
        # Coins
        pyxel.blt(self.accountant.x * 3, self.accountant.y - 10, self.accountant.sprite_coin[0],
                  self.accountant.sprite_coin[1], self.accountant.sprite_coin[2], self.accountant.sprite_coin[3],
                  self.accountant.sprite_coin[4])
        pyxel.text(self.accountant.x * 3, self.accountant.x, "X" + str(self.accountant.coins).zfill(2), 7)
        # Lives
        pyxel.blt(self.accountant.x * 4, self.accountant.y - 10, self.accountant.sprite_heart[0],
                  self.accountant.sprite_heart[1], self.accountant.sprite_heart[2], self.accountant.sprite_heart[3],
                  self.accountant.sprite_heart[4])
        pyxel.text(self.accountant.x * 4, self.accountant.x, "X" + str(self.mario.lives).zfill(2), 7)
        # Time
        self.accountant.time = self.accountant.end - int(time.time() - self.accountant.start)
        pyxel.text(self.accountant.x * 5, self.accountant.y, "TIME", 7)
        if self.mario.finish:
            pyxel.bltm(0, 0, 0, 200, 192, 64, 64)
        if self.mario.loose:
            pyxel.bltm(0, 0, 0, 9, 192, 64, 64)








