def area(length: int, width: int) -> int:
    return length * width


def perimeter(length: int, width: int) -> int:
    return 2 * length + 2 * width


def volume(length: int, width: int, height: int) -> int:
    return length * width * height


def surface_area(length: int, width: int, height: int) -> int:
    return 2 * ((length * width) + (length * height) + (width * height))


if __name__ == "__main__":
    assert area(10, 10) == 100
    assert area(0, 9999) == 0
    assert area(5, 8) == 40
    assert perimeter(10, 10) == 40
    assert perimeter(0, 9999) == 19998
    assert perimeter(5, 8) == 26
    assert volume(10, 10, 10) == 1000
    assert volume(9999, 0, 9999) == 0
    assert volume(5, 8, 10) == 400
    assert surface_area(10, 10, 10) == 600
    assert surface_area(9999, 0, 9999) == 199960002
    assert surface_area(5, 8, 10) == 340
