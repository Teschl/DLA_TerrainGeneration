import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.colors import LightSource


def dla128():
    ridge_map = np.zeros(shape=(8, 8), dtype=np.uint8)
    redge_map = rand_aggregation()

    for i in [16, 32, 64, 128]:
        pass


def rand_aggregation(in_map):
    size = in_map.shape[0]
    center = int((size-1)/2)

    if in_map[center][center] == 0:
        in_map[center][center] = 1

    for i in range(size*2):

        x = random.randrange(start=0, stop=size-1)
        y = random.randrange(start=0, stop=size-1)
        while in_map[x][y] != 0:
            x = random.randrange(start=0, stop=size-1)
            y = random.randrange(start=0, stop=size-1)

        while not connected(in_map, x, y):
            x, y = rand_move(in_map, x, y)

    return in_map


def rand_move(in_map, x, y):
    pass


def connected(in_map, x, y):
    pass


def upscale(in_map, out_map):
    pass


def linear_interpolation(in_map, out_map):
    pass


def convolution(in_map, out_map):
    pass


def show(self):
    plt.imshow(self.map, cmap='gray')
    plt.colorbar()
    plt.show()


def show_hs(self):
    ls = LightSource(azdeg=270, altdeg=60)
    hillshade = ls.hillshade(map)
    img = plt.imshow(self.map, cmap='gray')
    img_overlay = plt.imshow(hillshade,  cmap="gray", alpha=0.25)
    plt.colorbar(img)
    plt.show()


def main():
    map = dla128()
    map.show()


if __name__ == "__main__":
    main()
