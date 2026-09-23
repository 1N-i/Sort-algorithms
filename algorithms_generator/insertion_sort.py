def insertionSort(nums):
    len_nums = len(nums)
    
    for i in range(1, len_nums):
        key = nums[i]
        j = i - 1
        
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
            
        nums[j + 1] = key
        
    return nums

if __name__ == "__main__":
    print(insertionSort([5, 4, 8, -1, -3, -2, 9, 6, 7]))