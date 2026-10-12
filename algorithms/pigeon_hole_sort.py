def pigeonHoleSort(nums):
    len_nums, min_num = len(nums), min(nums)
    if min_num < 0:
        for i in range(len_nums):
            nums[i] -= min_num
        
    max_num = max(nums)
    lockers = [[] for _ in range(max_num + 1)]

    for num in nums:
        lockers[num].append(num)

    nums_id = 0
    for lockers_id in range(len(lockers)):
        if lockers[lockers_id] == []: continue
        for num in lockers[lockers_id]:
            nums[nums_id] = num
            nums_id += 1

    if min_num < 0:
        for i in range(len_nums):
            nums[i] += min_num

    return nums

if __name__ == "__main__":
    print(pigeonHoleSort([5, 4, 8, -1, -3, -2, 9, 6, 7]))