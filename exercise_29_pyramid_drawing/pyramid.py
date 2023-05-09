def draw_pyramid(height: int) -> None:
    for i in range(height):
        print(f'{" " * (height - 1 - i)}{"*" * (i * 2 + 1)}')


if __name__ == "__main__":
    draw_pyramid(51)
