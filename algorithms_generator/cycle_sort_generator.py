def cycleSortGenerator(nums):
    len_nums = len(nums)
    for i in range(len_nums):
        lower = 0
        num = nums[i]

        for j in range(len_nums):
            yield nums, j, i
            if nums[j] < num:
                lower += 1

        while lower != i:
            yield nums, i, lower
            if nums[i] == nums[lower]:
                lower += 1
                continue

            nums[i], nums[lower] = nums[lower], nums[i]
            yield nums, i, lower

            lower = 0
            num = nums[i]
            for j in range(len_nums):
                yield nums, j, i
                if nums[j] < num:
                    lower += 1

    return nums

if __name__ == "__main__":
    nums = [5, 4, 8, -1, -3, -2, 9, 6, 7]
    for state, i1, i2 in cycleSortGenerator(nums):
        print(f"Idx {i1} and {i2}: {state}")