def collatz(starting_number: int) -> list[int]:
    if starting_number < 1:
        return []
    seq = [starting_number]
    while starting_number > 1:
        if starting_number % 2 == 0:
            starting_number //= 2
        else:
            starting_number = starting_number * 3 + 1
        seq.append(starting_number)
    return seq


if __name__ == "__main__":
    assert collatz(0) == []
    assert collatz(10) == [10, 5, 16, 8, 4, 2, 1]
    assert collatz(11) == [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    assert collatz(12) == [12, 6, 3, 10, 5, 16, 8, 4, 2, 1]
    assert len(collatz(256)) == 9
    assert len(collatz(257)) == 123

    import random

    random.seed(42)
    for i in range(1000):
        starting_num = random.randint(1, 10000)
        seq = collatz(starting_num)
        assert seq[0] == starting_num
        assert seq[-1] == 1
