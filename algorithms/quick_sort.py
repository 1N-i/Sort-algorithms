def quickSort(nums):
    if len(nums) <= 1: return nums

    lower, bigger = [], []
    comparator = nums[-1]
    comparators = []
    for num in nums:
        if num < comparator:
            lower.append(num)

        elif num > comparator:
            bigger.append(num)

        else:
            comparators.append(num)

    nums = quickSort(lower) + comparators + quickSort(bigger)

    return nums

if __name__ == "__main__":
    print(quickSort([5, 4, 8, -1, -3, -2, 9, 6, 7]))