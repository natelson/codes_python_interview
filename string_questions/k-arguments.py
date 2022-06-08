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


