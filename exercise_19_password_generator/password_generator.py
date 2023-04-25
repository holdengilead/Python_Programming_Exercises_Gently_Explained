from random import choice, shuffle
from string import ascii_lowercase, ascii_uppercase, digits

LOWER_LETTERS = ascii_lowercase
UPPER_LETTERS = ascii_uppercase
NUMBERS = digits
SPECIAL = "~!@#$%^&*()_+."
_ALL = LOWER_LETTERS + UPPER_LETTERS + NUMBERS + SPECIAL


def generate_password(length: int) -> str:
    length = max(12, length)
    password = [
        choice(LOWER_LETTERS),
        choice(UPPER_LETTERS),
        choice(NUMBERS),
        choice(SPECIAL),
        "".join(choice(_ALL) for _ in range(length - 4)),
    ]
    shuffle(password)
    return "".join(password)


if __name__ == "__main__":
    assert len(generate_password(8)) == 12
    pw = generate_password(14)
    assert len(pw) == 14
    hasLowercase = False
    hasUppercase = False
    hasNumber = False
    hasSpecial = False
    for character in pw:
        if character in LOWER_LETTERS:
            hasLowercase = True
        if character in UPPER_LETTERS:
            hasUppercase = True
        if character in NUMBERS:
            hasNumber = True
        if character in SPECIAL:
            hasSpecial = True
    assert hasLowercase and hasUppercase and hasNumber and hasSpecial
