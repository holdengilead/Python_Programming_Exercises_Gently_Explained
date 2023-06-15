from merging import merge_two_lists


def test_second_bigger() -> None:
    l1 = [1, 3, 6]
    l2 = [5, 7, 8, 9]
    assert merge_two_lists(l1, l2) == [1, 3, 5, 6, 7, 8, 9]


def test_first_bigger() -> None:
    l1 = [1, 2, 3]
    l2 = [4, 5]
    assert merge_two_lists(l1, l2) == [1, 2, 3, 4, 5]


def test_same_lists() -> None:
    l1 = [2, 2, 2]
    l2 = [2, 2, 2]
    assert merge_two_lists(l1, l2) == [2, 2, 2, 2, 2, 2]


def test_second_list_empty() -> None:
    l1 = [1, 2, 3]
    l2: list[int] = []
    assert merge_two_lists(l1, l2) == [1, 2, 3]


def test_first_list_empty() -> None:
    l1: list[int] = []
    l2 = [1, 2, 3]
    assert merge_two_lists(l1, l2) == [1, 2, 3]


def test_both_empty() -> None:
    l1: list[int] = []
    l2: list[int] = []
    assert merge_two_lists(l1, l2) == []
