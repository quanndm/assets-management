import string
import random


def generate_password(length: int = 12) -> str:
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure that the password has at least one of each type of character
    password = [random.choice(string.ascii_lowercase),
                random.choice(string.ascii_uppercase),
                random.choice(string.digits),
                random.choice(string.punctuation)]

    # Fill the rest of the password with random characters
    for _ in range(length - 4):
        password.append(random.choice(characters))

    # Shuffle the password to randomize the order of characters
    random.shuffle(password)

    # Convert the list of characters to a string
    password = ''.join(password)

    return password
