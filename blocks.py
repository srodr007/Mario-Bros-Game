from sprites import Sprites
from accountant import Accountant
from enemies import Enemies
import random
class Blocks:
    def __init__(self, mario):
        """This method establishes lists will all the blocks for the map, in order to work in an easier way
        There is a list for objects and for enemies. The floor is created on a loop"""
        self.mario = mario
        self.accountant = Accountant(100)
        self.sprites = [Sprites(224, 158, "question"), Sprites(300, 158, "normal"), Sprites(316, 158, "question"), Sprites(332, 158, "normal"),
                        Sprites(348, 158, "question"), Sprites(360, 208, "mushroom"), Sprites(440, 192, "pipe"),  Sprites(570, 186, "big pipe"),
                        Sprites(717, 208, "stair"), Sprites(717 + 16, 208, "stair"), Sprites(717 + 16, 208 -16, "stair"), Sprites(717 + 32, 208, "stair"),
                        Sprites(717 + 32, 208 - 16, "stair"), Sprites(717 + 32, 208- 32, "stair"),
                        Sprites(717+ 48, 208, "stair"), Sprites(717 + 48, 208 -16, "stair"), Sprites(717 + 48, 208 - 32, "stair"),
                        Sprites(717 + 48, 208 - 48, "stair"), Sprites(717 + 64, 208, "stair"), Sprites(717 + 64, 208 - 16, "stair"),
                        Sprites(717 + 64, 208 - 32, "stair"), Sprites(717 + 64, 208 - 48, "stair"), Sprites(717 + 64, 208 - 64, "stair"),
                        Sprites(813, 208, "goomba"), Sprites(840, 208, "goomba"), Sprites(924, 175, "normal"), Sprites(940, 175, "question"),
                        Sprites(974, 145, "normal"), Sprites(990, 145, "normal"), Sprites(1100, 158, "normal"), Sprites(1116, 158, "question"),
                        Sprites(1132, 158, "normal"), Sprites(1180, 208, "normal"),
                        Sprites(1200, 208, "goomba"), Sprites(1240, 208, "normal"), Sprites(1270, 158, "question"), Sprites(1286, 158, "normal"),
                        Sprites(1302, 158, "question"), Sprites(1420, 208, "stair"),
                        Sprites(1420 + 16, 208, "stair"), Sprites(1420 + 16, 208 -16, "stair"),
                        Sprites(1420 + 32, 208, "stair"), Sprites(1420 + 32, 208 - 16, "stair"), Sprites(1420 + 32, 208- 32, "stair"),
                        Sprites(1420 + 48, 208, "stair"), Sprites(1420 + 48, 208 -16, "stair"), Sprites(1420 + 48, 208 - 32, "stair"),
                        Sprites(1420 + 48, 208 - 48, "stair"), Sprites(1420 + 64, 208, "stair"), Sprites(1420 + 64, 208 - 16, "stair"),
                        Sprites(1420 + 64, 208 - 32, "stair"), Sprites(1420 + 64, 208 - 48, "stair"), Sprites(1420 + 64, 208 - 64, "stair"),
                        Sprites(1800, 170, "flag")]
        self.enemies = [Enemies(602, "left", "goomba"), Enemies(425, "left", "goomba"), Enemies(813, "left", "goomba"),
                        Enemies(840, "left", "goomba"), Enemies(2650, "left", "goomba"), Enemies(2750, "left", "turtle"),
                        Enemies(1480, "left", "bullet")]
        n = 0
        for i in range(200):
            self.sprites.append(Sprites(n, 240, "floor"))
            self.sprites.append(Sprites(n, 224, "floor"))
            n += 16

    def movement(self, n):
        """This function affects the movement of the objects when mario moves"""
        for element in self.sprites:
            element.x -= n

    def right_collision(self):
        """This function establishes the collision when mario hits something on his right. We have to take into account,
        the big mario, the enemies, the pipes, the flag and all the sprites that make Mario interact"""
        if not self.mario.big:
            for element in self.sprites:
                if element.type == "pipe" or element.type == "big pipe":
                    if element.x <= self.mario.x + 15 <= element.x + 8 and (element.y < self.mario.y < element.y + 31 or
                                                                            self.mario.y + 15 > element.y > self.mario.y):
                        self.mario.x = element.x - 15
                elif element.type == "flag":
                    if element.x <= self.mario.x + 15 <= element.x + 8 and (element.y < self.mario.y < element.y + 95 or
                                                                            self.mario.y + 15 > element.y > self.mario.y):
                        self.mario.finish = True
                else:
                    if element.x <= self.mario.x + 15 <= element.x + 8 and (element.y < self.mario.y < element.y + 15 or
                                                                            self.mario.y + 15 > element.y > self.mario.y):
                        self.mario.x = element.x - 15
                        if element.type == "mushroom":
                            self.accountant.score += 100
                            self.mario.big = True
                            self.mario.y -= 16
                            self.sprites.remove(element)
                        if element.type == "coin":
                            self.accountant.coins += 1
                            self.sprites.remove(element)
            for element in self.enemies:
                if element.type != "shell" and element.type != "bullet":
                    if element.x <= self.mario.x + 15 <= element.x + 8 and (element.y < self.mario.y < element.y + 15 or
                                                                            self.mario.y + 15 > element.y > self.mario.y):
                        self.mario.x = 20
                        self.mario.lives -= 1
                        if element.type == "goomba":
                            self.enemies.remove(element)
                        elif element.type == "turtle":
                            element.type = "shell"
                            element.y += 4
                        self.accountant.score += 100
        else:
            for element in self.sprites:
                if element.type == "pipe" and element.type == "big pipe":
                    if element.x <= self.mario.x + 15 <= element.x + 8 and (element.y < self.mario.y < element.y + 31 or
                                                                            self.mario.y + 31 > element.y > self.mario.y):
                        self.mario.x = element.x - 15
                elif element.type == "flag":
                    if element.x <= self.mario.x + 15 <= element.x + 8 and (element.y < self.mario.y < element.y + 95 or
                                                                            self.mario.y + 31 > element.y > self.mario.y):
                        self.mario.finish = True
                else:
                    if element.x <= self.mario.x + 15 <= element.x + 8 and (element.y < self.mario.y < element.y + 15 or
                                                                            self.mario.y + 31 > element.y > self.mario.y):
                        self.mario.x = element.x - 15
                        if element.type == "mushroom":
                            self.accountant.score += 100
                            self.mario.big = False
                            self.mario.y += 16
                            self.sprites.remove(element)
                        if element.type == "coin":
                            self.accountant.coins += 1
                            self.sprites.remove(element)
            for element in self.enemies:
                if element.type != "shell" and element.type != "bullet":
                    if element.x <= self.mario.x + 15 <= element.x + 8 and (element.y < self.mario.y < element.y + 15 or
                                                                            self.mario.y + 31 > element.y > self.mario.y):
                        self.mario.big = False
                        self.mario.sprite = (0, 0, 48, 16, 16)
                        self.mario.y -= 16
                        self.mario.x = element.x - 15
                        if element.type == "goomba":
                            self.enemies.remove(element)
                        elif element.type == "turtle":
                            element.type = "shell"
                            element.y += 4
                        self.accountant.score += 100



    def left_collision(self):
        """This function establishes the collision when mario hits something on his left. We have to take into account
        the same things of above"""
        if not self.mario.big:
            for element in self.sprites:
                if element.type == "pipe" or element.type == "big pipe":
                    if element.x + 21 <= self.mario.x <= element.x + 31 and (element.y < self.mario.y < element.y + 31 or
                                                                             self.mario.y + 15 > element.y > self.mario.y):
                        self.mario.x = element.x + 31
                else:
                    if element.x + 5 <= self.mario.x <= element.x + 15 and (element.y < self.mario.y < element.y + 15 or
                                                                            self.mario.y + 15 > element.y > self.mario.y):
                        self.mario.x = element.x + 15
                        if element.type == "mushroom":
                            self.accountant.score += 100
                            self.mario.big = True
                            self.mario.y -= 16
                            self.sprites.remove(element)
                        if element.type == "coin":
                            self.accountant.coins += 1
                            self.sprites.remove(element)
            for element in self.enemies:
                if element.type != "shell" and element.type != "bullet":
                    if element.x + 5 <= self.mario.x <= element.x + 15 and (element.y < self.mario.y < element.y + 15 or
                                                                            self.mario.y + 15 > element.y > self.mario.y):
                        self.mario.x = 20
                        self.mario.lives -= 1
                        if element.type == "goomba":
                            self.enemies.remove(element)
                        elif element.type == "turtle":
                            element.type = "shell"
                            element.y += 4
                        self.accountant.score += 100


        else:
            for element in self.sprites:
                if element.type == "pipe" and element.type == "big pipe":
                    if element.x + 21 <= self.mario.x <= element.x + 31 and (element.y < self.mario.y < element.y + 31 or
                                                                            self.mario.y + 31 > element.y > self.mario.y):
                        self.mario.x = element.x + 31
                else:
                    if element.x + 5 <= self.mario.x <= element.x + 15 and (element.y < self.mario.y < element.y + 15 or
                                                                            self.mario.y + 31 > element.y > self.mario.y):
                        self.mario.x = element.x + 31
                        if element.type == "mushroom":
                            self.accountant.score += 100
                            self.mario.big = False
                            self.mario.y += 16
                            self.sprites.remove(element)
                        if element.type == "coin":
                            self.accountant.coins += 1
                            self.sprites.remove(element)
            for element in self.enemies:
                if element.type != "shell" and element.type != "bullet":
                    if element.x + 5 <= self.mario.x <= element.x + 15 and (element.y < self.mario.y < element.y + 15 or
                                                                            self.mario.y + 31 > element.y > self.mario.y):
                        self.mario.big = False
                        self.mario.sprite = (0, 0, 48, 16, 16)
                        self.mario.y -= 16
                        self.mario.x = element.x - 15
                        if element.type == "goomba":
                            self.enemies.remove(element)
                        elif element.type == "turtle":
                            element.type = "shell"
                            element.y += 4
                        self.accountant.score += 100



    def up_collision(self):
        """This function establishes the collision when mario hits something above"""
        for element in self.sprites:
            if element.y + 5 <= self.mario.y <= element.y + 15 and (element.x <= self.mario.x <= element.x + 15 or
                                                                    self.mario.x <= element.x <= self.mario.x + 15):
                self.mario.y = element.y + 15
                self.mario.jumping = False
                self.mario.falling = True
                if element.type == "normal":
                    if self.mario.big:
                        self.sprites.remove(element)
                if element.type == "question":
                    chance = random.randint(0, 4)
                    if chance == 0:
                        self.sprites.append(Sprites(element.x, element.y - 16, "mushroom"))
                    else:
                        self.sprites.append(Sprites(element.x, element.y - 16, "coin"))
                    element.type = "empty"
                if element.type == "coin":
                    self.accountant.coins += 1
                    self.sprites.remove(element)
        for element in self.enemies:
            if element.type == "bullet":
                if self.mario.big:
                    if element.y + 5 <= self.mario.y <= element.y + 15 and (element.x <= self.mario.x <= element.x + 15 or
                                                                            self.mario.x <= element.x <= self.mario.x + 15):
                        self.mario.big = False
                        self.mario.x = 20
                        self.mario.y = element.y + 15
                        self.mario.jumping = False
                        self.mario.falling = True
                        self.enemies.remove(element)
                if not self.mario.big:
                    if element.y + 5 <= self.mario.y <= element.y + 15 and (element.x <= self.mario.x <= element.x + 15 or
                                                                            self.mario.x <= element.x <= self.mario.x + 15):
                        self.mario.lives -= 1
                        self.mario.x = 20
                        self.mario.y = element.y + 15
                        self.mario.jumping = False
                        self.mario.falling = True
                        self.enemies.remove(element)

    def down_collision(self):
        """This function establishes the collision when mario hits something below"""
        if not self.mario.big:
            for element in self.sprites:
                if element.type == "pipe" and element.type == "big pipe":
                    if element.y + 26 >= self.mario.y + 15 >= element.y and (element.x <= self.mario.x <= element.x + 31 or
                                                                             self.mario.x <= element.x <= self.mario.x + 15):
                        self.mario.y = element.y - 15
                else:
                    if element.y + 10 >= self.mario.y + 15 >= element.y and (element.x <= self.mario.x <= element.x + 15 or
                                                                             self.mario.x <= element.x <= self.mario.x + 15):
                        self.mario.y = element.y - 15
                        self.mario.jumping = False
                        self.mario.falling = False
                        self.mario.y_top = self.mario.y - 80
                        if element.type == "coin":
                            self.accountant.coins += 1
                            self.sprites.remove(element)
                        if element.type == "mushroom":
                            self.accountant.score += 100
                            self.mario.big = True
                            self.mario.y -= 16
                            self.sprites.remove(element)
            for element in self.enemies:
                if element.type != "shell":
                    if element.y + 10 >= self.mario.y + 15 >= element.y and (element.x <= self.mario.x <= element.x + 15 or
                                                                             self.mario.x <= element.x <= self.mario.x + 15):
                        if element.type == "goomba" or element.type == "bullet":
                            self.enemies.remove(element)
                        elif element.type == "turtle":
                            element.type = "shell"
                            element.y += 4
                        self.accountant.score += 100

        else:
            for element in self.sprites:
                if element.type == "pipe" and element.type == "big pipe":
                    if element.y + 26 >= self.mario.y + 31 >= element.y and (element.x <= self.mario.x <= element.x + 31 or
                                                                             self.mario.x <= element.x <= self.mario.x + 15):
                        self.mario.y = element.y - 31
                else:
                    if element.y + 10 >= self.mario.y + 31 >= element.y and (element.x <= self.mario.x <= element.x + 15 or
                                                                             self.mario.x <= element.x <= self.mario.x + 15):
                        self.mario.y = element.y - 31
                        self.mario.jumping = False
                        self.mario.falling = False
                        self.mario.y_top = self.mario.y - 80
                        if element.type == "coin":
                            self.accountant.coins += 1
                            self.sprites.remove(element)
                        if element.type == "mushroom":
                            self.accountant.score += 100
                            self.mario.big = False
                            self.mario.y += 16
                            self.sprites.remove(element)
            for element in self.enemies:
                if element.type != "shell":
                    if element.y + 10 >= self.mario.y + 31 >= element.y and (element.x <= self.mario.x <= element.x + 15 or
                                                                             self.mario.x <= element.x <= self.mario.x + 15):
                        if element.type == "goomba" or element.type == "bullet":
                            self.enemies.remove(element)
                        elif element.type == "turtle":
                            element.type = "shell"
                            element.y += 4
                        self.accountant.score += 100


    def gravity(self):
        """This function establishes that when mario hits something below him, there is no gravity and he does not fall
        until he passes the object"""
        if not self.mario.big:
            if self.mario.over:
                n = 0
                for element in self.sprites:
                    if element.y + 10 >= self.mario.y + 15 >= element.y and (element.x <= self.mario.x <= element.x + 15 or
                                                                             self.mario.x <= element.x <= self.mario.x + 15):
                        n += 1
                if n == 0:
                    self.mario.falling = True
                    self.mario.jumping = False
        else:
            if self.mario.over:
                n = 0
                for element in self.sprites:
                    if element.y + 10 >= self.mario.y + 31 >= element.y and (element.x <= self.mario.x <= element.x + 15 or
                                                                            self.mario.x <= element.x <= self.mario.x + 15):
                        n += 1
                if n == 0:
                    self.mario.falling = True
                    self.mario.jumping = False

    def movement_enemies(self, mov: int):
        """This function establishes the movement of all the enemies, as the sprites one"""
        self.move = mov
        for element in self.enemies:
            if element.type != "shell":
                if element.dir == "left":
                    element.x -= self.move
                else:
                    element.x += self.move
            else:
                self.move += 2
                if element.dir == "left":
                    element.x -= self.move
                else:
                    element.x += self.move


    def collision_enemies(self):
        """We wanted this function to establish collision between enemies and sprites but it does not work properly"""
        for element in self.sprites:
            if element.type != "floor" and element.type != "pipe" and element.type != "big pipe":
                for enemie in self.enemies:
                    if element.x + 5 <= enemie.x <= element.x + 15 and (element.y < enemie.y < element.y + 15 or
                                                                            enemie.y + 15 > element.y > enemie.y):
                        element.dir = "right"
                    elif element.x <= enemie.x + 15 <= element.x + 8 and (element.y < enemie.y < element.y + 15 or
                                                                          enemie.y + 15 > element.y > enemie.y):
                        element.dir = "left"
            elif element.type == "pipe" or element.type == "big pipe":
                for enemie in self.enemies:
                    if element.x + 21 <= enemie.x <= element.x + 31 and (element.y < enemie.y < element.y + 31 or
                                                                             enemie.y + 15 > element.y > enemie.y):
                        element.dir = "right"
                    elif element.x <= enemie.x + 15 <= element.x + 8 and (element.y < enemie.y < element.y + 31 or
                                                                          enemie.y + 15 > element.y > enemie.y):
                        element.dir = "left"










