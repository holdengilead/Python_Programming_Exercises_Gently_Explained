from itertools import combinations


def print_handshakes(people: list[str]) -> int:
    num_hand = 0
    for person_a, person_b in combinations(people, 2):
        num_hand += 1
        print(f"{person_a} shakes hands with {person_b}")
    return num_hand


if __name__ == "__main__":
    assert print_handshakes(["Alice", "Bob"]) == 1
    assert print_handshakes(["Alice", "Bob", "Carol"]) == 3
    assert print_handshakes(["Alice", "Bob", "Carol", "David"]) == 6
