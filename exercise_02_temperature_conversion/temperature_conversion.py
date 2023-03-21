def convert_to_fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32


def convert_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9


if __name__ == "__main__":
    assert convert_to_celsius(0) == -17.77777777777778
    assert convert_to_celsius(180) == 82.22222222222223
    assert convert_to_fahrenheit(0) == 32
    assert convert_to_fahrenheit(100) == 212
    assert convert_to_celsius(convert_to_fahrenheit(15)) == 15
    assert convert_to_celsius(convert_to_fahrenheit(42)) == 42
