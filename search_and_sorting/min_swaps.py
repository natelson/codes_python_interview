'''
Given an array of n distinct elements. Find the minimum number
of swaps required to sort the array in strictly increasing order.


Example 1:

Input:
nums = {2, 8, 5, 4}
Output:
1
Explaination:
swap 8 with 4.
'''

def minSwaps(nums):

    #Initialization
    n = len(nums)
    cur = []

    for i in range(n):

        cur.append([nums[i], i])

    cur.sort()

    vis = [False for i in range(n)]
    ans = 0
    for i in range(n):

        if(vis[i] or cur[i][1] == i):
            continue
        else:
            cycle_size = 0
            j = i

            while(vis[j] == False):
                vis[j] = True
                j = cur[j][1]
                cycle_size = cycle_size +1

            ans = ans+ max(0, cycle_size-1)
    return ans

assert 2 == minSwaps([10,19,6,3,5])
assert 1 == minSwaps([2,4,8,5])












