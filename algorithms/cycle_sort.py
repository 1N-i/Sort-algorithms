def cycleSort(nums):
    len_nums = len(nums)
    for i in range(len_nums):
        lower = 0
        num = nums[i]

        for j in range(len_nums):
            if nums[j] < num:
                lower += 1

        while lower != i:
            if nums[i] == nums[lower]:
                lower += 1
                continue

            nums[i], nums[lower] = nums[lower], nums[i]

            lower = 0
            num = nums[i]
            for j in range(len_nums):
                if nums[j] < num:
                    lower += 1

    return nums

if __name__ == "__main__":
    print(cycleSort([5, 4, 8, -1, -3, -2, 9, 6, 7]))