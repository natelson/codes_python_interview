'''
Find the first non-repeating element in a given array arr of N integers.
Note: Array consists of only positive and negative integers and not zero.

Example 1:

Input : arr[] = {-1, 2, -1, 3, 2}
Output : 3
Explanation:
-1 and 2 are repeating whereas 3 is
the only number occuring once.
Hence, the output is 3.

An Efficient Solution is to use hashing.
1) Traverse array and insert elements and their counts in hash table.
2) Traverse array again and print first element with count equals to 1.
'''


def find_no_repeat_element(arr1):
    dict1 = {}
    for i in arr1:
        if i not in dict1:
            dict1[i] = 1
        else:
            dict1[i] += 1

    return [key for key, value in dict1.items() if value == 1]


assert [5,4] == find_no_repeat_element([1,1,2,3,3,5,4,2])
assert [3] == find_no_repeat_element([-1,2,-1,3,2])

assert [] == find_no_repeat_element([-1,2,-1,3,2,3])
