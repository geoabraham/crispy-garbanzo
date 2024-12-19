import math


def main():
    secret_message = "Súper Secret Message!!"
    key = 8

    encrypted_message = encrypt_message(secret_message, key)
    assert encrypted_message != secret_message

    decrypted_message = decrypt_message(encrypted_message, key)
    assert decrypted_message == secret_message


def encrypt_message(message: str, key: int) -> str:
    """Encrypts a given message using columnar transposition cipher."""
    encrypted_message = [""] * key
    for column in range(key):
        index = column
        while index < len(message):
            encrypted_message[column] += message[index]
            index += key

    return "".join(encrypted_message)


def decrypt_message(encrypted_message: str, key: int) -> str:
    """Decrypts a given encrypted message using columnar transposition cipher."""
    columns = math.ceil(len(encrypted_message) / float(key))
    shaded_boxes = (columns * key) - len(encrypted_message)
    decrypted_message = [""] * columns

    column = 0
    row = 0
    for symbol in encrypted_message:
        decrypted_message[column] += symbol
        column += 1
        if column == columns or (column == columns - 1 and row >= key - shaded_boxes):
            column = 0
            row += 1

    return "".join(decrypted_message)


if __name__ == "__main__":
    main()
