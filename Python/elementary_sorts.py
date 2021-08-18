from utils import less, exch
import cProfile
import time


def time_algorithm(alg: str, a: list) -> float:
    timer = time.time()
    insertion_sort(a) if alg == "Insertion" else False
    selection_sort(a) if alg == "Selection" else False
    shell_sort(a) if alg == "Shell" else False
    return time.time() - timer


def selection_sort(a: list) -> list:
    n = len(a)
    for i, _ in enumerate(a):
        mn = i
        for j in range(i+1, n):
            if less(a[j], a[mn]):
                mn = j
        exch(a, i, mn)
    return a


def insertion_sort(a: list) -> list:
    n = len(a)
    for i in range(1, n):
        j = i
        while j > 0 and less(a[j], a[j-1]):
            exch(a, j, j-1)
            j -= 1
    return a


def shell_sort(a: list) -> list:
    """
    This is loads quicker than insertion and selection sort
    :param a list:
    :return sorted list:
    """
    n = len(a)
    h = 1
    while (h < n/3):
        h = (3 * h) + 1
    while h >= 1:
        for i in range(int(h), n):
            j = int(i)
            h = int(h)
            while j >= h and less(a[j], a[j-h]):
                exch(a, j, j-h)
                j -= h
        h = h/3
    return a


if __name__ == '__main__':
    a = 'SORTEXAMPLE'
    assert selection_sort(list(a)) == list('AEELMOPRSTX')
    cProfile.runctx('selection_sort(a)', {'a': list(a), 'selection_sort': selection_sort}, {})
    print(time_algorithm('Selection', list(a)))

    assert insertion_sort(list(a)) == list('AEELMOPRSTX')
    cProfile.runctx('insertion_sort(a)', {'a': list(a), 'insertion_sort': insertion_sort}, {})
    print(time_algorithm('Insertion', list(a)))

    a = 'SHELLSORTEXAMPLE'
    assert shell_sort(list(a)) == list('AEEEHLLLMOPRSSTX')
    cProfile.runctx('shell_sort(a)', {'a': list(a), 'shell_sort': selection_sort}, {})
    print(time_algorithm('Shell', list(a)))

    with open('ishmael.txt', 'r', encoding='utf-8') as f:
        line = f.readline()
        print(f"Selection sort time: {time_algorithm('Selection', list(line))}")
        print(f"Insertion sort time: {time_algorithm('Insertion', list(line))}")
        print(f"Shell sort time: {time_algorithm('Shell', list(line))}")

        print('still running - on last test')

        sorted_selection = selection_sort(list(line))
        sorted_insertion = insertion_sort(list(line))
        sorted_shell = shell_sort(list(line))
        assert sorted_selection == sorted_insertion
        assert sorted_insertion == sorted_shell
