def countingSortGenerator(nums):
    min_num, max_num = min(nums), max(nums)
    if min_num == max_num:
        yield nums, None, None
        return
    
    count = [0] * ((max_num + 1) - min_num)

    for i, num in enumerate(nums):
        count[num - min_num] += 1

        yield nums, i, None

    write_i = 0
    for i in range(len(count)):
        qtd_num = count[i]
        if qtd_num == 0: continue

        val = i + min_num
        for j in range(count[i]):
            nums[write_i] = val
            yield nums, write_i, None
            write_i += 1

    return nums

if __name__ == "__main__":
    nums = [5, 4, 8, -1, -3, -2, 9, 6, 7]
    for state, i1, i2 in countingSortGenerator(nums):
        print(f"Idx {i1} and {i2}: {state}")