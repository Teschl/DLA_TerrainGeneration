import matplotlib.pyplot as plt
from matplotlib.colors import LightSource


def show(map):
    plt.imshow(map, cmap='gray')
    plt.colorbar()
    plt.show()


def show_hs(map):
    ls = LightSource(azdeg=270, altdeg=60)
    hillshade = ls.hillshade(map)
    img = plt.imshow(map, cmap='gray')
    img_overlay = plt.imshow(hillshade,  cmap="gray", alpha=0.25)
    plt.colorbar(img)
    plt.show()
