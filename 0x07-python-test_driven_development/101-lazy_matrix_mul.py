#!/usr/bin/python3
"""
This module provides a function to multiply two matrices
    Raises:
        ValueError: If the matrices cannot be multiplied.
"""


import numpy as np


def lazy_matrix_mul(matrix_a, matrix_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        matrix_a (list of lists): First matrix.
        matrix_b (list of lists): Second matrix.

    Returns:
        list of lists: The resulting matrix of the multiplication.

    Raises:
        ValueError: If the matrices cannot be multiplied.
    """
    try:
        result = np.dot(matrix_a, matrix_b)
        return result.tolist()
    except ValueError:
        raise ValueError("Incompatible matrices for multiplication")

# Sample test cases


if __name__ == "__main__":
    print(lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
    print(lazy_matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
