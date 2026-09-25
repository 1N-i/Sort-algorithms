def selectionSortGenerator(nums):
    len_nums = len(nums)
    for i in range(len_nums):
        min_i = i
        for j in range(i + 1, len_nums):
            yield nums, j, min_i
            if nums[j] < nums[min_i]:
                min_i = j

        nums[i], nums[min_i] = nums[min_i], nums[i]
        yield nums, i, min_i

    return nums

if __name__ == "__main__":
    nums = [5, 4, 8, -1, -3, -2, 9, 6, 7]
    for state, i1, i2 in selectionSortGenerator(nums):
        print(f"Idx {i1} and {i2}: {state}")