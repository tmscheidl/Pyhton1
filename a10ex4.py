"""
Author: Oleh Karavskyi
Matr.Nr.: k12139895
Exercise: 4
"""

import numpy as np

def create_minefield(rows: int, cols: int, n_mines: int, seed=None) -> np.ndarray:

    if rows < 2:
        raise ValueError("Number of rows is smaller than 2")

    if cols < 2:
        raise ValueError("Number of columns is smaller than 2")

    if n_mines < 1 or n_mines >= rows * cols:
        raise ValueError("Number of mines is 0.\nMines must be placed on different cells, i.e., a single cell can only contain a single mine.")

    np.random.seed(seed)

    minefield = np.zeros((rows, cols), dtype=int)

    minefield.flat[np.random.choice((rows*cols), n_mines, replace=False)] = -1

    for row in range(rows):
        for col in range(cols):
            if minefield[row, col] == -1:
                for r in range(row - 1, row + 2):
                    for c in range(col - 1, col + 2):
                        if minefield[r, c] != -1 and r >= 0 and r < rows and c >= 0 and c < cols:
                            minefield[r, c] += 1

    return minefield