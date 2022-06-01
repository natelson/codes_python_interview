#consider a sample space S consisting of all perfect squares starting
# from 1(1x1) , 4(2x2), 9(3X3). You are given a number N, you have to ouptut
#the number of integers less than N in the sampel S

#input
#N = 9
# outuput
#2
import math


def countspaces(number):
    answear = int(math.sqrt(number-1))
    return answear


def countspaces_manualy(number):
    answear = 0
    for i in range(1,number):
        if i*i < number:
            answear+=1
    return answear

assert 2 == countspaces(9)
assert 2 == countspaces_manualy(9)
assert 3 == countspaces(10)
assert 3 == countspaces_manualy(10)


