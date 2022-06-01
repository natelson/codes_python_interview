#Given a positive integerm N find the factorial of N.
#input
#N=5
#outupt
#120
#Explanation
#5*4*3*2*1=120


def factiorial(number):
    result = number
    for n in range(number-1,0,-1):
        result *=n

    return result


assert 120 == factiorial(5)
assert 720 == factiorial(6)
assert 0 == factiorial(0)
assert -1 == factiorial(-1)
assert 1 == factiorial(1)
