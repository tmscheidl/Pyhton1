"""
Author: Oleh Karavskyi
Matr.Nr.: k12139895
Exercise: 4
"""

import random
import argparse
from multiprocessing import Pool


def get_quarter_circle_hits(n: int) -> int:
    n_hits = 0

    for t in range(n):
        if (random.random()**2 + random.random()**2) < 1:
            n_hits += 1

    return n_hits


parser = argparse.ArgumentParser()
parser.add_argument("-p", "--processes", type=int, default=1, help="<p> is the number of process")
parser.add_argument("-n", "--n", type=int, default=1000, help="<n> the number of quarter circle hit checks per process")

args = parser.parse_args()

p_p = args.processes
p_n = args.n
p_tn = p_p*[p_n]

if __name__ == "__main__":
    with Pool(p_p) as p:
        n_hits = sum(p.map(get_quarter_circle_hits, p_tn))
    print(f"{p_p} processes with {p_n} checks each\ntotal tries: {p_p*p_n}\ntotal hits: {n_hits}\npi approximation: {4*n_hits/(p_p*p_n)}")