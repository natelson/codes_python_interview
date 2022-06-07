# Given an unsorted array arr[] of size N, rotate it by D elements (clockwise).
#
# Input:
#  N denoting the size
# of the array and an integer D denoting the number size of the rotation. Subsequent
# line will be the N space separated array elements.

# Output:
# For each testcase, in a new line, output the rotated array.
#
# Constraints:
# 1 <= N <= 107
# 1 <= D <= N
# 0 <= arr[i] <= 105

#Example:
#5
#2
#1 2 3 4 5

def rotate_array(array: list, rotates: int) -> list:
    new_array = [0] * len(array)
    for i in range(len(array)):
        new_position = i - rotates
        new_array[new_position] = array[i]

    return new_array


assert [3, 4, 5, 1, 2] == rotate_array([1, 2, 3, 4, 5], 2)
assert [1, 2, 3, 4, 5] == rotate_array([1, 2, 3, 4, 5], 5)
