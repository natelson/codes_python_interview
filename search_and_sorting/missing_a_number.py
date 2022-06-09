def get_missing_numbers(arr, size):
    result = []
    if len(arr) == size:
        return result

    arr = sorted(arr)
    i = 1
    for index in range(0, len(arr)):
        if arr[index] != i:
            result.append(i)

        if len(result) + len(arr) == size:
            return  result

        i+=1

    return result


print(get_missing_numbers([1,2,3,5], 5))


