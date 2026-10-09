def oddEvenSort(nums):
    len_nums = len(nums)
    swapped = True
    while swapped:
        swapped = False
        for even in range(0, len_nums - 1, 2):
            if nums[even] > nums[even + 1]:
                nums[even], nums[even + 1] = nums[even + 1], nums[even]
                swapped = True

        for odd in range(1, len_nums - 1, 2):
            if nums[odd] > nums[odd + 1]:
                nums[odd], nums[odd + 1] = nums[odd + 1], nums[odd]
                swapped = True

    return nums

if __name__ == "__main__":
    print(oddEvenSort([5, 4, 8, -1, -3, -2, 9, 6, 7]))