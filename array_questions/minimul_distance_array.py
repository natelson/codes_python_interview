def minimum_distance_array(arr, x, y):
    position_x = -1
    position_y = -1
    minimum_distance = len(arr)
    for i in range(0,len(arr)):
        if x in arr[i:] and arr[i:].index(x) > (position_x + i):
            position_x = arr[i:].index(x) + i

        for j in range(position_x,len(arr)):
            if y in arr[j:]:
                position_y = arr[j:].index(y) + j
                if (position_y - position_x) < minimum_distance:
                    minimum_distance = position_y - position_x

    return minimum_distance

assert 1 == minimum_distance_array([1,4,3,2,5,6,1,2], 1,2)
assert 3 == minimum_distance_array([1,4,3,2,5,6,2,1], 1,2)


