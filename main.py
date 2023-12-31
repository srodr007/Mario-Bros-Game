from board import Board
import pyxel

board = Board(255,255)
# The first thing to do is to create the screen, see API for more parameters
pyxel.init(board.width, board.height, caption="This is super Mario", fps = 30)
# Loading the pyxres file, it has a 16x16 cat in (0,0) in bank 0
pyxel.load("assets/characters.pyxres")
# Loading a 16x16 spaceship at bank 1 in (17,0)
pyxel.image(1).load(17, 0, "assets/player.png")
# To start the game we invoke the run method with the update and draw functions
pyxel.run(board.update, board.draw)
def update():
    ''' This function is executed every frame. Now it only checks if the
    Escape key or Q are pressed to finish the program'''
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()


