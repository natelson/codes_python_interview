'''
Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.


Example 1:

Input:
N = 5
arr[]= {0 2 1 2 0}
Output:
0 0 1 2 2
Explanation:
0s 1s and 2s are segregated
into ascending order.
'''


def sort_array(arr):
    order = [0,1,2]
    new_arr = []
    for i in range(0,len(order)):
        for index in range(0,len(arr)):
            if arr[index ] == order[i]:
                new_arr.append(arr[index])

    return new_arr


assert [0, 0, 0, 1, 1, 1, 1, 2, 2, 2] == sort_array([2,0,1,2,1,0,1,1,0,2])