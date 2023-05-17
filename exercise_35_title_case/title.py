def get_title_case(text: str) -> str:
    return text.title()


if __name__ == "__main__":
    assert get_title_case("Hello, world!") == "Hello, World!"
    assert get_title_case("HELLO") == "Hello"
    assert get_title_case("hello") == "Hello"
    assert get_title_case("hElLo") == "Hello"
    assert get_title_case("") == ""
    assert get_title_case("abc123xyz") == "Abc123Xyz"
    assert get_title_case("cat dog RAT") == "Cat Dog Rat"
    assert get_title_case("cat,dog,RAT") == "Cat,Dog,Rat"
    import random

    random.seed(42)
    chars = list("abcdefghijklmnopqrstuvwxyz1234567890 ,.")
    for i in range(1000):
        random.shuffle(chars)
        assert get_title_case("".join(chars)) == "".join(chars).title()
