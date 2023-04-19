def diagonal_difference(arr):
    # Write your code here
    total_rows = len(arr) - 1
    row_index = 0
    primary_diag = 0
    secondary_diag = 0

    while row_index < len(arr):
        primary_diag += arr[row_index][row_index]
        secondary_diag += arr[row_index][total_rows - row_index]
        row_index += 1

    return abs(primary_diag - secondary_diag)


if __name__ == '__main__':
    n = 3

    arr = [[11, 2, 4],
           [4, 5, 6],
           [10, 8, -12]]

    result = diagonal_difference(arr)

    print(result)
