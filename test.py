from timsort import insertion_sort, merge, get_run, timsort


def test_insertion_sort():
    source = [3, 1, 4, 5, 5, 2, 8, 6, 9, 7]

    assert insertion_sort(source.copy()) == sorted(source.copy())


def test_merge():
    a = [1, 2, 3, 4, 5]
    b = [1, 2, 3, 4, 6]

    assert merge(a, b) == [1, 1, 2, 2, 3, 3, 4, 4, 5, 6]


def test_merge_separated():
    a = [7, 8, 9, 11]
    b = [1, 2, 3, 4, 6]

    assert merge(a, b) == [1, 2, 3, 4, 6, 7, 8, 9, 11] == merge(b, a)


def test_get_run():
    source = [2, 7, 0, 1, 2, 3, 4, 5, 0, 5, 3]
    len_ = 5

    assert get_run(source, len_) == [2, 7, 0, 1, 2, 3, 4, 5]


def test_timsort():
    source = [3, 1, 4, 5, 5, 2, 8, 6, 9, 7]

    assert timsort(source.copy()) == sorted(source.copy())
