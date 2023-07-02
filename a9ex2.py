"""
Author: Oleh Karavskyi
Matr.Nr.: k12139895
Exercise: 2
"""

import re

def extract_matr_ids(text: str) -> list[int]:

    pattern = r"id=(\d{4,8}\b)|\b[kK]?(\d{8}\b)|id=(\d{4,8})\D"

    matches = re.findall(pattern, text)
    lst_int = [int(i) for m in matches for i in m if i]

    return lst_int