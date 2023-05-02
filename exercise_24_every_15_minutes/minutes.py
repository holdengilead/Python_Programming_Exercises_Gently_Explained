def times() -> None:
    for meridian in ("am", "pm"):
        for hour in (12,) + tuple(range(1, 12)):
            for minutes in ("00", "15", "30", "45"):
                print(f"{hour}:{minutes} {meridian}")


if __name__ == "__main__":
    times()
