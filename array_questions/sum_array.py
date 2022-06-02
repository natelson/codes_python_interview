


def sum_array(arr, n):
    if n > len(arr):
        n = len(arr)
    if n < 1:
        return 0

    return sum(arr[:n])


assert 10 == sum_array([5,4,1], 3)
assert 9 == sum_array([5,4,1], 2)
assert 5 == sum_array([5,4,1], 1)
assert 0 == sum_array([5,4,1], -1)