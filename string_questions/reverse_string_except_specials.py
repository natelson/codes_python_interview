def reverse_string(string, special_list):
    new_string = [''] * len(string)
    max_lengh = len(string)-1
    print(new_string)
    for i in range(0,max_lengh+1):
        if string[i] not in special_list:
            new_string[max_lengh-i] = string[i]
        else:
            new_string[i] = string[i]

        print(new_string, string, string[i])


    return ''.join(new_string)


print(reverse_string('abd?tgh?g','?'))

