#For a given number N check if it is prime or not
# A prime number is a number wich is only divisible by 1 and itself
def isprime(number):
    if number == 1:
        return False
    for i in range(2,number):
        if number % i == 0 and i != number:
            return False

    return True



assert True ==  isprime(3)
assert True == isprime(2)
assert False == isprime(4)
assert False == isprime(9)
assert True == isprime(23)
assert False == isprime(1)
assert True == isprime(0)
assert True == isprime(17)
