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


# def cut_a_square(img):
#     """cut a square in the center of the image"""
#     if img.shape[0] < img.shape[1]:
#         size = img.shape[0] // 4
#     else:
#         size = img.shape[1] // 4
#     return img[img.shape[0] // 2 - size: img.shape[0] // 2 + size,
#                img.shape[1] // 2 - size: img.shape[1] // 2 + size]

def cut_a_square(img):
    """cut a square in the center of the image"""
    return img[125:125+400:, 450:450+400]


def ft_rotate_right(img):
    """rotate an image 90 degrees"""
    new_img = []
    for i in range(len(img)):
        for j in range(len(img[i])):
            if i == 0:
                new_img.append([])
            new_img[j].insert(0, img[i][j])
    return new_img


def ft_rotate_left(img):
    """rotate an image -90 degrees"""
    new_img = []
    for i in range(len(img)):
        for j in range(len(img[i])):
            if i == 0:
                new_img.append([])
            new_img[j].append(img[i][j])
    return new_img


def draw_img(img, title, cmap=None):
    """Plot an image with title and cmap if wanted"""
    plt.figure()
    plt.imshow(img, cmap=cmap)
    plt.title(title)
    plt.draw()
    plt.pause(0.5)


def main():
    """main function to load an image then square in"""
    try:
        if len(argv) < 2:
            file = "/mnt/nfs/homes/thi-le/Tham_42/animal.jpeg"
        else:
            file = argv[1]
        img = ft_load(file)

        draw_img(img, "Original image")
        square = cut_a_square(img)
        draw_img(square, "Square image")
        grey = rgb_to_gray(square)
        draw_img(grey, "Grayscale image", cmap="gray")

        rotate_right = ft_rotate_right(grey)
        draw_img(rotate_right, "Rotated image: right", cmap="gray")

        rotate_left = ft_rotate_left(grey)
        draw_img(rotate_left, "Rotated image: left", cmap="gray")
        plt.show()
    except FileNotFoundError:
        print("An error occured: file not found")
    except Exception as e:
        print("An error occured:", e)


if __name__ == "__main__":
    main()
