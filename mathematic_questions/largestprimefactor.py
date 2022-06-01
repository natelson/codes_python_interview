#Given a number N, the Task is to find the largest prime factor of that number
#input
# N = 5
# Output 5
#Explanation
# 5 has 1 prive factor, only 5


def primefactor(number):
    multiply = 2
    while(multiply*multiply) < number:
        if number%multiply == 0:
            number = number//multiply
        else:
            multiply += 1

    return number


assert 5 == primefactor(5)
assert 3 == primefactor(24)
assert 7 == primefactor(7)
assert 23 == primefactor(46)
