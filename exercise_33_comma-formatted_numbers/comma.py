def comma_format(number: int | float) -> str:
    head, sep, end = str(number).partition(".")
    groups = [head[max(0, i - 2) : i + 1] for i in range(len(head) - 1, -1, -3)][::-1]
    return f"{','.join(groups)}{sep}{end}"


if __name__ == "__main__":
    assert comma_format(1) == "1"
    assert comma_format(10) == "10"
    assert comma_format(100) == "100"
    assert comma_format(1000) == "1,000"
    assert comma_format(10000) == "10,000"
    assert comma_format(100000) == "100,000"
    assert comma_format(1000000) == "1,000,000"
    assert comma_format(1234567890) == "1,234,567,890"
    assert comma_format(1000.123456) == "1,000.123456"
