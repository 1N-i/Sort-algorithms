def bucketSort(nums):
    min_nums, max_nums = min(nums), max(nums)
    if min_nums == max_nums: return nums
    num_buckets = len(nums)
    buckets = [[] for _ in range(num_buckets)]
    range_bucket = (max_nums - min_nums) / num_buckets

    for num in nums:
        bucket_i = min(int((num - min_nums) / range_bucket), num_buckets - 1)
        buckets[bucket_i].append(num)

    ans = []
    for bucket in buckets:
        len_bucket = len(bucket)
        for i in range(1, len_bucket):
            key = bucket[i]
            j = i - 1
                        
            while j >= 0 and bucket[j] > key:
                bucket[j + 1] = bucket[j]
                j -= 1
                            
            bucket[j + 1] = key
        ans.extend(bucket)

    nums[:] = ans
    return nums

if __name__ == "__main__":
    print(bucketSort([5, 4, 8, -1, -3, -2, 9, 6, 7]))