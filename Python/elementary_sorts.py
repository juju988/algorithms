from utils import less, exch


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


if __name__ == 'main':
    a = 'SORTEXAMPLE'
    assert selection_sort(list(a)) == list('AEELMOPRSTX')
