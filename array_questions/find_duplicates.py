

def find_duplicates(arr):
    duplicates = []

    uniques = set(arr)
    for item in uniques:
        if arr.count(item) > 1:
            duplicates.append(item)

    return duplicates


print(find_duplicates([2,3,1,2,3]))