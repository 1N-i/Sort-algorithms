def pigeonHoleSortGenerator(nums):
    len_nums, min_num = len(nums), min(nums)
    if min_num < 0:
        for i in range(len_nums):
            nums[i] -= min_num

    max_num = max(nums)
    lockers = [[] for _ in range(max_num + 1)]

    for i, num in enumerate(nums):
        lockers[num].append(num)

        if min_num < 0:
            yield [x + min_num for x in nums], i, None
        else:
            yield nums, i, None

    nums_id = 0
    for lockers_id in range(len(lockers)):
        if lockers[lockers_id] == []: continue
        for num in lockers[lockers_id]:
            nums[nums_id] = num
            if min_num < 0:
                yield [x + min_num for x in nums], nums_id, lockers_id
            else:
                yield nums, nums_id, lockers_id

            nums_id += 1

    if min_num < 0:
        for i in range(len_nums):
            nums[i] += min_num

    return nums

if __name__ == "__main__":
    nums = [5, 4, 8, -1, -3, -2, 9, 6, 7]
    for state, i1, i2 in pigeonHoleSortGenerator(nums):
        print(f"Idx {i1} and {i2}: {state}")