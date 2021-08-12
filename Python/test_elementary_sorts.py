from elementary_sorts import selection_sort, insertion_sort, time_algorithm

def test_selection_sort_characters():
    a = 'SORTEXAMPLE'
    assert selection_sort(list(a)) == list('AEELMOPRSTX')
    print(time_algorithm('Selection', list(a)))


def test_insertion_sort_characters():
    a = 'SORTEXAMPLE'
    assert insertion_sort(list(a)) == list('AEELMOPRSTX')
    print(time_algorithm('Insertion', list(a)))