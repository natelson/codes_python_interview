# Given an array A of N elements. Find the majority element in the array.
# A majority element in an array A of size N is an element that appears more than N/2 times in the array.
# #Input:
# N = 5
# A[] = {3,1,4,3,2}
# Output:
# 3
# Explanation:
# Since, 3 is present more
# than N/2 times, so it is
# the majority element.

#1. Traverse the array to find the maximum element
#2. Check if that element appears more than N/2 times.



def list_of_candidates(arr):
    candidate = -1
    uniques = list(set(arr))
    best_candidate = 0
    for i in range(len(uniques)):
        count = arr.count(uniques[i])
        if count >= len(arr)/2:
            if count > best_candidate:
                candidate = uniques[i]
                best_candidate = count

    return candidate

assert 3 == list_of_candidates([3,2,1,2,3,3,4,3,3])
assert 5 == list_of_candidates([5,1,5,5,2])


