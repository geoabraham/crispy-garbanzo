import os
import sys
import time

import transposition_columnar_cipher


def main():
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    input_file_name = os.path.join(file_dir, 'assets/frankenstein.txt')
    key = 8

    encrypt_file(input_file_name, key, 'encrypt')
    encrypt_file(f'{input_file_name[0:-4]}.encrypted.txt', key, 'decrypt')


def encrypt_file(file_name, key, mode):
    if not os.path.exists(file_name):
        print('ERROR :: Cant find: ' + file_name)
        sys.exit()

    file_obj = open(file_name)
    file_content = file_obj.read()
    file_obj.close()

    print(f'{mode.title()}ing...')

    # Measure how long the encryption takes
    start_time = time.time()

    if mode == 'encrypt':
        translated = transposition_columnar_cipher.encrypt_message(file_content, key)
    elif mode == 'decrypt':
        translated = transposition_columnar_cipher.decrypt_message(file_content, key)
    else:
        print(f'ERROR :: Cannot understand the order: "{mode}". Use "encrypt" or "decrypt"')
        sys.exit()

    total_time = round(time.time() - start_time, 2)
    print(f'{mode.title()}ion time: {total_time} seconds')

    output_obj = open(f'{file_name[0:-4]}.{mode}ed.txt', 'w')
    output_obj.write(translated)
    output_obj.close()

    print(f'Done {mode}ing {file_name} ({len(file_content)} characters).')
    print(f'{mode.title()}ed file is {file_name[0:-4]}.{mode}ed.txt ')


if __name__ == '__main__':
    main()
