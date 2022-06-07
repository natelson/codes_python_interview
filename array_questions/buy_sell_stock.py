'''
The cost of stock on each day is given in an array A[] of size N.
Find all the days on which you buy and sell the stock so that in between those days your profit is maximum.
Note: There may be multiple possible solutions. Return any one of them.
Any correct solution will result in an output of 1, whereas wrong solutions will result in an output of 0.

Example 1:

Input:
N = 7
A[] = {100,180,260,310,40,535,695}
Output:
1
Explanation:
One possible solution is (0 3) (4 6)
We can buy stock on day 0,
and sell it on 3rd day, which will
give us maximum profit. Now, we buy
stock on day 4 and sell it on day 6.
'''

def findPositionBuySell(arr):
    buy_postion = -1
    for index in range(len(arr)):
        if index+1 < len(arr) and arr[index] < arr[index+1]:
            buy_postion = index
            break

    for index in range(buy_postion, len(arr)):
        sell_position = -1
        if index+1 < len(arr) and arr[index] > arr[index+1]:
            sell_position = index
            break


    if buy_postion == -1 or sell_position == -1:
        return []
    else:
        return [buy_postion, sell_position]


assert [0,3] == findPositionBuySell([10,180,260,310,40,535,695])
