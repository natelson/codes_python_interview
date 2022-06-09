def get_position_the_number(arr, number):
    for index in range(len(arr)):
        if number == arr[index]:
            return index+1

    return -1



assert 5 == get_position_the_number([5,3,2,6,7,-5,28], 7)