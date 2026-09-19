def countingSort(nums):
    min_num, max_num = min(nums), max(nums)
    if min_num == max_num: return nums
    count = [0] * ((max_num + 1) - min_num)

    for num in nums:
        count[num - min_num] += 1

    ans = []
    for i in range(len(count)):
        qtd_num = count[i]
        if qtd_num == 0: continue

        ans.extend([i + min_num] * qtd_num)

    nums[:] = ans
    return nums

if __name__ == "__main__":
    print(countingSort([5, 4, 8, -1, -3, -2, 9, 6, 7]))