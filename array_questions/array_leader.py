

def list_leaders_array(arr):
    leaders = []
    for i in range(len(arr)-1):
        if arr[i] > sum(arr[i+1:]):
            leaders.append(arr[i] )

    leaders.append(arr[-1])
    return leaders


assert [5,3,1] == list_leaders_array([1,2,5,3,1])

assert [17,5,2] == list_leaders_array([16,17,4,3,5,2])
