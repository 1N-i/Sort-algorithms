def combSort(nums):
    gap = len(nums)
    swapped = False

    while gap > 1 or swapped:
        swapped = False
        gap = int(gap // 1.3)
        if gap < 1: gap = 1

        for i in range(len(nums) - gap):
            if nums[i] > nums[i + gap]:
                nums[i], nums[i + gap] = nums[i + gap], nums[i]
                swapped = True

    return nums

if __name__ == "__main__":
    print(combSort([5, 4, 8, -1, -3, -2, 9, 6, 7]))