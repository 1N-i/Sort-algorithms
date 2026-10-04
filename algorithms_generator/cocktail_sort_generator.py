def cocktailSortGenerator(nums):
    len_nums = len(nums)
    left, right = 0, len_nums - 1
    while left <= right:
        swapped = False
        for i in range(left, right):
            yield nums, i, i + 1
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                yield nums, i, i + 1
                swapped = True
        right -= 1

        for j in range(right, left, -1):
            yield nums, j, j - 1
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                yield nums, j, j - 1
                swapped = True
        left += 1

        if swapped == False:
            break

    return nums

if __name__ == "__main__":
    nums = [5, 4, 8, -1, -3, -2, 9, 6, 7]
    for state, i1, i2 in cocktailSortGenerator(nums):
        print(f"Idx {i1} and {i2}: {state}")