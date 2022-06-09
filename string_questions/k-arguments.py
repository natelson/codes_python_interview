'''
Given two strings of lowercase alphabets and a value K, your task is to complete the given function which
tells if  two strings are K-anagrams of each other or not.

Two strings are called K-anagrams if both of the below conditions are true.
1. Both have same number of characters.
2. Two strings can become anagram by changing at most K characters in a string.

Input:
str1 = "fodr", str2="gork"
k = 2
Output:
1
Explanation: Can change fd to gk

Stores occurrence of all characters of both strings in separate count arrays.
Count number of different characters in both strings (in this if a strings has 4 a
and second has 3 ‘a’ then it will be also count.
If count of different characters is less than or equal to k, then return true else false.
'''
def is_anagram_with_k(string1, string2, k):
    if len(string1) != len(string2):
        return False
    missing = 0
    for character in string1:
        if character not in string2:
            missing += 1

        if missing > k:
            return False

    return True


assert False == is_anagram_with_k('fadr', 'gadrk', 2)
assert True == is_anagram_with_k('fadr', 'gark', 2)
assert False == is_anagram_with_k('fadr', 'gark', 1)


