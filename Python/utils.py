def compare_to(v, w) -> int:
    args = [v, w]
    for i, _ in enumerate(args):
        if type(args[i]) == str:
            args[i] = ord(args[i])
    if args[0] < args[1]:
        return -1
    elif args[0] == args[1]:
        return 0
    else:
        return 1


def less(v, w) -> bool:
    return compare_to(v, w) < 0


def is_sorted(a):
    for i in range (1, len(a)):
        if less(a[i], a[i-1]):
            return False
    return True


if __name__ == 'main':
    assert less(0, 0.111) is True
    assert is_sorted([1, 2, 3, 4, 5, 6, 7, 8]) is True
    assert is_sorted([1, 2, 3, 4, 5, 6, 8, 7]) is False
