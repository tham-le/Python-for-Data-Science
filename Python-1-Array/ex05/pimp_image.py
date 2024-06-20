# invert: =, +, -, *
# red: =, *
# green: =, -
# blue: =
# grey: =, /

import array
import matplotlib.pyplot as plt


def draw_img(img, title, cmap=None):
    """Plot an image with title and cmap if wanted"""
    plt.figure()
    plt.imshow(img, cmap=cmap)
    plt.title(title)
    plt.draw()
    plt.pause(0.1)


# https://www.homeandlearn.co.uk/extras/image/image-invert-colors.html
def ft_invert(array) -> array:
    """Inverts the color of the image received"""
    new = array.copy()
    if len(array.shape) == 3:
        new[:, :, 0] = 255 - array[:, :, 0]
        new[:, :, 1] = 255 - array[:, :, 1]
        new[:, :, 2] = 255 - array[:, :, 2]
    draw_img(new, "Invert")
    return new


def ft_red(array) -> array:
    """Removes the green and blue channels from the image"""
    new = array.copy()
    if len(array.shape) == 3:
        new[:, :, 1] = 0
        new[:, :, 2] = 0
    draw_img(new, "Red")
    return new


def ft_green(array) -> array:
    """Removes the red and blue channels from the image"""
    new = array.copy()
    if len(array.shape) == 3:
        new[:, :, 0] = 0
        new[:, :, 2] = 0
    draw_img(new, "Green")
    return new


def ft_blue(array) -> array:
    """Removes the red and green channels from the image"""
    new = array.copy()
    if len(array.shape) == 3:
        new[:, :, 0] = 0
        new[:, :, 1] = 0
    draw_img(new, "Blue")
    return new


def ft_grey(array) -> array:
    """converts an image to grayscale
    img is a 3d array, the last dimension is the RGB channels
    returns a 2d array of the grayscale image"""
    if len(array.shape) == 3:
        new = array[:, :, 0] / 3.3456 + array[:, :, 1] / 1.7035775
        + array[:, :, 2] / 8.77192982456
    draw_img(new, "Grey", cmap="grey")
    return new
