# 'fH3r5&frp5r7&Zr66ntr(('
# 'Súper Secret Message!!'
secret_message = 'fH3r5&frp5r7&Zr66ntr(('
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
NUMBERS = '1234567890'
SPACE_AND_SPECIAL_CHARACTERS = ' ¡!¿?.+*/@#$%&=()-_:;,ñÑáéíóúÁÉÍÓÚ'
SYMBOLS = LETTERS + NUMBERS + SPACE_AND_SPECIAL_CHARACTERS

for key in range(len(SYMBOLS)):
    hacked_message = ''

    for symbol in secret_message:
        if symbol in SYMBOLS:
            encrypted_index = SYMBOLS.find(symbol)

            # Perform decryption:
            symbol_index = encrypted_index - key

            # Handle wrap-around, if needed:
            if symbol_index < 0:
                symbol_index += len(SYMBOLS)

            hacked_message += SYMBOLS[symbol_index]
        else:
            hacked_message += symbol

    print(hacked_message)
