from utils import less
import numpy as np

def merge(a: list, lo: int, mid: int, hi: int) -> list:
    a = np.array(a) # optional
    i = lo
    j = mid + 1
    for k in range(lo, hi+1):
        aux[k] = a[k]

    for k in range(lo, hi+1):
        if i > mid:
            a[k] = aux[j++]
        elif j > hi:
            a[k] = aux[i++]
        elif (less(aux[j], aux[i])):
            a[k] = aux[j++]
        else:
            a[k] = auk[i++]
    return list(a)  # may or may not have to reconvert back to list