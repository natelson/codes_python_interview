'''
Given an unsorted array of size N, use selection sort to sort arr[] in increasing order.


Example 1:

Input:
N = 5
arr[] = {4, 1, 3, 9, 7}
Output:
1 3 4 7 9
Explanation:
Maintain sorted (in bold) and unsorted subarrays.
Select 1. Array becomes 1 4 3 9 7.
Select 3. Array becomes 1 3 4 9 7.
Select 4. Array becomes 1 3 4 9 7.
Select 7. Array becomes 1 3 4 7 9.
Select 9. Array becomes 1 3 4 7 9.

The algorithm maintains two subarrays in a given array.

1) The subarray which is already sorted.
2) Remaining subarray which is unsorted.

In every iteration of selection sort, the minimum element
(considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray.
'''


def select(arr, index):
    max = arr[0]
    idx = 0
    for i in range(1, index+1):
        if arr[i] > max:
            idx = i
            max = arr[i]

    return idx


def selectionSort(arr):
    for i in range(len(arr)-1,0,-1):
        j = select(arr, i)
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    return arr

assert [1,2,3,4,5] == selectionSort([4,5,1,2,3])