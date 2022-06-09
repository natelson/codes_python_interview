'''
Given two strings A and B, find if A is a subsequence of B.

Input:
A = prgai
B = ilikeprogramming
Output: 1
Explanation: A is a subsequence of B.
'''
def exist_subsequence_any_position(string1, string2):
    if len(string2) < len(string1):
        return False

    for character in string1:
        if character not in string2:
            return False

    return True


def exist_subsequency_same_order(pattern, string2):
    len_pattern = len(pattern)
    for i in range(0, len(string2)):
        if i + len_pattern> len(string2):
            return False
        if string2[i:len_pattern + i] == pattern:
            return  True
    return False

assert True == exist_subsequence_any_position('prog', 'I love programing every day')
assert False == exist_subsequence_any_position('prob', 'I love programing every day')
assert True == exist_subsequence_any_position('proi', 'I love programing every day')

assert True == exist_subsequency_same_order('prog', 'I love programing every day')
assert False == exist_subsequency_same_order('prob', 'I love programing every day')
assert False == exist_subsequency_same_order('proi', 'I love programing every day')