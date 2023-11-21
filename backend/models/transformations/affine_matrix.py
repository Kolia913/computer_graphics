import numpy as np


class AffineMatrix:
    @staticmethod
    def get_translation_matrix(translation: np.ndarray, dimension: int) -> np.ndarray:

        matrix = np.identity(dimension + 1)
        matrix[:-1, -1] = translation
        return matrix

    @staticmethod
    def get_scale_matrix(scale: np.ndarray, dimension: int) -> np.ndarray:
        """Return a scale matrix.

        Args:
            scale (np.ndarray): Scale vector. (a, d)
            dimension (int): Dimension of the matrix.
        """

        matrix = np.identity(dimension + 1)

        # set diagonal to 1
        matrix = np.diag(np.ones(dimension + 1))

        # set scale
        matrix[0][0] = scale[0]
        matrix[1][1] = scale[1]

        return matrix

    @staticmethod
    def get_rotation_matrix(alpha: float, dimension: int) -> np.ndarray:
        """Return a rotation matrix."""

        matrix = np.identity(dimension + 1)

        # set diagonal to 1
        matrix = np.diag(np.ones(dimension + 1))

        # rotation_matrix = np.array([[np.cos(alpha), np.sin(alpha)], [-np.sin(alpha), np.cos(alpha)]])
        matrix[0][0] = np.cos(alpha)
        matrix[0][1] = np.sin(alpha)
        matrix[1][0] = -np.sin(alpha)
        matrix[1][1] = np.cos(alpha)
        return matrix
