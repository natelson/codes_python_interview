'''
Given an array arr of size n and an integer X. Find if there's a triplet in
the array which sums up to the given integer X.


Example 1:

Input:
n = 6, X = 13
arr[] = [1 4 45 6 10 8]
Output:
1
Explanation:
The triplet {1, 4, 8} in
the array sums up to 13.

Sort the given array.
Loop over the array and fix the first element of the possible triplet, arr[i].
Then fix two pointers, one at i + 1 and the other at n – 1. And look at the sum,
If the sum is smaller than the required number, increment the first pointer.
Else, If the sum is bigger, decrease the end pointer to reduce the sum.
Else, if the sum of elements at two-pointer is equal to given number return true.
'''

def have_a_triple_sum(arr, number):
    for i in range(0,len(arr)):
        left = i + 1
        right = len(arr) -1
        way = 'right'
        while left < right:
            curr_sum = arr[i] + arr[left] + arr[right]
            if curr_sum == number:
                return True

            if way == 'right' and left < right:
                right -= 1

            if way == 'right' and left == right:
                right = len(arr) -1
                way = 'left'

            if way == 'left':
                both = True
                left += 1

    return False

assert True == have_a_triple_sum([1,4,45,6,10,8], 13)
assert True == have_a_triple_sum([1,4,45,6,10,8], 19)
assert False == have_a_triple_sum([1,4,45,6,10,8], 9)
assert True == have_a_triple_sum([1,4,45,6,10,8], 18)
assert True == have_a_triple_sum([1,4,45,6,10,8], 24)