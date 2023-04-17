def calculate_sum(numbers: list[int | float]) -> int | float:
    result = 0
    for number in numbers:
        result += number
    return result


def calculate_product(numbers: list[int | float]) -> int | float:
    result = 1
    for number in numbers:
        result *= number
    return result


if __name__ == "__main__":
    assert calculate_sum([]) == 0
    assert calculate_sum([2, 4, 6, 8, 10]) == 30
    assert calculate_product([]) == 1
    assert calculate_product([2, 4, 6, 8, 10]) == 3840
