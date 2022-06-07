
# Given an array nums[] of size n, construct a Product Array P (of same size n) such
# that P[i] is equal to the product of all the elements of nums except nums[i].
#
# Input:
# n = 5
# nums[] = {10, 3, 5, 6, 2}
# Output:
# 180 600 360 300 900
# Explanation:
# For i=0, P[i] = 3*5*6*2 = 180.
# For i=1, P[i] = 10*5*6*2 = 600.
# For i=2, P[i] = 10*3*6*2 = 360.
# For i=3, P[i] = 10*3*5*2 = 300.
# For i=4, P[i] = 10*3*5*6 = 900.

# Compute product of all elements of array in from left and right in
# left(let) and right(let) array.Then start traversing from i = 0.
# For every element the answer will left(i-1) * right(i+1).
# Handle corner cases for first and last element.

def product_array(arr):
    if len(arr) == 1:
        return arr

    new_arr = [0] * len(arr)
    for item in range(len(arr)):
        temp = 1
        for new in range(len(arr)):
            if item != new:
                temp *= arr[new]
        new_arr[item] = temp

    return new_arr

assert [180,600,360,300,900] == product_array([10,3,5,6,2])

assert [180] == product_array([180])
assert [2,10] == product_array([10,2])

