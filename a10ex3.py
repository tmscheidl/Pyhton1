"""
Author: Oleh Karavskyi
Matr.Nr.: k12139895
Exercise: 3
"""

import numpy as np

def create_data(setups: list[dict], seed=None) -> dict:

    if seed != None:
        np.random.seed(seed)

    data_list = {}

    for setup in setups:

        p_id = setup["id"]
        p_n = setup["n"]
        p_a = setup["a"]
        p_b = setup["b"]

        data_list[p_id] = np.random.uniform(p_a, p_b, size=p_n)

    return data_list