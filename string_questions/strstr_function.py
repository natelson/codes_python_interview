'''
Your task is to implement the function strstr.
The function takes two strings as arguments (s,x) and
locates the occurrence of the string x in the string s.
The function returns and integer denoting the first occurrence of the string x in s (0 based indexing).

Note: You are not allowed to use inbuilt function.

Input:
s = ProgramingDoesGood, x = Does
Output: 10
'''


def strstr(string, pattern):
    len_pattern = len(pattern)
    for i in range(0,len(string)):
        if (i + len_pattern) > len(string):
            return -1
        if string[i:len_pattern+i] == pattern:
            return i

    return -1


assert 0 == strstr('ProgramingisGoodForEverwone', 'Pro')
assert 12 == strstr('ProgramingisGoodForEverwone', 'Good')
assert 24 == strstr('ProgramingisGoodForEverwone', 'one')