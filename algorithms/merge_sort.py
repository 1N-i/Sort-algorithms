def mergeSort(nums):
    if len(nums) <= 1: return nums

    nums_left = mergeSort(nums[:len(nums) // 2])
    nums_right = mergeSort(nums[len(nums) // 2:])
    nums = []
    left, right = 0, 0

    while left < len(nums_left) and right < len(nums_right):
        if nums_left[left] < nums_right[right]:
            nums.append(nums_left[left])
            left += 1
        else:
            nums.append(nums_right[right])
            right += 1

    nums.extend(nums_right[right:])
    nums.extend(nums_left[left:])

    return nums

if __name__ == "__main__":
    print(mergeSort([5, 4, 8, 1, 3, 2, 9, 6, 7]))