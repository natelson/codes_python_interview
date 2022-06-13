# Given a binary array A[] of size N.The task is to arrange the
# array in increasing order. Note: The binary array contains only 0 and 1.
#
# Input:
# 5
# 1 0 1 1 0
#
# Output:
# 0 0 1 1 1
#Algorithm
# Segregated approach
# Run a loop till left index is smaller than or equal to right index.
# For every iteration:
# If element at left index is 0, increase the left index.
# Else If element at high index is 1, decrease the right index.
# Else, swap the elements at left and right index and update the left and right index.
#
#

def binary_sorting(arr):
    right = len(arr)
    left = 0
    new_arr = []
    for i in range(0,len(arr)):
        if arr[i] == 0:
            new_arr.append(arr[i])

    for i in range(0,len(arr)):
        if arr[i] == 1:
            new_arr.append(arr[i])

    return new_arr

print(binary_sorting([1,1,0,1,0,1,0,1]))