#Given two numbers A and B, find kth digit from right A^B
#Example
#input
#A = 3
# B = 3
#k  =1
#Output
#7
#explanation
#3^3 = 27 and 1st digit from right is 7


def k_digit(a, b, k):
    result = a ** b
    if k > len(str(result)):
        return 0
    else:
        return int(str(result)[-k])


def k_digit_only_number(a, b, k):
    result = a ** b
    temp = 0
    while(k >0):
        temp = result%10
        result = result//10
        k-=1
    return temp

assert 7 == k_digit(3,3,1)
assert 9 == k_digit(5345,342,5)
assert 0 == k_digit(3,3,3)

assert 7 == k_digit_only_number(3,3,1)
assert 9 == k_digit_only_number(5345,342,5)
assert 0 == k_digit_only_number(3,3,3)
