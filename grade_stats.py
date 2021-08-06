# The grades may not always be A, B, C, D, E, and I.
# For example, A- is a valid grade in some places as is 3.7.
# You should treat whatever is in the passed-in list as a valid grade.

def grade_stats(lis):
    # If the passed-in list is empty, your function should return an empty dictionary.
    result = dict()
    if len(lis) == 0:
        return result
    # Insert your code here
    for grade in lis:
        if result.__contains__(grade):
            result[grade] += 1
        else:
            result[grade] = 1

    return result


G = ['A', 'I', 'C', 'C', 'E', 'B', 'A', 'E', 'E', 'A', 'B', 'B', 'B']
# {'A':3, 'I':1, 'C':2, 'E':3, 'B':4}
print(grade_stats(G))
