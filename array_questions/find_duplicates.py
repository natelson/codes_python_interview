'''
# Given an array a[] of size N which contains elements
# from 0 to N-1, you need to find all the elements occurring more than once in the given array.

# Input:
# N = 5
# a[] = {2,3,1,2,3}
# Output: 2 3
# Explanation: 2 and 3 occur more than once
# in the given array.
'''

def find_duplicates(arr):
    duplicates = []

    uniques = set(arr)
    for item in uniques:
        if arr.count(item) > 1:
            duplicates.append(item)

    return duplicates


assert [2,3] == find_duplicates([2,3,1,2,3])

assert [5] == find_duplicates([5,5,1,2,5])

assert [1,2,3,4,5] == find_duplicates([1,5,4,3,2,2,3,4,5,1])