def draw_border(width: int, height: int) -> None:
    if width < 2 or height < 2:
        return
    for i in range(1, height + 1):
        extremes = "+" if i in (1, height) else "|"
        medium = "-" if i in (1, height) else " "
        print(f"{extremes}{medium * (width - 2)}{extremes}")


if __name__ == "__main__":
    draw_border(46, 15)
