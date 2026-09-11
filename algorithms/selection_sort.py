def selectionSort(nums):
    len_nums = len(nums)

    for i in range(len_nums):
        min_i = i

        for j in range(i + 1, len_nums):
            if nums[j] < nums[min_i]:
                min_i = j

        nums[i], nums[min_i] = nums[min_i], nums[i]

    return nums

if __name__ == "__main__":
    print(selectionSort([5, 4, 8, 1, 3, 2, 9, 6, 7]))