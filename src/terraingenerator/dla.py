import random
import matplotlib.pyplot as plt
import numpy as np


def dla():
    grid = np.zeros(shape=(128, 128))
    grid[64][64] = 1

    return grid


def is_neighbour():

    return False


if __name__ == '__main__':
    grid = dla()
    plt.imshow(grid)
    plt.show()
