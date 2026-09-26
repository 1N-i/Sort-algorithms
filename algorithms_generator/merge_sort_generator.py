def mergeSortGenerator(nums, start=0, end=None):
    if end is None:
        end = len(nums) - 1

    if start < end:
        mid = (start + end) // 2

        yield from mergeSortGenerator(nums, start, mid)
        yield from mergeSortGenerator(nums, mid + 1, end)

        left_part = nums[start : mid + 1]
        right_part = nums[mid + 1 : end + 1]

        i, j = 0, 0
        k = start

        while i < len(left_part) and j < len(right_part):
            yield nums, start + i, mid + 1 + j

            if left_part[i] <= right_part[j]:
                nums[k] = left_part[i]
                i += 1
            else:
                nums[k] = right_part[j]
                j += 1

            yield nums, k, None
            k += 1

        while i < len(left_part):
            nums[k] = left_part[i]
            yield nums, k, None
            i += 1
            k += 1

        while j < len(right_part):
            nums[k] = right_part[j]
            yield nums, k, None
            j += 1
            k += 1

    return nums

if __name__ == "__main__":
    nums = [5, 4, 8, -1, -3, -2, 9, 6, 7]
    for state, i1, i2 in mergeSortGenerator(nums):
        print(f"Idx {i1} and {i2}: {state}")