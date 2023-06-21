from bubble import bubble_sort


def test_sort():
    assert bubble_sort([2, 0, 4, 1, 3]) == [0, 1, 2, 3, 4]


def test_all_items_equal():
    assert bubble_sort([2, 2, 2, 2]) == [2, 2, 2, 2]


def test_one_item():
    assert bubble_sort([1]) == [1]


def test_empty():
    assert not bubble_sort([])
