# # You are given an array A, of N elements.
# Find minimum index based distance between two elements of the array, x and y.
# Input:
# N = 4
# A[] = {1,2,3,2}
# x = 1, y = 2
# Output: 1
# Explanation: x = 1 and y = 2. There are
# two distances between x and y, which are
# 1 and 3 out of which the least is 1.
def minimum_distance_array(arr, x, y):
    position_x = -1
    position_y = -1
    minimum_distance = len(arr)
    for i in range(0,len(arr)):
        if x in arr[i:] and arr[i:].index(x) > (position_x + i):
            position_x = arr[i:].index(x) + i

        for j in range(position_x,len(arr)):
            if y in arr[j:]:
                position_y = arr[j:].index(y) + j
                if (position_y - position_x) < minimum_distance:
                    minimum_distance = position_y - position_x

    return minimum_distance

assert 1 == minimum_distance_array([1,4,3,2,5,6,1,2], 1,2)
assert 3 == minimum_distance_array([1,4,3,2,5,6,2,1], 1,2)


