def get_smallest(numbers: list[int] | None) -> int | None:
    if not numbers:
        return None
    smallest = numbers[0]
    for number in numbers[1:]:
        if number < smallest:
            smallest = number
    return smallest


def get_biggest(numbers: list[int] | None) -> int | None:
    if not numbers:
        return None
    smallest = numbers[0]
    for number in numbers[1:]:
        if number > smallest:
            smallest = number
    return smallest


if __name__ == "__main__":
    assert get_smallest([1, 2, 3]) == 1
    assert get_smallest([3, 2, 1]) == 1
    assert get_smallest([28, 25, 42, 2, 28]) == 2
    assert get_smallest([1]) == 1
    assert get_smallest([]) == None
    assert get_biggest([1, 2, 3]) == 3
    assert get_biggest([3, 2, 1]) == 3
    assert get_biggest([28, 25, 42, 2, 28]) == 42
    assert get_biggest([1]) == 1
    assert get_biggest([]) == None
