


def product_array(arr):
    if len(arr) == 1:
        return arr

    new_arr = [0] * len(arr)
    for item in range(len(arr)):
        temp = 1
        for new in range(len(arr)):
            if item != new:
                temp *= arr[new]
        new_arr[item] = temp

    return new_arr

assert [180,600,360,300,900] == product_array([10,3,5,6,2])

assert [180] == product_array([180])
assert [2,10] == product_array([10,2])

