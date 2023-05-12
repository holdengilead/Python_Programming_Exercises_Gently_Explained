def convert_str_to_int(string_num: str) -> int:
    return int(string_num)


if __name__ == "__main__":
    for i in range(-10000, 10000):
        assert convert_str_to_int(str(i)) == i
