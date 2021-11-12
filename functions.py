import random
import time
from functools import wraps

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


def calc_hi_lo_avg(*args, log_to_console=False):
    hi = int(bool(args)) and max(args)
    lo = int(bool(args)) and min(args)
    avg = (hi + lo) / 2
    if log_to_console:
        print(avg)
    return avg


def func(a, b=10):
    print(a, b)


def func(a, b, *args):
    print(a, b, args)


def func(a, b, *args, kw1, kw2=100):
    print(a, b, args, kw1, kw2)


def func(a, b=10, *, kw1, kw2=100):
    print(a, b, kw1, kw2)


def func(a, b, *args, kw1, kw2=100, **kwargs):
    print(a, b, args, kw1, kw2, kwargs)


def func(a, b=10, *, kw1, kw2=100, **kwargs):
    print(a, b, kw1, kw2, kwargs)


def func_args(*args):
    print(args)


def func_kwargs(**kwargs):
    print(kwargs)


def func_args_kwargs(*args, **kwargs):
    print(args, kwargs)


def time_it(fn, *args, rep=5, **kwargs):
    start = time.perf_counter()

    for i in range(rep):
        fn(*args, **kwargs)

    end = time.perf_counter()
    return (end - start) / rep


def fact(n):
    from operator import mul
    from functools import reduce

    return reduce(mul, range(1, n+1))


def compute_powers_1(n, *, start=1, end):
    # using a for loop
    results = []
    for i in range(start, end):
        results.append(n**i)
    return results


def compute_powers_2(n, *, start=1, end):
    # using a list comprehension
    return [n**i for i in range(start, end)]


def compute_powers_3(n, *, start=1, end):
    # using a generator expression
    return (n**i for i in range(start, end))


def counter(fn):
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'Function {fn.__name__} was called {count} times')
        return fn(*args, **kwargs)

    return inner


# calc()
# guess_secret_word()
# print (raise_to_power(2, 3))
# print(replace_vowel_for_x("Eggs Please !!"))

# print(replace_vowel_for_number("Eggs Please !!"))

# help(func)

# func(10, 12, 13, d=30)

# compute_powers_1(2, end=5)

# compute_powers_2(2, end=5)

# list(compute_powers_3(2, end=5))

# time_it(compute_powers_1, n=2, end=20000, rep=4)

# time_it(compute_powers_2, 2, end=20000, rep=4)

# time_it(compute_powers_3, 2, end=20000, rep=4)


# append_file()
# read_file()
# print("FLUSH!")
# write_file()
# read_file()

points = [(1, 4), (10, 40), (23, 14), (5, 6), (7, 8)]
for x, y in points:
    print(f'x:{x},y:{y}')

columns = ['name', 'shares', 'price']
values = ['GOOG', 100, 490.1]
pairs = zip(columns, values)
print(*pairs)
d = dict(zip(columns, values))
print(d)