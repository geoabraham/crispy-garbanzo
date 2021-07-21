from cracking_codes import detect_english


def main():
    message = 'Hello World!'
    is_english = detect_english.is_english(message)
    print(f'message: {message}, isEnglish: {is_english}')

    message = 'fH3r 5&f rp5r7 &Zr66 ntr'
    is_english = detect_english.is_english(message)
    print(f'message: {message}, isEnglish: {is_english}')

    message = 'Hello World! fH3r5  &frp5r7&Zr  66ntr'
    is_english = detect_english.is_english(message)
    print(f'message: {message}, isEnglish: {is_english}')

    message = 'Hello World! Hello World! Hello World! Hello World! Hello World! fH3r  5&fr  p5r7 &Zr 66ntr'
    is_english = detect_english.is_english(message)
    print(f'message: {message}, isEnglish: {is_english}')


if __name__ == '__main__':
    main()
