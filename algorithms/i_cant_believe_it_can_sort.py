def iCantBelieveItCanSort(nums):
    len_nums = len(nums)

    for i in range(len_nums):
        for j in range(len_nums):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

    return nums

if __name__ == "__main__":
    print(iCantBelieveItCanSort([5, 4, 8, -1, -3, -2, 9, 6, 7]))