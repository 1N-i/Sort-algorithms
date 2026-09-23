def bubbleSortGenerator(nums):
    len_nums = len(nums)
    for i in range(len_nums):
        for j in range(len_nums - i - 1):
            yield nums, j, j + 1
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                yield nums, j, j + 1

    return nums

if __name__ == "__main__":
    nums = [5, 4, 8, -1, -3, -2, 9, 6, 7]
    for state, i1, i2 in bubbleSortGenerator(nums):
        print(f"Comparando índices {i1} e {i2}: {state}")