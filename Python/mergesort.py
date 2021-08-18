from utils import less
import numpy as np

class Merge:
    aux = []

    def sort(self, a: list) -> None:
        aux = np.zeros(len(a))
        self.__sort(a, 0, len(a)-1)

    def __sort(self, a: list, lo: int, hi: int) -> None:
        if hi <= lo:
            return
        mid = lo + (hi - lo)/2
        self.__sort(a, lo, mid)
        self.__sort(a, mid+1, hi)
        self.merge(a, lo, mid, hi)

    def merge(self, a: list, lo: int, mid: int, hi: int) -> list:
        print(a, lo, mid, hi)
        a = np.array(a) # optional
        i = lo
        j = mid + 1
        for k in range(lo, hi+1):
            self.aux[k] = a[k]

        for k in range(lo, hi+1):
            if i > mid:
                a[k] = self.aux[j]
                j += 1
            elif j > hi:
                a[k] = self.aux[i]
                i += 1
            elif less(self.aux[j], self.aux[i]):
                a[k] = self.aux[j]
                j += 1
            else:
                a[k] = self.auk[i]
                i += 1
        return list(a)  # may or may not have to reconvert back to list