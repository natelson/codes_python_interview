def rotate_array(array: list, rotates: int) -> list:
    new_array = [0] * len(array)
    for i in range(len(array)):
        new_position = i - rotates
        new_array[new_position] = array[i]

    return new_array


assert [3, 4, 5, 1, 2] == rotate_array([1, 2, 3, 4, 5], 2)
assert [1, 2, 3, 4, 5] == rotate_array([1, 2, 3, 4, 5], 5)
