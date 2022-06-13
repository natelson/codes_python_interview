'''
The task is to complete the insert() function which is used to implement Insertion Sort.


Example 1:

Input:
N = 5
arr[] = { 4, 1, 3, 9, 7}
Output:
1 3 4 7 9


 Hint 2
 Full Solution
Algorithm
To sort an array of size n in ascending order:
1: Iterate from arr[1] to arr[n-1] over the array.
2: Compare the current element (key) to its predecessor.
3: If the key element is smaller than its predecessor,
compare it to the elements before. Move the greater elements
one position up to make space for the swapped element.
'''


def insert(arr, index):
    currValue = arr[index]
    position = index

    while position > 0 and arr[position-1] > currValue:
        arr[position] = arr[position-1]
        position = position-1

    arr[position] = currValue
    return arr

def insertionSort(arr):
    for index in range(1,len(arr)):
        insert(arr, index)

    return arr


assert [1,2,3,4,5] == insertionSort([4,5,1,2,3])