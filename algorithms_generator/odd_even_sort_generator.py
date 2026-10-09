def oddEvenSortGenerator(nums):
    len_nums = len(nums)
    swapped = True
    while swapped:
        swapped = False
        for even in range(0, len_nums - 1, 2):
            yield nums, even, even + 1
            if nums[even] > nums[even + 1]:
                nums[even], nums[even + 1] = nums[even + 1], nums[even]
                yield nums, even, even + 1
                swapped = True

        for odd in range(1, len_nums - 1, 2):
            yield nums, odd, odd + 1
            if nums[odd] > nums[odd + 1]:
                nums[odd], nums[odd + 1] = nums[odd + 1], nums[odd]
                yield nums, odd, odd + 1
                swapped = True

    return nums

if __name__ == "__main__":
    nums = [5, 4, 8, -1, -3, -2, 9, 6, 7]
    for state, i1, i2 in oddEvenSortGenerator(nums):
        print(f"Idx {i1} and {i2}: {state}")