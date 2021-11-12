from typing import List


def get_squared_even_numbers(numbers: List[int]):
    squared_even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            squared_even_numbers.append(number ** 2)
    return squared_even_numbers


def get_squared_odd_numbers_by_num(numbers):
    squared_odd_numbers = dict()
    for number in numbers:
        if number % 2 != 0:
            squared_odd_numbers[number] = number ** 2
    return squared_odd_numbers


def main():
    assert get_squared_even_numbers([1, 2, 3, 4, 5, 6, 7]) == [4, 16, 36]
    assert get_squared_odd_numbers_by_num([1, 2, 3, 4, 5, 6, 7]) == {
        1: 1, 3: 9, 5: 25, 7: 49}
    print("Challenge 2 works!")

if __name__ == "__main__":
    main()