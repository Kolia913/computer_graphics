from typing import Tuple
from matplotlib import pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from matplotlib.patches import Polygon, Rectangle
import numpy as np


def add_square_to_plot(ax: plt.Axes, square: np.ndarray, color: str = "blue") -> None:
    """Plot a square on the given Axes.

    Args:
        ax (plt.Axes): The matplotlib Axes object.
        square (np.ndarray): Array of shape (4, 2) representing the coordinates of the square.
        color (str, optional): Color of the square. Defaults to 'blue'.
    """

    start_point = square[3]  # bottom_left

    width = abs(square[3][0] - square[2][0])  # bottom_left[0] - bottom_right[0]
    height = abs(square[0][1] - square[3][1])  # top_left[1] - bottom_left[1]

    square_patch = Rectangle(start_point, width, height, color=color, fill=False, linewidth=2)
    ax.add_patch(square_patch)


def add_polygon_to_plot(ax: plt.Axes, polygon: np.ndarray, color: str = "purple") -> None:
    """Plot a polygon on the given Axes.

    Args:
        ax (plt.Axes): The matplotlib Axes object.
        polygon (np.ndarray): Array of shape (n, 2) representing the coordinates of the polygon.
        color (str, optional): Color of the polygon. Defaults to 'purple'.
    """

    polygon_patch = Polygon(polygon, edgecolor=color, fill=False)
    ax.add_patch(polygon_patch)


def generate_plot(size: int = 10) -> Tuple[Figure, Axes]:
    fig, ax = plt.subplots()
    ax.set_aspect("equal", adjustable="box")
    plt.xticks(np.arange(-1 * size, size + 1, 1))
    plt.yticks(np.arange(-1 * size, size + 1, 1))
    plt.grid(True)

    return fig, ax


def main() -> None:

    # Plotting

    plt.show()


if __name__ == "__main__":
    main()
