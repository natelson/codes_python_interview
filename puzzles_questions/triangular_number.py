# Given a number N.Check whether it is a triangular number or not.
# Note: A number is termed as a triangular number if we can represent it in the
# form of a triangular grid of points such that the points form an equilateral
# triangle and each row contains as many points as the row number, i.e., the first
# row has one point, the second row has two points, the third row has three points and so on.
# The starting triangular numbers are 1, 3 (1+2), 6 (1+2+3), 10 (1+2+3+4).
# Input:
# N=55
# Output:
# 1


def isTriangularNumber(number):
    result = 0
    for i in range(1,number-1):
        result += i
        if result == number:
            return True

    return False


assert True == isTriangularNumber(10)
assert False == isTriangularNumber(7)
assert True == isTriangularNumber(55)
assert False == isTriangularNumber(11)


