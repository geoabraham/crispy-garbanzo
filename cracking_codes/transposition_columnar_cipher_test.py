import random
import sys
import transposition_columnar_cipher

random.seed(42)  # set the random "seed" to a static value
for i in range(20):  # run 20 tests
    # Generate random messages to test.
    # The message will have a random length:
    message = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * random.randint(4, 40)

    # Convert the message string to a list to shuffle it.
    message = list(message)
    random.shuffle(message)
    message = "".join(message)  # convert list to string

    print('Test #%s: "%s..."' % (i + 1, message[:50]))

    # Check all possible keys for each message.
    for key in range(1, int(len(message) / 2)):
        encrypted = transposition_columnar_cipher.encrypt_message(message, key)
        decrypted = transposition_columnar_cipher.decrypt_message(encrypted, key)

        # If the decryption doesn't match the original message,
        # display an error message and quit.
        if message != decrypted:
            print("Mismatch with key %s and message %s." % (key, message))
            print("Decrypted as: " + decrypted)
            sys.exit()

print("Transposition cipher test passed.")
