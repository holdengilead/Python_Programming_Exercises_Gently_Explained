from random import randint


def roll_dice(number_of_dice: int) -> int:
    if not number_of_dice:
        return 0
    return sum(randint(1, 6) for _ in range(number_of_dice))


if __name__ == "__main__":
    assert roll_dice(0) == 0
    assert roll_dice(1000) != roll_dice(1000)
    for i in range(1000):
        assert 1 <= roll_dice(1) <= 6
        assert 2 <= roll_dice(2) <= 12
        assert 3 <= roll_dice(3) <= 18
        assert 100 <= roll_dice(100) <= 600
