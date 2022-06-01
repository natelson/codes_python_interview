#Given two number A and B, The task is to find out their LCM and GCD
#LCM is smallest divisible by all the given numbers

#HCF/GCD is the largest number that can be divided all the given numbers

#LCM = a*b/HCF
#input
#a = 14, B = 8
#output
#56 2
#Explanation
#LCM of 14 and 8 is 56, while
#thier GCD is 2
import math


def lcmandgc(a, b):
    gcd = math.gcd(a,b)
    lcm = (a*b)//gcd
    return lcm, gcd


assert (56,2) == lcmandgc(14,8)
assert (108,3) == lcmandgc(12,27)

