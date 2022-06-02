

def getMinMax(arr, n):
    minimum, maximum = min(arr[:n]), max(arr[:n])

    return minimum, maximum


assert (1,110) == getMinMax([5,8,110,1,22,54], 6)

assert (5,110) == getMinMax([5,8,110,1,22,54], 3)