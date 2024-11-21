from generators import key_generator


def test_key_generator():
    key = key_generator.generate_key()
    assert len(key) == 2, "The Generated key should have 2 elements: the key and the accidental"
    assert key[0] in ["C", "D", "E", "F", "G", "A", "B"]
    assert key[1] in ["♭", "♯", "♮"], f"Invalid accent: {key[1]}"
    print(f"Test passed! Generated key: {key}")


if __name__ == "__main__":
    test_key_generator()
