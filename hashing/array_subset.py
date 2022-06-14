'''
Given two arrays: a1[0..n-1] of size n and a2[0..m-1] of size m.
Task is to check whether a2[] is a subset of a1[] or not.
Both the arrays can be sorted or unsorted. It may be assumed that elements in both array are distinct.


Example 1:

Input:
a1[] = {11, 1, 13, 21, 3, 7}
a2[] = {11, 3, 7, 1}
Output:
Yes
Explanation:
a2[] is a subset of a1[]

Create a Hash Table for all the elements of arr1[].
Traverse arr2[] and search for each element of arr2[] in the Hash Table.
If element is not found then return False.
If all elements are found then return True.

'''

def isSubset(arr1, arr2):
    s = set()
    for i in arr1:
        s.add(i)

    size_s = len(s)

    for i in arr2:
        s.add(i)

    if len(s) == size_s:
        return True
    else:
        return False



assert True == isSubset([4,7,8,9,1,2,3], [1,2,3])
assert False == isSubset([4,7,8,9,1,2,3], [1,2,3,10])