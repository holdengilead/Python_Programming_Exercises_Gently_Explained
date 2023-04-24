def get_cost_of_coffee(number_of_coffees: int, price_per_coffee: float) -> float:
    return (
        number_of_coffees * price_per_coffee - number_of_coffees // 9 * price_per_coffee
    )


if __name__ == "__main__":
    assert get_cost_of_coffee(7, 2.50) == 17.50
    assert get_cost_of_coffee(8, 2.50) == 20
    assert get_cost_of_coffee(9, 2.50) == 20
    assert get_cost_of_coffee(10, 2.50) == 22.50
    for i in range(1, 4):
        assert get_cost_of_coffee(0, i) == 0
        assert get_cost_of_coffee(8, i) == 8 * i
        assert get_cost_of_coffee(9, i) == 8 * i
        assert get_cost_of_coffee(18, i) == 16 * i
        assert get_cost_of_coffee(19, i) == 17 * i
        assert get_cost_of_coffee(30, i) == 27 * i
