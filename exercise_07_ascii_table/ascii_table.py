def print_ascii_table() -> None:
    print("\n".join(f"{i} {chr(i)}" for i in range(32, 127)))


if __name__ == "__main__":
    print_ascii_table()
