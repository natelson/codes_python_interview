'''
Given a string S consisting of lowercase Latin Letters. Find the first non-repeating character in S.

Example 1:

Input:
S = lohello
Output: h
Explanation: In the given string, the
first character which is non-repeating
is h, as it appears first and there is
no other 'h' in the string.

Store the count of each character in a hash table.

Iterate over the string and if the frequency of any
character is 1, return it. If there is no non-repeating character then we return '$'.

'''
def first_norepeat_character(string):
    for character in string:
        find_position = -1
        count = 0
        for i in range(0,len(string)):
            if character == string[i]:
                find_position = i
                count +=1

        if count == 1:
            return find_position

    return -1



assert 0 == first_norepeat_character('potato')
assert 1 == first_norepeat_character('character')


