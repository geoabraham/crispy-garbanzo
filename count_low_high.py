# If a number is greater than 50 or divisible by 3, it will count as a high.
# If these conditions are not met, the number is considered a low.
# At the end of the function, you must return a list that contains the number of lows and highs, in that order.
# In case the list is empty, you may return None.
def count_low_high(num_list):
    if len(num_list) == 0:
        return None
    result = [0, 0]
    for num in num_list:
        if num > 50 or num % 3 == 0:
            result[1] += 1
        else:
            result[0] += 1
    return result
