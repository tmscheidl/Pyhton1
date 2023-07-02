"""
Author: Oleh Karavskyi
Matr.Nr.: k12139895
Exercise: 1
"""

import numpy as np

def  extend(arr: np.ndarray, size: int, fill=None) -> np.ndarray:

    if arr.ndim != 1:
        raise ValueError("Array is not 1D")

    if size < arr.size:
        raise ValueError("Size is smaller than the 1D array")

    if fill == None:
        extended_arr = np.empty(size)
        extended_arr[:len(arr)] = arr

    if fill == "mean" and np.issubdtype(arr.dtype, np.number):

        extended_arr = np.full(size, arr.mean(), dtype=arr.dtype)
        extended_arr[:len(arr)] = arr

    else:
        extended_arr = np.full(size, fill, dtype=object)
        extended_arr[:len(arr)] = arr

    return extended_arr