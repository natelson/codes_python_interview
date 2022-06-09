def get_small_missing_number(arr):
    # order array
    arr = sorted(arr)
    i = 0
    for item in range(0, len(arr)):
        if arr[item] != i:
            return i
        i += 1

    return i


assert 7 == get_small_missing_number([0, 1, 2, 3, 4, 5, 6])
assert 5 == get_small_missing_number([0, 1, 2, 3, 4, 6])
assert 0 == get_small_missing_number([-1, 1, 2, 3, 4, 6])
