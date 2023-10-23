import numpy as np
import matplotlib.pyplot as plt
from numba import jit


@jit(nopython=True)
def generate_julia(
    c_real: float, c_imag: float, re: float, im: float, max_iterations: int
) -> int:
    """
    Generate a Julia set for a given complex coordinate and Julia constant.

    :param c_real: The real part of the Julia constant.
    :param c_imag: The imaginary part of the Julia constant.
    :param re: The real part of the complex coordinate.
    :param im: The imaginary part of the complex coordinate.
    :param max_iterations: The maximum number of iterations to perform.
    :return: The number of iterations required for the sequence to escape the Julia set.
    """

    z = complex(re, im)

    for i in range(max_iterations):
        z = z * z + complex(c_real, c_imag)

        if (z.real * z.real + z.imag * z.imag) >= 4:
            return i

    return max_iterations


def generate_julia_set(
    c_real: float, c_imag: float, zoom_percentage: float, max_iterations: int
) -> np.array:
    """
    Generate a Julia set with the given Julia constant, zoom percentage, and max iterations.

    :param c_real: The real part of the Julia constant.
    :param c_imag: The imaginary part of the Julia constant.
    :param zoom_percentage: The zoom percentage (0 - default image scale, 1 - 100% zoom).
    :param max_iterations: The maximum number of iterations to perform.
    :return: A numpy array representing the Julia set.
    """
    rows, cols = 2000, 2000
    zoom = 1 + zoom_percentage

    re_range = [-2 / zoom, 2 / zoom]
    im_range = [-2 / zoom, 2 / zoom]

    re_linspace = np.linspace(re_range[0], re_range[1], num=cols)
    im_linspace = np.linspace(im_range[0], im_range[1], num=rows)

    result = np.zeros([rows, cols])

    for row_index, re in enumerate(re_linspace):  # real axis
        for col_index, im in enumerate(im_linspace):  # imaginary axis
            result[row_index, col_index] = generate_julia(
                c_real, c_imag, re, im, max_iterations
            )

    return result


def __main():
    """Generate a Julia set visualization based on a passed constant."""
    julia_set = generate_julia_set(-0.7, 0.4, 0.5, 100)
    plt.figure(dpi=100)
    plt.imshow(
        julia_set.T,
        cmap="hot",
        interpolation="nearest",
        extent=[-2, 2, -2, 2],
    )
    # hide axis
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    __main()
