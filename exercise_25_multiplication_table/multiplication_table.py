def mul_table() -> None:
    print("  | 1  2  3  4  5  6  7  8  9 10")
    print("--+------------------------------")
    for i in range(1, 11):
        print(f'{str(i).rjust(2)}|{" ".join(str(i*j).rjust(2) for j in range(1,11))}')


if __name__ == "__main__":
    mul_table()
