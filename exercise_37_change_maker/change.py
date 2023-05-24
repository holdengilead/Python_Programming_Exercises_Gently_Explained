COINS = {"quarters": 25, "dimes": 10, "nickels": 5, "pennies": 1}


def make_change(amount: int) -> dict[str, int]:
    total_change = {}
    for coin, value in COINS.items():
        if change := amount // value:
            total_change[coin] = change
            amount %= value
    return total_change


if __name__ == "__main__":
    assert make_change(30) == {"quarters": 1, "nickels": 1}
    assert make_change(10) == {"dimes": 1}
    assert make_change(57) == {"quarters": 2, "nickels": 1, "pennies": 2}
    assert make_change(100) == {"quarters": 4}
    assert make_change(125) == {"quarters": 5}
