from random import sample
import string


def get_random_password(default_length=8) -> str:
    symbols = string.ascii_uppercase + string.ascii_lowercase + string.digits
    generation_password = ''.join(sample(symbols, default_length))
    return generation_password


print(get_random_password())
