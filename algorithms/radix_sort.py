def radixSort(nums):
    len_nums, min_num = len(nums), min(nums)
    if min_num < 0:
        for i in range(len_nums):
            nums[i] -= min_num
            
    max_num = max(nums)
    exp = 1

    while exp <= max_num:
        count = [0] * 10
        output = [0] * len_nums
        for num in nums:
            digit = (num // exp) % 10
            count[digit] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        for i in range(len_nums - 1, -1, -1):
            num = nums[i]
            digit = (num // exp) % 10
            pos = count[digit] - 1
            output[pos] = num
            count[digit] -= 1

        nums[:] = output
        exp *= 10

    if min_num < 0:
        for i in range(len_nums):
            nums[i] += min_num

    return nums

if __name__ == "__main__":
    print(radixSort([5, 4, 8, 1, 3, 2, 9, 6, 7]))