'''
Given two integer arrays A1[ ] and A2[ ] of size N and M respectively. Sort the first array A1[ ]
such that all the relative positions of the elements in the first array are the same as the elements in the second array A2[ ].
See example for better understanding.
Note: If elements are repeated in the second array, consider their first occurance only.

Example 1:

Input:
N = 11
M = 4
A1[] = {2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8}
A2[] = {2, 1, 8, 3}
Output:
2 2 1 1 8 8 3 5 6 7 9
Explanation: Array elements of A1[] are
sorted according to A2[]. So 2 comes first
then 1 comes, then comes 8, then finally 3
comes, now we append remaining elements in
sorted order.


Algorithm:

Store all the elements of first array in map.
Traverse over the second array and store all those elements which are present in map.
Iterate over the map and store the rest elements present in map.

'''

def bubble_sort(arr):
    n = 0
    for j in range(0,len(arr)-1):
        n +=1
        for i in range(len(arr)-j-1):
            if arr[i] > arr[i+1]:
                temp = arr[i+1]
                arr[i+1] = arr[i]
                arr[i] = temp
            n +=1

    return arr

def sort_array(arr1 , arr2):
    new_arr = []
    part_arr = []
    for i in range(0,len(arr2)):
        for index in range(0,len(arr1)):
            if arr1[index] == arr2[i]:
                new_arr.append(arr1[index])

    for i in range(0,len(arr1)):
        if arr1[i] not in arr2:
            part_arr.append(arr1[i])



    return new_arr + bubble_sort(part_arr)


assert [8, 9, 4, 4, 1, 2, 5] == sort_array([1,4,5,8,9,2,4], [8,9,4])