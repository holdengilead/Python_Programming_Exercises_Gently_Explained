from collections import Counter


def mode(numbers: list[int]) -> int:
    if not numbers:
        return None
    freq = Counter(numbers)
    return freq.most_common(n=1)[0][0]


if __name__ == "__main__":
    assert mode([]) == None
    assert mode([1, 2, 3, 4, 4]) == 4
    assert mode([1, 1, 2, 3, 4]) == 1
    import random

    random.seed(42)
    testData = [1, 2, 3, 4, 4]
    for i in range(1000):
        random.shuffle(testData)
        assert mode(testData) == 4
