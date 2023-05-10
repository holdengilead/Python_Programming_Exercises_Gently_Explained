def draw_box(size: int):
    if size < 1:
        return
    print(f"{' ' * (size + 1)}+{'-' * (size * 2)}+")
    for i in range(size):
        print(f"{' ' * (size - i)}/{' ' * (size * 2)}/{' ' * i}|")
    print(f"+{'-' * (size * 2)}+{' ' * size}+")
    for i in range(size):
        print(f"|{' ' * (size * 2)}|{' ' * (size - 1 - i)}/")
    print(f"+{'-' * (size * 2)}+")


if __name__ == "__main__":
    for i in range(10):
        draw_box(i)
