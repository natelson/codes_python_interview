# Given a number N. Find the last two digits of the Nth fibonacci number.
# Note: If the last two digits are 02, return 2.
# The last two digits of a fibonacci number repeats after an interval of 300 i.e
# the 1000th and 1300th fibonacci numbers have the same last two digits.
# Input:
# N = 13
# Output:
# 33
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,144,233


def fibonnaciDigit(number):
    before_number = (0,1)
    result = 0
    for i in range(number):
        result = before_number[0] + before_number[1]
        before_number = (before_number[1], result)

    if len(str(result)) >= 2:
        return int(str(result)[-2:])
    else:
        return result


assert 33 == fibonnaciDigit(12)
assert 8 == fibonnaciDigit(5)


