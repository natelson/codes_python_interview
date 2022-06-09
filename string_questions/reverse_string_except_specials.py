#Invert a string, but keep the position the special characters
#input 'b?a?', '?'
#output 'a?b?


def reverse_string(string, special_list):
    new_string = [''] * len(string)
    max_lengh = len(string)-1
    j = max_lengh
    for i in range(0,max_lengh+1):
        if string[i] not in special_list:
            if new_string[j] != '' or string[j] in special_list:
                j-=1
            new_string[j] = string[i]
            j-=1
        else:
            new_string[i] = string[i]
    return ''.join(new_string)


assert 'w?f?nxb?a' == reverse_string('a?b?xnf?w','?')
assert 'a?b?' == reverse_string('b?a?','?')
