# Your function should preserve the order of values in the list (removing duplicates that come later in the list),
# but the values in the set can appear in any order.

def remove_duplicates(lis):
    # You may construct the set to be returned,
    # but you are not allowed to construct other structured objects (no string, list, etc.).

    # Insert your code here
    result = list(tuple())
    for point in lis:
        if len([r for r in result if r == point]) == 0:
            result.append(point)
    return result
    pass


points = [(1, 3), (7, 7), (1, 3), (7, 8), (1, 3), (7, 7),
          (7, 8), (4, 2), (7, 8), (7, 8), (4, 2), (4, 2)]
print(remove_duplicates(points))
# [(1, 3), (7, 7), (7, 8), (4, 2)] 