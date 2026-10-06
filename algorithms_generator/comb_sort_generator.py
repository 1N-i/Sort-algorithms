def combSortGenerator(nums):
    gap = len(nums)
    swapped = False

    while gap > 1 or swapped:
        swapped = False
        gap = int(gap // 1.3)
        if gap < 1: gap = 1

        for i in range(len(nums) - gap):
            yield nums, i, i + gap
            if nums[i] > nums[i + gap]:
                nums[i], nums[i + gap] = nums[i + gap], nums[i]
                yield nums, i, i + gap
                swapped = True

    return nums

if __name__ == "__main__":
    nums = [5, 4, 8, -1, -3, -2, 9, 6, 7]
    for state, i1, i2 in combSortGenerator(nums):
        print(f"Idx {i1} and {i2}: {state}")