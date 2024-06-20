#!/usr/bin/env python3
from load_image import ft_load
import matplotlib.pyplot as plt
from sys import argv


def rgb_to_gray(img):
    """converts an image to grayscale
    img is a 3d array, the last dimension is the RGB channels
    returns a 2d array of the grayscale image"""
    return img[:, :, 0] * 0.2989 + img[:, :, 1] * 0.5870 \
        + img[:, :, 2] * 0.1140
# https://en.wikipedia.org/wiki/Luma_(video)
# https://en.wikipedia.org/wiki/Grayscale


def ft_zoom(img):
    """zooms in the image in the center"""
    zoom_factor = 4
    h = img.shape[0]
    w = img.shape[1]
    z_h = h // zoom_factor
    z_w = w // zoom_factor
    return img[h // 2 - z_h: h // 2 + z_h, w // 2 - z_w: w // 2 + z_w]


def main():
    """main function to load an image then zoom in"""
    try:
        if len(argv) < 2:
            file = "/mnt/nfs/homes/thi-le/Tham_42/animal.jpeg"
        else:
            file = argv[1]
        img = ft_load(file)
        print("Original image")
        print(img)
        plt.imshow(img)
        plt.draw()
        plt.pause(1)
        zoom = ft_zoom(img)
        print("Zoomed image")
        print(zoom)
        plt.imshow(zoom)
        plt.draw()
        plt.pause(1)
        grey = rgb_to_gray(zoom)
        print("Grayscale image of the zoomed image")
        print(grey)
        plt.imshow(grey, cmap="gray")
        plt.show()

    except FileNotFoundError:
        print("An error occured: file not found")
    except Exception as e:
        print("An error occured:", e)


if __name__ == "__main__":
    main()
