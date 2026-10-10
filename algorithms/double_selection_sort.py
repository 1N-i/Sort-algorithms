def doubleSelectionSort(nums):
    start, end = 0, len(nums) - 1

    while start < end:
        min_id = start
        max_id = start
        for i in range(start + 1, end + 1):
            if nums[i] < nums[min_id]:
                min_id = i

            if nums[i] > nums[max_id]:
                max_id = i

        nums[start], nums[min_id] = nums[min_id], nums[start]
        if max_id == start:
            max_id = min_id
        nums[end], nums[max_id] = nums[max_id], nums[end]
        start += 1
        end -= 1

    return nums

if __name__ == "__main__":
    print(doubleSelectionSort([5, 4, 8, -1, -3, -2, 9, 6, 7]))