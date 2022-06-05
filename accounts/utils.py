from random import randint


def create_random_8_digits_code():
    return str(randint(10_000_000, 99_000_000))
