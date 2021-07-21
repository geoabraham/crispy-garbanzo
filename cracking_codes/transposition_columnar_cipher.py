import math as m


def main():
    secret_message = "Súper Secret Message!!"
    key = 8

    secret_message_encrypted = encrypt_message(secret_message, key)

    print(secret_message_encrypted + '|')

    secret_message_decrypted = decrypt_message(secret_message_encrypted, key)

    print(secret_message_decrypted + '|')

    return


def encrypt_message(message, key):
    # If you imagine each column is a string,
    # the result would be a list of eight strings
    encrypted_message = [''] * key

    for column in range(key):
        index = column
        while index < len(message):
            # Place the character at index in the string in column.
            encrypted_message[column] += message[index]
            # move index over
            index += key

    return ''.join(encrypted_message)


def decrypt_message(message, key):
    columns = int(m.ceil(len(message) / float(key)))
    shaded_boxes = (columns * key) - len(message)
    decrypted_message = [''] * columns

    column = 0
    row = 0
    for symbol in message:
        decrypted_message[column] += symbol
        column += 1
        if (column == columns) or (column == columns - 1 and row >= key - shaded_boxes):
            column = 0
            row += 1

    return ''.join(decrypted_message)


# If transposition_columnar_cipher.py is run (instead of imported as a module)
# call the main() function.
if __name__ == '__main__':
    main()
