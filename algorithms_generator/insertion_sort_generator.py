def insertionSortGenerator(nums):
    len_nums = len(nums)
    for i in range(1, len_nums):
        key = nums[i]
        j = i - 1

        yield nums, j + 1, j
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
            yield nums, j + 2, j + 1
            
        nums[j + 1] = key
        yield nums, j + 1, j + 1
        
    return nums

if __name__ == "__main__":
    nums = [5, 4, 8, -1, -3, -2, 9, 6, 7]
    for state, i1, i2 in insertionSortGenerator(nums):
        print(f"Idx {i1} and {i2}: {state}")