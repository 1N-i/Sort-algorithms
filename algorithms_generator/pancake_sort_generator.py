def pancakeSortGenerator(nums):    
    len_nums = len(nums)

    for i in range(len_nums):
        max_i = len_nums - i - 1
        for j in range(len_nums - i):
            yield nums, j, max_i
            if nums[j] > nums[max_i]:
                max_i = j

        end = len_nums - i - 1
        if max_i != end and max_i != 0:
            nums[:max_i + 1] = nums[:max_i + 1][::-1] #Flip
            yield nums, 0, max_i
        if max_i != end:
            nums[:end + 1] = nums[:end + 1][::-1]     #Flip
            yield nums, 0, end

    return nums

if __name__ == "__main__":
    nums = [5, 4, 8, -1, -3, -2, 9, 6, 7]
    for state, i1, i2 in pancakeSortGenerator(nums):
        print(f"Idx {i1} and {i2}: {state}")