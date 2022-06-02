



def remove_duplicates_without_map(arr):
    new_arr = []
    for j in range(len(arr)):
        if arr[j] not in new_arr:
            new_arr.append(arr[j])

    return new_arr


def remove_duplicates_with_hashmap(arr):
    return list(set(arr))

assert [1, 3, 5, 8] == remove_duplicates_without_map([1,1,3,5,8,3])



