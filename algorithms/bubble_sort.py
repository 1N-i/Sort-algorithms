def bubbleSort(nums):
    len_nums = len(nums)
    for i in range(len_nums):
        for j in range(len_nums - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums

if __name__ == "__main__":
    print(bubbleSort([5, 4, 8, -1, -3, -2, 9, 6, 7]))