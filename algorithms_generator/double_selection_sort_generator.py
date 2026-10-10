def doubleSelectionSortGenerator(nums):
    start, end = 0, len(nums) - 1

    while start < end:
        min_id = start
        max_id = start
        for i in range(start + 1, end + 1):
            yield nums, i, min_id
            if nums[i] < nums[min_id]:
                min_id = i

            yield nums, i, max_id
            if nums[i] > nums[max_id]:
                max_id = i

        nums[start], nums[min_id] = nums[min_id], nums[start]
        yield nums, start, min_id
        if max_id == start:
            max_id = min_id

        nums[end], nums[max_id] = nums[max_id], nums[end]
        yield nums, end, max_id
        start += 1
        end -= 1

    return nums

if __name__ == "__main__":
    nums = [5, 4, 8, -1, -3, -2, 9, 6, 7]
    for state, i1, i2 in doubleSelectionSortGenerator(nums):
        print(f"Idx {i1} and {i2}: {state}")