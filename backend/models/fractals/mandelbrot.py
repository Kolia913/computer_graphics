import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from numba import jit


matplotlib.use("agg")


@jit(nopython=True)
def generate_mandelbrot(re: float, im: float, max_iterations: int) -> int:
    """
    Generate a Mandelbrot fractal for a given complex coordinate.

    :param re: The real part of the complex coordinate.
    :param im: The imaginary part of the complex coordinate.
    :param max_iterations: The maximum number of iterations to perform.
    :return: The number of iterations required for the sequence to escape the Mandelbrot set.
    """

    c = complex(re, im)
    z = 0.0j

    for i in range(max_iterations):
        z = z * z + c

        if (z.real * z.real + z.imag * z.imag) >= 4:
            return i

    return max_iterations


def generate_mandelbrot_set(zoom_percentage: float, max_iterations: int) -> np.array:
    """
    Generate a mandelbrot set with the given zoom percentage and max iterations.

    :param zoom_percentage: The zoom percentage (0 - default image scale, 1 - 100% zoom).
    :param max_iterations: The maximum number of iterations to perform.
    :return: A numpy array representing the mandelbrot set.
    """

    rows, cols = 2000, 2000
    zoom = 1 + zoom_percentage

    re_range = [-2 / zoom, 1 / zoom]
    im_range = [-1 / zoom, 1 / zoom]

    re_linspace = np.linspace(re_range[0], re_range[1], num=cols)
    im_linpace = np.linspace(im_range[0], im_range[1], num=rows)

    result = np.zeros([rows, cols])

    for row_index, re in enumerate(re_linspace):  # real axis
        for col_index, im in enumerate(im_linpace):  # imaginary axis
            result[row_index, col_index] = generate_mandelbrot(re, im, max_iterations)

    return result


def __main():
    cols = 2000
    rows = 2000

    zoom_percentage = 0
    zoom = 1 + zoom_percentage

    re_range = [-2 / zoom, 1 / zoom]
    im_range = [-1 / zoom, 1 / zoom]

    re_linspace = np.linspace(re_range[0], re_range[1], num=cols)
    im_linpace = np.linspace(im_range[0], im_range[1], num=rows)

    result = np.zeros([rows, cols])

    for row_index, re in enumerate(re_linspace):  # real axis
        for col_index, im in enumerate(im_linpace):  # imaginary axis
            result[row_index, col_index] = generate_mandelbrot(re, im, 100)

    # for row_index, re in enumerate(np.linspace(-2, 1, num=rows)):  # real axis
    #     for col_index, im in enumerate(np.linspace(-1, 1, num=cols)):  # imaginary axis
    #         result[row_index, col_index] = generate_mandelbrot(re, im, cols, rows, 100)

    plt.figure(dpi=100)
    plt.imshow(result.T, cmap="hot", interpolation="bilinear", extent=[-2, 1, -1, 1])
    plt.xlabel("Re")
    plt.ylabel("Im")
    plt.show()


if __name__ == "__main__":
    __main()
