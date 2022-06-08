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