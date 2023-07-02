"""
Author: Oleh Karavskyi
Matr.Nr.: k12139895
Exercise: 2
"""

import numpy as np

def matrix_stats(matrix: np.ndarray) -> dict:

    if matrix.ndim != 2:
        raise ValueError("Matrix is not 2D")

    matrix_stat_result = {'total_sum': matrix.sum(), 'row_sums': matrix.sum(axis=1), 'column_sums': matrix.sum(axis=0)}

    return matrix_stat_result