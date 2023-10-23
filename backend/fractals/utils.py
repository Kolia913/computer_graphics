from matplotlib.transforms import Bbox
import numpy as np
import io
import matplotlib.pyplot as plt


def convert_set_to_image(
    set_array: np.array, color_map: str = "hot", interpolation: str = "bilinear"
) -> io.BytesIO:
    """
    Convert a passed set to an image.

    :param set_array: A numpy array representing the set.
    :param color_map: A string representing the color map to be used for the image.
    :param interpolation: A string representing the interpolation to be used for the image.
    :return: A BytesIO object containing the image data.
    """

    plt.figure(dpi=100)
    plt.imshow(
        set_array.T,
        cmap=color_map,
        interpolation=interpolation,
        extent=[-2, 1, -1, 1],
    )
    # hide axis
    plt.axis("off")

    img_byte_array = io.BytesIO()
    plt.savefig(img_byte_array, format="png", bbox_inches="tight", pad_inches=0)
    img_byte_array.seek(0)
    return img_byte_array


def convert_figure_to_image(figure: plt.figure):
    """
    Convert a passed figure to an image.

    :param figure: A matplotlib figure.
    :return: A BytesIO object containing the image data.
    """

    img_byte_array = io.BytesIO()
    figure.savefig(
        img_byte_array,
        format="png",
        pad_inches=0.2,
        bbox_inches="tight",
    )
    img_byte_array.seek(0)
    return img_byte_array
