def bitonicSortGenerator(nums):

    return nums

if __name__ == "__main__":
    nums = [5, 4, 8, -1, -3, -2, 9, 6, 7]
    for state, i1, i2 in bitonicSortGenerator(nums):
        print(f"Idx {i1} and {i2}: {state}")