def cocktailSort(nums):
    len_nums = len(nums)
    left, right = 0, len_nums - 1
    while left <= right:
        swapped = False
        for i in range(left, right):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        right -= 1

        for j in range(right, left, -1):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                swapped = True
        left += 1

        if swapped == False:
            break

    return nums

if __name__ == "__main__":
    print(cocktailSort([5, 4, 8, -1, -3, -2, 9, 6, 7]))