import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.animation import FuncAnimation
from typing import List, Tuple


def plot_square(ax: plt.Axes, square: np.ndarray, color: str = "blue") -> None:
    """Plot a square on the given Axes.

    Args:
        ax (plt.Axes): The matplotlib Axes object.
        square (np.ndarray): Array of shape (4, 2) representing the coordinates of the square.
        color (str, optional): Color of the square. Defaults to 'blue'.
    """
    square_patch = Polygon(square, edgecolor=color, fill=False)
    ax.add_patch(square_patch)


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
    # Apply the transformation matrix
    transformed_square = np.dot(square_homogeneous, matrix.T)
    # Remove homogeneous coordinate
    transformed_square = transformed_square[:, :2]
    return transformed_square


def translate_square(square: np.ndarray, translation: np.ndarray) -> np.ndarray:
    """Translate a square.

    Args:
        square (np.ndarray): Array of shape (4, 2) representing the coordinates of the square.
        translation (np.ndarray): Translation vector.

    Returns:
        np.ndarray: Translated square coordinates.
    """
    translation_matrix = np.array([[1, 0, translation[0]], [0, 1, translation[1]], [0, 0, 1]])
    return affine_transform(square, translation_matrix)


def update(
    frame: int,
    square: np.ndarray,
    affine_matrix: np.ndarray,
    translation_vector: np.ndarray,
    square_plot: plt.Axes,
) -> List[plt.Artist]:
    """Update function for animation."""
    square_transformed = affine_transform(square, np.linalg.matrix_power(affine_matrix, frame))
    square_translated = translate_square(square_transformed, translation_vector)

    square_plot.clear()
    plot_square(square_plot, square, color="blue")  # Original square
    plot_square(square_plot, square_transformed, color="red")  # Transformed square
    plot_square(square_plot, square_translated, color="green")  # Translated square

    square_plot.set_aspect("equal", adjustable="box")
    square_plot.set_xlim(-5, 5)
    square_plot.set_ylim(-5, 5)
    square_plot.grid(True)
    square_plot.set_title("Affine Transformation and Translation of a Square")

    return [square_plot]


def main() -> None:
    # Input coordinates of the square
    square_coords = np.array([[0, 0], [1, 0], [1, 1], [0, 1]])

    # Affine transformation matrix (scaling example)
    scaling_factor = 2
    affine_matrix = np.array([[scaling_factor, 0, 0], [0, scaling_factor, 0], [0, 0, 1]])

    # Translate the square
    translation_vector = np.array([1, 2])

    # Plotting
    fig, square_plot = plt.subplots()
    plot_square(square_plot, square_coords, color="blue")  # Original square

    square_plot.set_aspect("equal", adjustable="box")
    square_plot.set_xlim(-5, 5)
    square_plot.set_ylim(-5, 5)
    square_plot.grid(True)
    square_plot.set_title("Affine Transformation and Translation of a Square")

    animation = FuncAnimation(
        fig,
        update,
        frames=30,
        interval=500,
        repeat=False,
        fargs=(square_coords, affine_matrix, translation_vector, square_plot),
    )

    animation.save("anim.gif")

    plt.show()


if __name__ == "__main__":
    main()
