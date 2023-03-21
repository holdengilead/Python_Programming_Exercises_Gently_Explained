def is_odd(number: int) -> bool:
    return isinstance(number, int) and number % 2 != 0


def is_even(number: int) -> bool:
    return isinstance(number, int) and number % 2 == 0


if __name__ == "__main__":
    assert is_odd(42) == False
    assert is_odd(9999) == True
    assert is_odd(-10) == False
    assert is_odd(-11) == True
    assert is_odd(3.1415) == False
    assert is_even(42) == True
    assert is_even(9999) == False
    assert is_even(-10) == True
    assert is_even(-11) == False
    assert is_even(3.1415) == False
