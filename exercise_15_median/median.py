def median(numbers: list[int]) -> int | float:
    if not numbers:
        return None
    idx_med = len(numbers) // 2
    numbers.sort()
    if len(numbers) % 2 != 0:
        return numbers[idx_med]
    return (numbers[idx_med] + numbers[idx_med - 1]) / 2


if __name__ == "__main__":
    assert median([]) == None
    assert median([1, 2, 3]) == 2
    assert median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]) == 5.5
    assert median([3, 7, 10, 4, 1, 9, 6, 2, 8]) == 6
    import random

    random.seed(42)
    testData = [3, 7, 10, 4, 1, 9, 6, 2, 8]
    for i in range(1000):
        random.shuffle(testData)
        assert median(testData) == 6
