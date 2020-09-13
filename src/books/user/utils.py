import random
import string


def generate_random_password(password_len: int = 10):
    result = ''
    chars = string.digits + string.punctuation + string.ascii_letters
    for _ in range(password_len):
        result += random.choice(chars)
    return result
