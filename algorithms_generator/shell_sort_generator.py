def shellSortGenerator(nums):
    len_nums = len(nums)
    gap = len_nums // 2

    yield nums, None, None
    while gap > 0:
        for i in range(gap, len_nums):
            key = nums[i]
            j = i - gap

            yield nums, j + gap, j
            while j >= 0 and nums[j] > key:
                nums[j + gap] = nums[j]
                j -= gap
                yield nums, j + (2 * gap), j + gap
                        
            nums[j + gap] = key
            yield nums, j + gap, j + gap

        gap //= 2

    return nums

if __name__ == "__main__":
    nums = [5, 4, 8, -1, -3, -2, 9, 6, 7]
    for state, i1, i2 in shellSortGenerator(nums):
        print(f"Idx {i1} and {i2}: {state}")