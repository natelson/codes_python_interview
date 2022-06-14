# Given two arrays A and B of equal size N, the task is to find if given arrays are equal or not.
# Two arrays are said to be equal if both of them contain same set of elements, arrangements (or permutation)
# of elements may be different though.
# Note : If there are repetitions, then counts of repeated elements must also be same for two array to be equal.
#
# Example 1:
#
# Input:
# N = 5
# A[] = {1,2,5,4,0}
# B[] = {2,4,5,0,1}
# Output: 1
# Explanation: Both the array can be
# rearranged to {0,1,2,4,5}

def check_equility(arr1, arr2):
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)
    if arr1 == arr2:
        return True
    else:
        return False


def check_equility_with_dict(arr1, arr2):
    dict1 = {}
    for i in arr1:
        if i not in dict1:
            dict1[i] = 1
        else:
            dict1[i] +=1

    for i in arr2:
        if i not in dict1:
            return False
        else:
            dict1[i] -=1

    if sum(dict1.values()) > 0:
        return False
    return True



assert False == check_equility([1,5,4,3,2,0],[0,1,2,3,4,5,6])
assert True == check_equility([1,5,4,3,2,0],[0,1,2,3,4,5])

assert False == check_equility_with_dict([1,5,4,3,2,0],[0,1,2,3,4,5,6])
assert True == check_equility_with_dict([1,5,4,3,2,0],[0,1,2,3,4,5])