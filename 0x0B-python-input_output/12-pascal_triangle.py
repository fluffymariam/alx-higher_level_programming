#!/usr/bin/python3
"""
Module containing the pascal_triangle function.
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the given number of rows.

    Args:
        n (int): The number of rows in Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]
        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)
        triangle.append(new_row)

    return triangle


if __name__ == "__main__":
    n = 5
    triangle = pascal_triangle(n)
    for row in triangle:
        print(row)
