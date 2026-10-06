def gnomeSort(nums):
    i = 1
    while i < len(nums):
        if i == 0: i += 1
        elif nums[i - 1] > nums[i]:
            nums[i - 1], nums[i] = nums[i], nums[i - 1]
            i -= 1
        else: i += 1

    return nums

if __name__ == "__main__":
    print(gnomeSort([5, 4, 8, -1, -3, -2, 9, 6, 7]))