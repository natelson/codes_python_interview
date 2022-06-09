def find_transition_point(arr):
    for index in range(0, len(arr)):
        if arr[index] == 1:
            return index

    return -1


def find_transition_point_binary_search(arr):
    if arr[0] == 1:
        return 0
    start = 0
    end = len(arr)
    while(start < end):
        midle = (start+end)//2
        if arr[midle] == 0:
            start = midle + 1
        elif arr[midle] == 1:
            if arr[midle-1] == 0:
                return midle
            else:
                end = midle

    return -1


assert 3 == find_transition_point([0, 0, 0, 1, 1])
assert -1 == find_transition_point([0, 0, 0, 0, 0])

assert 3 == find_transition_point_binary_search([0, 0, 0, 1, 1])
assert -1 == find_transition_point_binary_search([0, 0, 0, 0, 0])
