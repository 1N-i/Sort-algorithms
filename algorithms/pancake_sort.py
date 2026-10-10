def pancakeSort(nums):    
    len_nums = len(nums)

    for i in range(len_nums):
        max_i = len_nums - i - 1
        for j in range(len_nums - i):
            if nums[j] > nums[max_i]:
                max_i = j

        end = len_nums - i - 1
        if max_i != end and max_i != 0:
            nums[:max_i + 1] = nums[:max_i + 1][::-1] #Flip
        if max_i != end:
            nums[:end + 1] = nums[:end + 1][::-1]     #Flip

    return nums

if __name__ == "__main__":
    print(pancakeSort([5, 4, 8, -1, -3, -2, 9, 6, 7]))