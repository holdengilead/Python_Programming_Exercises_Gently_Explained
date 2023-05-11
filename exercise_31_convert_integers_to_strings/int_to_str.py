def convert_int_to_str(integer_num: int) -> str:
    return str(integer_num)


if __name__ == "__main__":
    for i in range(-10000, 10000):
        assert convert_int_to_str(i) == str(i)
