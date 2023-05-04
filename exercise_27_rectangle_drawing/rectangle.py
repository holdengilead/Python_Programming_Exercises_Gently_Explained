def draw_rectangle(width: int, height: int) -> None:
    if not width or not height:
        return
    print("\n".join("#" * width for _ in range(height)))


if __name__ == "__main__":
    draw_rectangle(40, 20)
