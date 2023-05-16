def get_uppercase(text: str) -> str:
    return text.upper()


if __name__ == "__main__":
    assert get_uppercase("Hello") == "HELLO"
    assert get_uppercase("hello") == "HELLO"
    assert get_uppercase("HELLO") == "HELLO"
    assert get_uppercase("Hello, world!") == "HELLO, WORLD!"
    assert get_uppercase("goodbye 123!") == "GOODBYE 123!"
    assert get_uppercase("12345") == "12345"
    assert get_uppercase("") == ""
