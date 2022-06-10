def find_common_elements(arr1, arr2):
    arr_major = []
    arr_less = []
    commons = []
    if len(arr1) > len(arr2):
        arr_major = arr1
        arr_less = arr2
    else:
        arr_major = arr2
        arr_less = arr1

    for index in range(0,len(arr_major)):
        if arr_major[index] in arr_less:
            commons.append(arr_major[index])

    return sorted(commons)

assert [2, 4, 7, 8, 8] == find_common_elements([4,8,9,8,1,7,56,9,1,2], [8,4,2,19,87,6,23,7,5])
assert [2,2,3] == find_common_elements([3,4,2,2,4], [3,2,2,7,8])