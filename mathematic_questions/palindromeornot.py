#Given the number N. If the digit sum(or sum of digits) of N is a Palindrome or not.
#Note: A palindrone number is a number wich stays the same when reversed. Example: 123,321,7 etc.

#Input
#56
#Output
#1
#xplanation:
#The digit of sum of 56 is 5+6=11
#Since 11 is a palindrome number. This answear is 1

def number_is_palindrome(N):
    sum_of_digit = 0
    for digit in str(N):
        sum_of_digit += int(digit)

    if str(sum_of_digit) == str(sum_of_digit)[::-1]:
        return 1
    else:
        return 0



