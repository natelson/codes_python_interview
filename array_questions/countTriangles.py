


def count_possible_tringles(arr):
    arr.sort()
    count = 0
    print(arr)
    for first_element in range(len(arr) - 2):
        for i in range(first_element+1, len(arr) - 1):
            print(arr[first_element], arr[i], arr[i+1])
            if arr[first_element] + arr[i] >  arr[i+1]:
                count+=1


    return count


assert 1 == count_possible_tringles([3,4,5,1])
assert 6 == count_possible_tringles([6,4,9,7,8])



