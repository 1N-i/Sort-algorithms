def quickSortGenerator(nums, low=0, high=None):
    if high is None:
        high = len(nums) - 1

    if low < high:
        pivot = nums[high]
        i = low - 1

        for j in range(low, high):
            yield nums, j, high

            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
                yield nums, i, j

        pivot_i = i + 1
        nums[pivot_i], nums[high] = nums[high], nums[pivot_i]
        yield nums, pivot_i, high

        yield from quickSortGenerator(nums, low, pivot_i - 1)
        yield from quickSortGenerator(nums, pivot_i + 1, high)

    return nums

if __name__ == "__main__":
    nums = [5, 4, 8, -1, -3, -2, 9, 6, 7]
    for state, i1, i2 in quickSortGenerator(nums):
        print(f"Idx {i1} and {i2}: {state}")