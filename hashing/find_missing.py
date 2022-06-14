'''
Given two arrays A and B contains integers of size N and M,
the task is to find numbers which are present in the first array, but not present in the second array.

Example 1:

Input: N = 6, M = 5
A[] = {1, 2, 3, 4, 5, 10}
B[] = {2, 3, 1, 0, 5}
Output: 4 10
Explanation: 4 and 10 are present in
first array, but not in second array.
add()
append()
#Array: same type of element, Repeating is possible
#Set: Same type of element, Repeating is prohibited
'''

def find_missing(arr1, arr2):
    s = set(arr2)
    ans = []
    for i in arr1:
        if i not in s:
            ans.append(i)


    return ans


assert [] == find_missing([1,5,4,3,2,0],[0,1,2,3,4,5,6])
assert [8,11] == find_missing([1,5,4,3,2,0,8,11],[0,1,2,3,4,5,6])
