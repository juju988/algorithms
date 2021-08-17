from utils import less, exch
import cProfile
import time


def selection_sort(a: list) -> list:
    n = len(a)
    for i, _ in enumerate(a):
        mn = i
        for j in range(i+1, n):
            if less(a[j], a[mn]):
                mn = j
        exch(a, i, mn)
    print(a)
    return a


def insertion_sort(a: list) -> list:
    n = len(a)
    for i in range(1, n):
        j = i
        while j > 0 and less(a[j], a[j-1]):
            exch(a, j, j-1)
            j -= 1
    return a


if __name__ == 'main':
    a = 'SORTEXAMPLE'
    assert selection_sort(list(a)) == list('AEELMOPRSTX')
    cProfile.runctx('selection_sort(a)', {'a': list(a), 'selection_sort': selection_sort}, {})
    print(time_algorithm('Selection', list(a)))

    assert insertion_sort(list(a)) == list('AEELMOPRSTX')
    cProfile.runctx('insertion_sort(a)', {'a': list(a), 'insertion_sort': insertion_sort}, {})
    print(time_algorithm('Insertion', list(a)))

    with open('ishmael.txt', 'r', encoding='utf-8') as f:
        line = f.readline()
        print(time_algorithm('Selection', list(line)))
        print(time_algorithm('Insertion', list(line)))
