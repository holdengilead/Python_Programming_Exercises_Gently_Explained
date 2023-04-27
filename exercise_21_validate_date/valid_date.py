MONTH_DAYS = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}


def is_leap_year(year: int) -> bool:
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0


def is_valid_date(year: int, month: int, day: int) -> bool:
    if not (year >= 0 and 1 <= month <= 12 and day > 0):
        return False
    if month == 2 and is_leap_year(year):
        return day <= 29
    return day <= MONTH_DAYS[month]


if __name__ == "__main__":
    assert is_valid_date(1999, 12, 31) == True
    assert is_valid_date(2000, 2, 29) == True
    assert is_valid_date(2001, 2, 29) == False
    assert is_valid_date(2029, 13, 1) == False
    assert is_valid_date(1000000, 1, 1) == True
    assert is_valid_date(2015, 4, 31) == False
    assert is_valid_date(1970, 5, 99) == False
    assert is_valid_date(1981, 0, 3) == False
    assert is_valid_date(1666, 4, 0) == False
    import datetime

    d = datetime.date(1970, 1, 1)
    oneDay = datetime.timedelta(days=1)
    for i in range(1000000):
        assert is_valid_date(d.year, d.month, d.day) == True
        d += oneDay
