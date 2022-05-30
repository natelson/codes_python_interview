#given the first 2 terms A1 and A2 of an Arithmetic Series. Find the Nth term of the series. Find the Nth term of the series
#input
#A1 = 2
#A2 = 4
#N = 4
#Output
# 8

def define_list(start, step, size):
    list_number = list(range(start, size+1, step))
    return list_number


def seriesAp(A1, A2, N):
    step = A2 - A1
    size = step * N
    list_numbers = define_list(A2, step, size)
    return list_numbers[-1]


nTerm = seriesAp(2,4,25)

