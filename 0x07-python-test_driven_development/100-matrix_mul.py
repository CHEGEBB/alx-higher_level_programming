#!/usr/bin/python3
"""Module for matrix_mul method."""

def matrix_mul(m_a, m_b):
    """Function that multiplies 2 matrices.

    Args:
        m_a (list): The first matrix.
        m_b (list): The second matrix.

    Raises:
        TypeError: If m_a or m_b are not lists.
        TypeError: If m_a or m_b are not lists of lists.
        ValueError: If m_a or m_b are empty lists/matrices.
        TypeError: If m_a or m_b contain a non int/float.
        TypeError: If m_a or m_b are not rectangular.

    Returns:
        list: The result of the multiplication.
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")

    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        if type(row) is not list:
            raise TypeError("m_a must be a list of lists")

    for row in m_b:
        if type(row) is not list:
            raise TypeError("m_b must be a list of lists")

    if len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")

    if len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for num in row:
            if type(num) is not int and type(num) is not float:
                raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        for num in row:
            if type(num) is not int and type(num) is not float:
                raise TypeError("m_b should contain only integers or floats")

    for row in m_a:
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")

    for row in m_b:
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for col in range(len(m_b[0]))] for row in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]
    return result
