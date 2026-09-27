def timSort(nums):
    def insertion_sort_slice(slice, left, right):
        for i in range(left + 1, right + 1):
            key = slice[i]
            j = i - 1
                
            while j >= left and slice[j] > key:
                slice[j + 1] = slice[j]
                j -= 1 
            slice[j + 1] = key
                
        return slice

    def merge_slice(slice, left, mid, right):
        if len(slice) <= 1: return slice
        
        slice_left = slice[left : mid + 1]
        slice_right = slice[mid + 1 : right + 1]
        merged = []

        left_i, right_i = 0, 0
        while left_i < len(slice_left) and right_i < len(slice_right):
            if slice_left[left_i] < slice_right[right_i]:
                merged.append(slice_left[left_i])
                left_i += 1
            else:
                merged.append(slice_right[right_i])
                right_i += 1

        merged.extend(slice_left[left_i:])
        merged.extend(slice_right[right_i:])
        slice[left : right + 1] = merged
        
        return slice

    len_nums = len(nums)
    min_run = 32
    left = 0
    right = min(left + min_run - 1, len(nums) - 1)
    for i in range(0, len_nums, min_run):
        right = min(i + min_run - 1, len_nums - 1)
        insertion_sort_slice(nums, i, right)

    size = min_run
    while size < len_nums:
        for left in range(0, len_nums, 2 * size):
            mid = min(left + size - 1, len_nums - 1)
            right = min(left + 2 * size - 1, len_nums - 1)

            if mid < right:
                nums = merge_slice(nums, left, mid, right)
        size *= 2

    return nums

if __name__ == "__main__":
    print(timSort([5, 4, 8, -1, -3, -2, 9, 6, 7]))