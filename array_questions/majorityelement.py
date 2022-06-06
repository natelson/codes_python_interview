


def list_of_candidates(arr):
    candidate = -1
    uniques = list(set(arr))
    best_candidate = 0
    for i in range(len(uniques)):
        count = arr.count(uniques[i])
        if count >= len(arr)/2:
            if count > best_candidate:
                candidate = uniques[i]
                best_candidate = count

    return candidate

assert 3 == list_of_candidates([3,2,1,2,3,3,4,3,3])
assert 5 == list_of_candidates([5,1,5,5,2])


