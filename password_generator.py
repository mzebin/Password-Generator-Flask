import random
import string

UPPERCASE = string.ascii_uppercase
LOWERCASE = string.ascii_lowercase
DIGITS = string.digits
PUNCTUATION = string.punctuation.replace("-", "")


def generator(**kwargs):
    length = kwargs.get("length", 14)
    characters = get_characters(**kwargs)

    password = ""
    for i in range(length):
        if i % 3 == 0 and i != 0 and i + 1 != length:
            password += "-"
        else:
            password += random.choice(characters)

    return password


def get_characters(**kwargs):
    pass
