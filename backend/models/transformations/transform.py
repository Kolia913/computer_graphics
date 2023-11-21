import io
from matplotlib import animation, pyplot as plt
import numpy as np

from .affine_matrix import AffineMatrix
from .plotting import add_polygon_to_plot, add_square_to_plot, generate_plot


def is_square(diagonal_coord1: tuple, diagonal_coord2: tuple) -> bool:
    x1, y1 = diagonal_coord1
    x2, y2 = diagonal_coord2

    # Check if the difference in x and y coordinates is the same
    return abs(x2 - x1) == abs(y2 - y1)


def generate_square(diagonal_coord1: tuple, diagonal_coord2: tuple) -> np.array:
    x1, y1 = diagonal_coord1
    x2, y2 = diagonal_coord2

    # Calculate the coordinates of the four corners of the square without rounding
    top_left = (min(x1, x2), max(y1, y2))
    top_right = (max(x1, x2), max(y1, y2))
    bottom_left = (min(x1, x2), min(y1, y2))
    bottom_right = (max(x1, x2), min(y1, y2))

    return np.array((top_left, top_right, bottom_right, bottom_left))


def affine_transform(square: np.ndarray, matrix: np.ndarray) -> np.ndarray:
    """Apply an affine transformation to a square.

    Args:
        square (np.ndarray): Array of shape (4, 2) representing the coordinates of the square.
        matrix (np.ndarray): Affine transformation matrix.

    Returns:
        np.ndarray: Transformed square coordinates.
    """

    # Add homogeneous coordinates to the square
    square_homogeneous = np.hstack((square, np.ones((square.shape[0], 1))))
    transformed_square = np.dot(square_homogeneous, matrix.T)

    # Remove homogeneous coordinate
    transformed_square = transformed_square[:, :2]
    return transformed_square


def transform_square(diagonal: tuple, translation: tuple, scaling: tuple, rotation: float) -> io.BytesIO:

    if not is_square(*diagonal):
        return io.BytesIO()

    fig, plot_ax = generate_plot()

    square_matrix = generate_square(*diagonal)
    square_dim = square_matrix.shape[1]

    add_square_to_plot(plot_ax, square_matrix, color="blue")  # Original square

    # Translation
    if any(translation):
        translated_square = affine_transform(
            square_matrix, AffineMatrix.get_translation_matrix(np.array(translation), square_dim)
        )
        add_square_to_plot(plot_ax, translated_square, color="red")
    else:
        translated_square = square_matrix

    # Scaling
    if any(scaling):
        scaled_square = affine_transform(
            translated_square, AffineMatrix.get_scale_matrix(np.array(scaling), square_dim)
        )
        add_square_to_plot(plot_ax, scaled_square, color="green")
    else:
        scaled_square = translated_square

    # Rotation
    rotated_square = affine_transform(scaled_square, AffineMatrix.get_rotation_matrix(rotation, square_dim))
    add_polygon_to_plot(plot_ax, rotated_square, color="purple")

    img_byte_array = io.BytesIO()
    plt.savefig(img_byte_array, format="png", bbox_inches="tight", pad_inches=0)
    img_byte_array.seek(0)

    return img_byte_array


# def animate_square(frame: int, diagonal: tuple, translation: tuple, scaling: float, rotation: float, plot_ax: Axes):

#     square_matrix = generate_square(*diagonal)

#     # plot_ax.clear()
#     # add_square_to_plot(plot_ax, square_matrix, color='blue')  # Original square

#     # Translation
#     translated_square = affine_transform(square_matrix, AffineMatrix.get_translation_matrix(np.array(translation), square_matrix.shape[1]))
#     add_square_to_plot(plot_ax, translated_square, color='red')  # Translated square

#     return [plot_ax]


def main() -> None:
    diagonal = ((0, 0), (5, 5))
    translation = (0, 0)
    scaling = (0, 0)
    rotation = 0

    transform_square(diagonal, translation, scaling, rotation)


if __name__ == "__main__":
    main()
