def check_sum(nums):
    for num in nums:
        for other_num in nums:
            if num + other_num == 0:
                return True
    return False


num_list = [10, -14, 26, 5, -3, 13, -5]
print(check_sum(num_list))
