'''
Given two strings S1 and S2 in lowercase, the task is to make them anagram. The only allowed operation is to remove a
 character from any string. Find the minimum number of characters to be deleted to make both the strings anagram.
 Two strings are called anagram of each other if one of them can be converted into another by rearranging its letters.

Example 1:

Input:
S1 = bcadeh
S2 = hea
Output: 3
Explanation: We need to remove b, c
and d from S1.
'''

def convert_to_anagram(string1, string2):
    missing = ''
    for character in string1:
        if character not in string2:
            if character not in missing:
                missing += character

    if len(string2) > len(string1):
        for character in string2:
            if character not in string1:
                if character not in missing:
                    missing += character


    return len(missing)

assert 3 == convert_to_anagram('bcadeh', 'hea')