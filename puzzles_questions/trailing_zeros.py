#For a integer N find the number of trailing zeros in N!
# Input
#N = 5
#Output
#1
#Explanation
#5! = 120 so the number of trailing zero is 1


def factorial(number):
    result = number
    for i in range(number-1,1,-1):
        result *= i

    return result


def get_trailing_zeros(number):
    result = factorial(number)
    return str(result).count('0')




assert 1 == get_trailing_zeros(5)
assert 1 == get_trailing_zeros(0)

