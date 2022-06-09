'''
Given a alphanumeric string S, extract maximum numeric value from S.

Example 1:

Input:
S = 100klh564abc365bg
Output: 564
Explanation: Maximum numeric value
among 100, 564 and 365 is 564.
'''

def extract_max_number(string):
    numbers = '0123456789'
    list_numbers = []
    temp_number = ''
    for character in string:
        if character in numbers:
            temp_number += character
        else:
            if temp_number != '':
                list_numbers.append(int(temp_number))
                temp_number = ''

    if temp_number != '':
        list_numbers.append(int(temp_number))

    if len(list_numbers) > 0:
        return max(list_numbers)
    else:
        return -1


assert 987 == extract_max_number('100klh564abc300n24rt89f987')
assert 564 == extract_max_number('100klh564abc300n24rt89fabc')
assert -1 == extract_max_number('dfdfffklhfddsfabcfddnfsdfrtfdfabc')
assert 0 == extract_max_number('dfdfffkl0hfddsfabcfddnfsdfrtfdfabc')

