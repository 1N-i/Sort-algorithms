def iCantBelieveItCanSortGenerator(nums):
    len_nums = len(nums)
    for i in range(len_nums):
        for j in range(len_nums):
            yield nums, i, j
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                yield nums, i, j

    return nums

if __name__ == "__main__":
    nums = [5, 4, 8, -1, -3, -2, 9, 6, 7]
    for state, i1, i2 in iCantBelieveItCanSortGenerator(nums):
        print(f"Idx {i1} and {i2}: {state}")