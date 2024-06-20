import array
from matplotlib import image as mpimg


def ft_load(path: str) -> array:
    """loads an image,
    prints its format, and its pixels content in RGB format"""
    try:
        img = mpimg.imread(path)
        print(f"The shape of image is ({img.shape[0]}, {img.shape[1]},\
{img.shape[2]})")
        return img
    except FileNotFoundError:
        print("An error occured: file not found")
        return None
    except Exception as e:
        print(f"An error occured: {e}")
        return None
