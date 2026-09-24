def bucketSortGenerator(nums):
    min_nums, max_nums = min(nums), max(nums)
    if min_nums == max_nums:
        yield nums, None, None
        return

    num_buckets = len(nums)
    buckets = [[] for _ in range(num_buckets)]
    range_bucket = (max_nums - min_nums) / num_buckets

    for idx, num in enumerate(nums):
        bucket_i = min(int((num - min_nums) / range_bucket), num_buckets - 1)
        buckets[bucket_i].append(num)

        placed_elements = [elem for bucket in buckets for elem in bucket]
        unplaced_elements = nums[idx + 1:]
        
        nums[:] = placed_elements + unplaced_elements
        curr_pos = len(placed_elements) - 1
        yield nums, curr_pos, idx

    offset = 0

    for bucket in buckets:
        len_bucket = len(bucket)
        for i in range(1, len_bucket):
            key = bucket[i]
            j = i - 1

            yield nums, offset + j, offset + i

            while j >= 0 and bucket[j] > key:
                bucket[j + 1] = bucket[j]
                j -= 1

                nums[:] = [elem for b in buckets for elem in b]
                yield nums, offset + j + 1, offset + j + 2

            bucket[j + 1] = key

            nums[:] = [elem for b in buckets for elem in b]
            yield nums, offset + j + 1, None

        offset += len_bucket

    nums[:] = [elem for b in buckets for elem in b]
    yield nums, None, None

if __name__ == "__main__":
    nums = [5, 4, 8, -1, -3, -2, 9, 6, 7]
    for state, i1, i2 in bucketSortGenerator(nums):
        print(f"Comparando índices {i1} e {i2}: {state}")