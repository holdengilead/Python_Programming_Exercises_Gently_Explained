from rot import rot13


def test_encrypt():
    assert rot13("Hello, world!") == "Uryyb, jbeyq!"


def test_decrypt():
    assert rot13("Uryyb, jbeyq!") == "Hello, world!"


def test_encrypt_decrypt():
    assert rot13(rot13("Hello, world!")) == "Hello, world!"


def test_encrypt_all_lowercase_letters():
    assert rot13("abcdefghijklmnopqrstuvwxyz") == "nopqrstuvwxyzabcdefghijklm"


def test_encrypt_all_uppercase_letters():
    assert rot13("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == "NOPQRSTUVWXYZABCDEFGHIJKLM"
