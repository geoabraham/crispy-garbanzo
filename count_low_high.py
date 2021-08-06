# If a number is greater than 50 or divisible by 3, it will count as a high.
# If these conditions are not met, the number is considered a low.
# At the end of the function, you must return a list that contains the number of lows and highs, in that order.
# In case the list is empty, you may return None.
def count_low_high_my_solution(num_list):
    if len(num_list) == 0:
        return None
    result = [0, 0]
    for num in num_list:
        if num > 50 or num % 3 == 0:
            result[1] += 1
        else:
            result[0] += 1
    return result


def count_low_high_filter_lambda_solution(num_list):
    if (len(num_list) == 0):
        return None
    high_list = list(filter(lambda n: n > 50 or n % 3 == 0, num_list))
    low_list = list(filter(lambda n: n <= 50 and not n % 3 == 0, num_list))
    return [len(low_list), len(high_list)]


def count_low_high_list_comprehension_solution(num_list):
    if (len(num_list) == 0):
        return None
    high_list = len([n for n in num_list if n > 50 or n % 3 == 0])
    low_list = len([n for n in num_list if n <= 50 and not n % 3 == 0])
    return [low_list, high_list]


num_list = [20, 9, 51, 81, 50, 42, 77]

print(count_low_high_my_solution(num_list))

print(count_low_high_filter_lambda_solution(num_list))

print(count_low_high_list_comprehension_solution(num_list))
