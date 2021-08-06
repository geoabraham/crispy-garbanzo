def find_max(lis):
    row_sum = 0
    max_sum = (0, 0)

    for row_num in range(len(lis)):
        for num in lis[row_num]:
            row_sum += num
        if max_sum[1] < row_sum:
            max_sum = (row_num, row_sum)
        row_sum = 0

    return max_sum[0]


list_find_max = [[1, 2, 3], [2, 3, 3], [1, 3, 3]]
print(find_max(list_find_max))
