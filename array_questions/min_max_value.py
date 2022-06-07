# Given an array A of size N of integers. Your task is to find the minimum and maximum elements in the array.
#
# Input:
# N = 6
# A[] = {3, 2, 1, 56, 10000, 167}
# Output:
# min = 1, max =  10000


def getMinMax(arr, n):
    minimum, maximum = min(arr[:n]), max(arr[:n])

    return minimum, maximum


assert (1,110) == getMinMax([5,8,110,1,22,54], 6)

assert (5,110) == getMinMax([5,8,110,1,22,54], 3)