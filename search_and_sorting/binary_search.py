def get_position_the_number_binary_search(arr, left, right, number):
    if left > right:
        return -1
    midle = (left+right)//2
    if number == arr[midle]:
        return midle
    elif number > arr[midle]:
        return get_position_the_number_binary_search(arr, midle+1, right, number)
    else:
        return get_position_the_number_binary_search(arr, left, midle-1, number)


def find_position(arr, number):
    arr = sorted(arr)
    return get_position_the_number_binary_search(arr, 0, len(arr)-1, number)


assert 2 == find_position([1,2,3,4,5,6,7,8,9,12],3)
assert 0 == find_position([1,2,3,4,5,6,7,8,9,12],1)
assert 1 == find_position([1,2,3,4,5,6,7,8,9,12],2)
