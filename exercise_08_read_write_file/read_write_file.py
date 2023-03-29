def write_to_file(filename: str, text: str) -> None:
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(text)


def append_to_file(filename: str, text: str) -> None:
    with open(filename, mode="a", encoding="utf-8") as file:
        file.write(text)


def read_from_file(filename: str) -> str:
    with open(filename, encoding="utf-8") as file:
        return file.read()


if __name__ == "__main__":
    write_to_file("greet.txt", "Hello!\n")
    append_to_file("greet.txt", "Goodbye!\n")
    assert read_from_file("greet.txt") == "Hello!\nGoodbye!\n"
