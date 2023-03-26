SUFFIXES = {1: "st", 2: "nd", 3: "rd"}


def ordinal_suffix(number: int) -> str:
    suffix = "th"
    if number % 10 in {1, 2, 3} and number % 100 not in {11, 12, 13}:
        suffix = SUFFIXES[number % 10]
    return f"{number}{suffix}"


if __name__ == "__main__":
    assert ordinal_suffix(0) == "0th"
    assert ordinal_suffix(1) == "1st"
    assert ordinal_suffix(2) == "2nd"
    assert ordinal_suffix(3) == "3rd"
    assert ordinal_suffix(4) == "4th"
    assert ordinal_suffix(10) == "10th"
    assert ordinal_suffix(11) == "11th"
    assert ordinal_suffix(12) == "12th"
    assert ordinal_suffix(13) == "13th"
    assert ordinal_suffix(14) == "14th"
    assert ordinal_suffix(101) == "101st"
