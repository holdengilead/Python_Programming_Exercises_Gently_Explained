def fizz_buzz(up_to: int) -> None:
    for i in range(1, up_to + 1):
        if i % 3 == 0:
            print("Fizz", end="")
        if i % 5 == 0:
            print("Buzz", end="")
        if i % 3 != 0 and i % 5 != 0:
            print(i, end="")
        print(" ", end="")


if __name__ == "__main__":
    fizz_buzz(35)
