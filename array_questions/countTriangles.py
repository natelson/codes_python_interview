# Given an unsorted array arr[] of n positive integers.
# Find the number of triangles that can be formed with three
#     different array elements as lengths of three sides of triangles.
# Input:
# n = 3
# arr[] = {6,4,9,7,8}
# Output:
# 10
# Explanation:
# A triangle is possible
# with all the elements 5, 3 and 4.
#1. Sort the elements of the array. Sorting would help you to maintain the condition that  for any three sides of  the triangle  a,b and c ,
#
#    max(a,b) <=c.
#
# 2. Now, traverse for each pair of element in the array and make the count of triplets such that (a+b)>c.

def count_possible_tringles(arr):
    arr.sort()
    count = 0
    for first_element in range(len(arr) - 2):
        for i in range(first_element+1, len(arr) - 1):
            if arr[first_element] + arr[i] >  arr[i+1]:
                count+=1


    return count


assert 1 == count_possible_tringles([3,4,5,1])
assert 6 == count_possible_tringles([6,4,9,7,8])



