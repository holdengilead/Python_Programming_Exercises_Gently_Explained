def get_chess_square_color(column: int, row: int) -> str:
    column, row = column - 1, row - 1
    if not (0 <= column <= 7 and 0 <= row <= 7):
        return ""
    if row % 2 == column % 2:
        return "white"
    return "black"


if __name__ == "__main__":
    assert get_chess_square_color(1, 1) == "white"
    assert get_chess_square_color(2, 1) == "black"
    assert get_chess_square_color(1, 2) == "black"
    assert get_chess_square_color(8, 8) == "white"
    assert get_chess_square_color(0, 8) == ""
    assert get_chess_square_color(2, 9) == ""
