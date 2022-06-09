'''
In this problem, a String S is composed of lowercase alphabets and wildcard characters i.e. '?'.
Here, '?' can be replaced by any of the lowercase alphabets. Now you have to classify the given String on the basis of following rules:
If there are more than 3 consonants together or more than 5 vowels together, the String is considered to be "BAD".
A String is considered "GOOD" only if it is not “BAD”.
NOTE: String is considered as "BAD" if the above condition is satisfied even once. Else it is "GOOD" and the task is to make the string "BAD".

Example 1:

Input:
S = mobile??
Output:
GOOD
Explanation: The String doesn't contain more
than 3 consonants or more than 5 vowels together.
So, it's a GOOD string.
Example 2:

Input:
S = bcdaeiou??
Output:
BAD
Explanation: The String contains the
Substring "aeiou??" which counts as 7
vowels together. So, it's a BAD string.
'''

def isGoodOrBadString(string):
    voewls = 'aeiou'
    consonantes = 'bcdfghjklmnpqrstvxwyz'
    count_vogals = 0
    count_consonts = 0
    for character in string:
        if character in voewls:
            count_vogals += 1
            if count_vogals >= 5:
                return False
        else:
            count_vogals = 0

        if character in consonantes:
            count_consonts += 1
            if count_consonts >= 3:
                return False
        else:
            count_consonts = 0

    return True


assert False == isGoodOrBadString('goeiuop')
assert True == isGoodOrBadString('teacher')
assert False == isGoodOrBadString('phnomenal')