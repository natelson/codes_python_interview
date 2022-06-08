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


