'''
Given an array Arr of N positive integers and another number X.
Determine whether or not there exist two elements in Arr whose sum is exactly X.

Example 1:

Input:
N = 6, X = 16
Arr[] = {1, 4, 45, 6, 10, 8}
Output: Yes
Explanation: Arr[3] + Arr[4] = 6 + 10 = 16

hasArrayTwoCandidates (A[], ar_size, sum)
Sort the array in non-decreasing order.
Initialize two index variables to find the candidate
elements in the sorted array.
Initialize first to the leftmost index: l = 0
Initialize second the rightmost index: r = ar_size-1
Loop while l < r.
If (A[l] + A[r] == sum) then return 1
Else if( A[l] + A[r] < sum ) then l++
Else r–
No candidates in whole array – return 0
'''

def exist_sum_number(arr, number):
    for i in range(0,len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == number :
                return True


    return False

assert True == exist_sum_number([1,4,45,6,10,8], 16)
assert False == exist_sum_number([1,4,45,6,10,8], 13)
assert True == exist_sum_number([1,4,45,6,10,8], 18)