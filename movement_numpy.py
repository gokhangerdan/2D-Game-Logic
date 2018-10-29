import numpy as np


class game:
    scene = np.zeros([10, 10]).astype(int)
    scene[0, 0] = 1
    pos_x = 0
    pos_y = 0


print(game.scene)


# MOVE UP
def w():
    try:
        if game.pos_y == 0:
            0 / 0
        game.scene[game.pos_y - 1, game.pos_x] = 1
        game.scene[game.pos_y, game.pos_x] = 0
        game.pos_y -= 1
        print(game.scene)
    except:
        print(game.scene)


# MOVE LEFT
def a():
    try:
        if game.pos_x == 0:
            0 / 0
        game.scene[game.pos_y, game.pos_x - 1] = 1
        game.scene[game.pos_y, game.pos_x] = 0
        game.pos_x -= 1
        print(game.scene)
    except:
        print(game.scene)


# MOVE DOWN
def s():
    try:
        game.scene[game.pos_y + 1, game.pos_x] = 1
        game.scene[game.pos_y, game.pos_x] = 0
        game.pos_y += 1
        print(game.scene)
    except:
        print(game.scene)


# MOVE RIGHT
def d():
    try:
        game.scene[game.pos_y, game.pos_x + 1] = 1
        game.scene[game.pos_y, game.pos_x] = 0
        game.pos_x += 1
        print(game.scene)
    except:
        print(game.scene)
