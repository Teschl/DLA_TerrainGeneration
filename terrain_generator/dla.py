import numpy as np
import random


def dla256():
    """Generate 256x256 pixels of terrain with dla.

    Returns:
        np.ndarray: Map of terrain.
    """

    map = np.zeros(shape=(8, 8), dtype=np.float32)
    map[3][3] = 1.0

    n = int(8*8*0.2)
    map = random_aggregation(map, n)

    for i in [16, 32, 64, 128, 256]:
        # TODO: #2 implement dla256
        pass

    return map


def random_aggregation(map, n):
    """Adds n new pixels randomly to existing pixels.

    Args:
        map (np.ndarray): Map of unblurred ridgelines.
        n (int): How many pixels will be added.

    Returns:
        np.ndarray: Map of now extended ridgelines.
    """
    size = map.shape[0]

    for i in range(n):
        while True:
            x = random.randrange(0, size-1)
            y = random.randrange(0, size-1)

            if map[x][y] == 0.0:
                break

        while not connected_to_ridge:
            pass

    return map


def connected_to_ridge(map, x, y):
    """Checks is pixel is connected to other pixel.

    Args:
        map (np.ndarray): Map of ridgelines
        x (int): x coordinate of pixel.
        y (int): y coordinate of pixel.

    Returns:
        bool: True when pixel is connected to other pixel.
    """
    size = map.shape[0]

    # TODO: #1 catch array out of bounds for connected_to_ridge()

    if (map[x+1][y] != 0.0 or map[x][y+1] != 0.0
            or map[x-1][y] != 0.0 or map[x][y-1] != 0.0):

        return True

    else:
        return False
