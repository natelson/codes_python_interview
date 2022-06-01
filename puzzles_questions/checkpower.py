#Given two positive numbers X and Y, check if Y is power of X

#input
# x =2, y = 8
#outupt
#true
# Explantion
# 2^3 is equal to 8


def checkPower(x,y):
    for i in range(y):
        if x**i == y:
            return True

    return False


assert True == checkPower(2,8)
assert True == checkPower(2,16)
assert True == checkPower(3,27)
assert True == checkPower(1,1)

