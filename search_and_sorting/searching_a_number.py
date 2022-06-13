# Given an array Arr of N elements and a integer K. Your task is to return the position
# of first occurence of K in the given array.
# Note: Position of first element is considered as 1.
#
# Example 1:
#
# Input:
# N = 5, K = 16
# Arr[] = {9, 7, 2, 16, 4}
# Output: 4
# Explanation: K = 16 is found in the
# given array at position 4.

def get_position_the_number(arr, number):
    for index in range(len(arr)):
        if number == arr[index]:
            return index+1

    return -1



assert 5 == get_position_the_number([5,3,2,6,7,-5,28], 7)