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