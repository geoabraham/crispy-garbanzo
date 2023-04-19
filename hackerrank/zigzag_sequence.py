def find_zigzag_sequence(nums: list, total_num: int):
    nums.sort()
    mid = int((total_num - 1) / 2)
    nums[mid], nums[total_num - 1] = nums[total_num - 1], nums[mid]

    st = mid + 1
    ed = total_num - 2
    while st <= ed:
        nums[st], nums[ed] = nums[ed], nums[st]
        st = st + 1
        ed = ed - 1

    for i in range(total_num):
        if i == total_num - 1:
            print(nums[i])
        else:
            print(nums[i], end=' ')
    return


test_cases = 1  # int(input())
for cs in range(test_cases):
    n = 7  # int(input())
    a = [1, 2, 3, 4, 5, 6, 7]  # list(map(int, input().split()))
    find_zigzag_sequence(a, n)
