LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
NUMBERS = '1234567890'
SPACE_AND_SPECIAL_CHARACTERS = ' ¡!¿?.+*/@#$%&=()-_:;,ñÑáéíóúÁÉÍÓÚ'
SYMBOLS = LETTERS + NUMBERS + SPACE_AND_SPECIAL_CHARACTERS


def main():
    secret_message = 'Súper Secret Message!!'
    key = 13

    encrypted_message = encrypt_message(secret_message, key)

    print(encrypted_message)

    decrypted_message = encrypt_message(encrypted_message, key, 'decrypt')

    print(decrypted_message)


def encrypt_message(message, key, mode='encrypt'):
    encrypted_message = ''

    for symbol in message:
        if symbol in SYMBOLS:
            symbol_index = SYMBOLS.find(symbol)
            encrypted_index = 0

            # Perform encryption/decryption:
            if mode == 'encrypt':
                encrypted_index = symbol_index + key
            elif mode == 'decrypt':
                encrypted_index = symbol_index - key

            # Handle wrap-around, if needed:
            if encrypted_index >= len(SYMBOLS):
                encrypted_index -= len(SYMBOLS)
            elif encrypted_index < 0:
                encrypted_index += len(SYMBOLS)

            encrypted_message += SYMBOLS[encrypted_index]
        else:
            encrypted_message += symbol

    return encrypted_message


if __name__ == '__main__':
    main()
