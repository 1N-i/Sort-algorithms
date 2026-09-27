def radixSortGenerator(nums):
    len_nums, min_num = len(nums), min(nums)
    max_num = max(nums) - min_num
    if min_num == max_num + min_num:
        return nums

    exp = 1
    while exp <= max_num:
        count = [0] * 10
        output = [0] * len_nums

        for i in range(len_nums):
            yield nums, i, None
            val = nums[i] - min_num
            digit = (val // exp) % 10
            count[digit] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        for i in range(len_nums - 1, -1, -1):
            num = nums[i]
            val = nums[i] - min_num
            digit = (val // exp) % 10
            pos = count[digit] - 1
            output[pos] = num
            count[digit] -= 1
            yield nums, i, pos

        for k in range(len_nums):
            nums[k] = output[k]
            yield nums, k, None

        exp *= 10
        yield nums, None, None

    return nums

if __name__ == "__main__":
    nums = [5, 4, 8, -1, -3, -2, 9, 6, 7]
    for state, i1, i2 in radixSortGenerator(nums):
        print(f"Idx {i1} and {i2}: {state}")