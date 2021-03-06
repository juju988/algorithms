import sys
from elementary_sorts import insertion_sort, selection_sort, shell_sort
import time
import numpy as np

"""
    p256 of Algorithms book
"""


def time_algorithm(alg: str, a: list) -> float:
    timer = time.time()
    insertion_sort(a) if alg == "Insertion" else False
    selection_sort(a) if alg == "Selection" else False
    shell_sort(a) if alg == "Shell" else False
    return time.time() - timer


def timeRandomInput(alg: str, N: int, T: int) -> float:
    """
    Creates an array of length N. Then for T times populates
    that with random numbers and sends it off to alg for sorting.
    :param alg:
    :param N:
    :param T:
    :return: float
    """
    total = 0.0
    a = np.zeros(N)
    for t in range(0, T):
        for i in range(0, N):
            a[i] = np.random.uniform()
        total += time_algorithm(alg, a)
    return total


def main(args):
    alg1 = args[1]
    alg2 = args[2]
    N = int(args[3])
    T = int(args[4])
    t1 = timeRandomInput(alg1, N, T)    # total for alg1
    print(f'{alg1} time: {t1}')
    t2 = timeRandomInput(alg2, N, T)    # total for alg2
    print(f'{alg2} time: {t2}')
    print(f'for {N} random floats\n {alg2} is')
    print(f'{t1/t2}\n times faster than {alg1}')


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Not enough arguments supplied - 2 different algorithms and 2 integers required")
        print("e.g. sort_compare Insertion Selection 1000 100")
        print("Generally put the fastest alg second")
        exit(1)
    else:
        print(sys.argv[1:4])
        main(sys.argv)
