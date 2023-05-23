def reverse_string(text: str) -> str:
    return "".join(text[::-1])


if __name__ == "__main__":
    assert reverse_string("Hello") == "olleH"
    assert reverse_string("") == ""
    assert reverse_string("aaazzz") == "zzzaaa"
    assert reverse_string("xxxx") == "xxxx"
