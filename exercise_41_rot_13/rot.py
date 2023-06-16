from string import ascii_lowercase as LWR
from string import ascii_uppercase as UPP


def rot13(text: str) -> str:
    cipher = dict(zip(LWR, LWR[13:] + LWR[:13])) | dict(zip(UPP, UPP[13:] + UPP[:13]))

    return "".join(cipher.get(letter, letter) for letter in text)
