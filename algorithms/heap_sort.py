def heapSort(nums):
    def heapify(nums, n, i):
        largest = i
        left, right = (2 * i) + 1, (2 * i) + 2

        if left < n and nums[left] > nums[largest]:
            largest = left
        if right < n and nums[right] > nums[largest]:
            largest = right

        if i != largest:
            nums[i], nums[largest] = nums[largest], nums[i]
            heapify(nums, n, largest)

    len_nums = len(nums)
    for i in range((len_nums // 2) - 1, -1, -1):
        heapify(nums, len_nums, i)

    for i in range(len_nums - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)

    return nums

if __name__ == "__main__":
    print(heapSort([5, 4, 8, 1, 3, 2, 9, 6, 7]))