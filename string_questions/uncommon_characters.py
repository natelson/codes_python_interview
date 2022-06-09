'''
Given two strings A and B. Find the characters that are not common in the two strings.

Input:
A = characters
B = alphabets
Output: bclpr
'''

def uncommon_character(string1, string2):
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


    return missing

assert 'agh' == uncommon_character('abcdef', 'bcdefgh')
