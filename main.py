import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.sample(characters, k=length))
    return password


print(generate_password(12))
