'''
Given two strings a and b consisting of lowercase characters. The task is to check
whether two given strings are an anagram of each other or not. An anagram of a
string is another string that contains the same characters, only the order of characters
can be different. For example, “act” and “tac” are an anagram of each other.

Input:
a = allergy, b = allergic
Output: False
Explanation:Characters in both the strings
are not same, so they are not anagrams.
'''

def isAnagram(string1, string2):
    map = {}
    for letter in string1:
        if letter in map.keys():
            map[letter]+=1
        else:
            map[letter] = 1

    for letter in string2:
        if letter not in map.keys():
            return False
        else:
            map[letter] -=1

    for i in map.keys():
        if map[i] != 0:
            return False

    return True

assert False == isAnagram('allergy', 'allergic')
assert True == isAnagram('all', 'lal')