

# Given a sorted array A[] of size N show how many unduplicated elements there are
# Note: Don't use set or HashMap to solve the problem.
#
# Input:
# N = 5
# Array = {2, 2, 2, 3, 3}
# Output: 2
# Explanation: After removing all the duplicates
# only one instance of 2 will remain.

def remove_duplicates_without_map(arr):
    new_arr = []
    for j in range(len(arr)):
        if arr[j] not in new_arr:
            new_arr.append(arr[j])

    return new_arr


def remove_duplicates_with_hashmap(arr):
    return list(set(arr))

assert [1, 3, 5, 8] == remove_duplicates_without_map([1,1,3,5,8,3])



