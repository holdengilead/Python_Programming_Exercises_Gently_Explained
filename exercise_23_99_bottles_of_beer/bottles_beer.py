def beer_song() -> None:
    for i in range(99, 0, -1):
        plural = "s" if i > 1 else ""
        print(f"{i} bottle{plural} of beer on the wall, {i} bottle{plural} of beer,")
        print("Take one down,\nPass it around,")
        plural = "" if i - 1 == 1 else "s"
        left = i - 1 if i > 1 else "No more"
        final = "," if i > 1 else "!"
        print(f"{left} bottle{plural} of beer on the wall{final}\n")


if __name__ == "__main__":
    beer_song()
