def gnomeSortGenerator(nums):
    i = 1
    while i < len(nums):
        if i == 0: i += 1
        else:
            yield nums, i, i - 1
            if nums[i - 1] > nums[i]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
                yield nums, i, i - 1
                i -= 1
            else: i += 1

    return nums

if __name__ == "__main__":
    nums = [5, 4, 8, -1, -3, -2, 9, 6, 7]
    for state, i1, i2 in gnomeSortGenerator(nums):
        print(f"Idx {i1} and {i2}: {state}")