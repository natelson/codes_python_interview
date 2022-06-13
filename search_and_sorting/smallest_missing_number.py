# You are given an array arr[] of N integers including 0.
# The task is to find the smallest positive number missing from the array.
#
# Example 1:
#
# Input:
# N = 5
# arr[] = {1,2,3,4,5}
# Output: 6
# Explanation: Smallest positive missing
# number is 6.

#Function that returns the smallest possible number from
#an array of positive numbers

def get_small_missing_number(arr):
    # order array
    arr = sorted(arr)
    i = 0
    for item in range(0, len(arr)):
        if arr[item] != i:
            return i
        i += 1

    return i


assert 7 == get_small_missing_number([0, 1, 2, 3, 4, 5, 6])
assert 5 == get_small_missing_number([0, 1, 2, 3, 4, 6])
assert 0 == get_small_missing_number([-1, 1, 2, 3, 4, 6])
