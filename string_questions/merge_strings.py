'''
Given two strings S1 and S2 as input, the task is to merge them alternatively i.e.
 the first character of S1 then the first character of S2 and so on till the strings end.
NOTE: Add the whole string if other string is empty.

Example 1:

Input:
S1 = "Hello" S2 = "Bye"
Output: HBeylelo
Explanation: The characters of both the
given strings are arranged alternatlively.
'''
def merge_strings(string1, string2):
    new_string = ''
    for i in range(len(string1)):
        new_string += string1[i]
        if i >= len(string2):
            new_string += string2[i:]
        else:
            new_string += string2[i]

        if i == len(string1)-1 and i <= len(string2):
            new_string += string2[i+1:]


    return new_string

assert 'BHyeello' == merge_strings('Bye', 'Hello')
assert 'HBeylelo' == merge_strings('Hello', 'Bye')
