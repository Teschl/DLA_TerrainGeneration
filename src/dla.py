import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.colors import LightSource
import math


def show(map):
    #ls = LightSource(azdeg=270, altdeg=60)
    #hillshade = ls.hillshade(map)
    img = plt.imshow(map, cmap='gray')
    #img_overlay = plt.imshow(hillshade,  cmap="gray", alpha=0.25)
    plt.colorbar(img)
    plt.show()

def gen256():
    crisp = np.zeros(shape=(16, 16), dtype=np.float32)
    crisp = dla(crisp)

    for i in [32,64,128,256]:
        crisp = upscale(crisp, i)
        blurry = blur(crisp, i)

        crisp = dla(crisp)
        blurry = blurry + crisp


def dla(map):
    for counter in range(map.shape[0]):
        map = addPixel(map)
    
    return map

def blur(map, newsize):
    result = np.zeros(shape=(newsize, newsize), dtype=np.float32)

    #TODO implement blurring with upscale
    for x in range(newsize-1):
        for y in range(newsize-1):
            pass

    return result

def upscale(map, newsize):
    result = np.zeros(shape=(newsize, newsize), dtype=np.float32)

    for x in range(newsize-1):
        for y in range(newsize-1):
            nearest_x = int(x / 2)
            nearest_y = int(y / 2)

            result[x][y] = map[nearest_x][nearest_y]

    return result

def addPixel(map):
    # mitte der map
    x = int((map.shape[0]-1) /2)
    y = int((map.shape[1]-1) /2)

    # if center not 1 set to 1
    if map[x][y] == 0.0:
        map[x][y] = 1.0
        return map
    
    while map[x][y] != 0.0:
        x = random.randrange(start=0, stop=map.shape[0]-1)
        y = random.randrange(start=0, stop=map.shape[1]-1)

    # move new pixel until connected to other pixels
    while not connected(map, x, y):
        x, y = move(x, y)
        x, y = stay_in_bounds(map, x, y)
        

    map[x][y] = 1.0
    return map

def stay_in_bounds(map, x, y):
    #print("nr1: ",x,y)
    if x == 0:
        x = 1
    if x == map.shape[0]-1:
        x = map.shape[0]-2
    if y == 0:
        y = 1
    if y == map.shape[1]-1:
        y = map.shape[1]-2
    #print("nr2: ",x,y)

    return x, y

def connected(map, x, y):
    if map[x+1][y] != 0 or map[x-1][y] != 0 or map[x][y+1] != 0 or map[x][y-1] != 0:
        return True
    else:
        return False

def move(x, y):
    direction = random.randint(0,3)
    if direction == 0:
        x += 1
    elif direction == 1:
        y += 1
    elif direction == 2:
        x -= 1
    else:
        y -= 1

    return x, y


def main():
    map = gen256()
    show(map)

if __name__=="__main__": 
    main() 