#!/usr/bin/python3
"""Module lazy_matrix_mul
Matrix multiplication using NumPy.
"""
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    matrix_a = np.array(m_a)
    matrix_b = np.array(m_b)
    result = np.matmul(matrix_a, matrix_b)
    return result.tolist()
