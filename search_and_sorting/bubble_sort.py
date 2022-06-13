# Given an Integer N and a list arr. Sort the array using bubble sort algorithm.
# Example 1:
#
# Input:
# N = 5
# arr[] = {4, 1, 3, 9, 7}
# Output:
# 1 3 4 7 9
#
# To sort an array in increasing order in Bubble Sort, we move the greatest element at the
# end in first pass.  To do this we compare adjacent elements.
#
# In one pass, we compare every element to its next.  If next element is smaller,
# we swap them else we do nothing.

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


assert [4, 5, 7, 8] ==  bubble_sort([8,7,5,4])
assert [1,2,4,6,7,8] ==  bubble_sort([4,7,8,2,1,6])



