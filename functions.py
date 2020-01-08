import random

file_name = "players.txt"

def calc():
    num1 = float(input("num1: "))
    num2 = float(input("num2: "))
    op = input("operator: ")

    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        print(num1 / num2)
    else:
        print("Invalid Operator !")


def guess_secret_word():
    guess = ""
    secret_word = "Ble"
    guess_count = 0
    guess_limit = 3
    out_of_guesses = False

    while guess != secret_word and not out_of_guesses:
        if guess_count < guess_limit:
            guess = input("Enter guess: ")
            guess_count += 1

            if guess_count != 3:
                print("Strike {0}!!".format(guess_count))
                print("{0} guess/es left".format(guess_limit - guess_count))

            if guess_count == 3:
                print("Strike 3!!")

        else:
            out_of_guesses = True

    if out_of_guesses:
        print("OUT!")
    else:
        print("WIN!")


def raise_to_power(num, num_power):
    result = 1

    for index in range(num_power):
        result *= num

    return result


def replace_vowel_for_x(phrase):
    result = ""

    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                result += "X"
            else:
                result += "x"
        else:
            result += letter

    return result


def replace_vowel_for_number(phrase):
    result = ""
    vower_numbers = {
        "a": "4",
        "e": "3",
        "i": "1",
        "o": "0",
        "u": "u",
    }

    try:
        print(int("ok"))
    except ValueError as valErr:
        print(valErr)
    else:
        print("pass")
    finally:
        print("Finally !!")

    for letter in phrase:
        if letter.lower() in "aeiou":
            result += vower_numbers[letter.lower()]
        else:
            result += letter

    return result


def read_file():
    players_file = open(file_name, "r")
    # print(players_file.read())  # read util Eof
    # print(players_file.readline())  # read the last unread line until EoF
    for player in players_file.readlines():  # return a list with each line
        print(player)

    players_file.close()


def append_file():
    players_file = open(file_name, "a")
    players_file.write("Player{0} - {1}\n".format(
        random.choice(range(32)), random_role()))
    players_file.close()

def write_file():
    players_file = open(file_name, "w")
    players_file.write("Player{0} - {1}\n".format(
        random.choice(range(32)), random_role()))
    players_file.close()

def random_role():
    roles = ["Tank", "Healer", "Support", "Stealth", "Leader", "Controller"]
    return random.choice(roles)

def roll_dice(num):
    return random.randint(1, num)


# calc()
# guess_secret_word()
# print (raise_to_power(2, 3))
# print(replace_vowel_for_x("Eggs Please !!"))

# print(replace_vowel_for_number("Eggs Please !!"))

append_file()
read_file()
print("FLUSH!")
write_file()
read_file()