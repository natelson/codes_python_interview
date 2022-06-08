def merge_strings(string1, string2):
    new_string = ''
    for i in range(len(string1)):
        new_string += string1[i]
        if i >= len(string2):
            new_string += string2[i:]
        else:
            new_string += string2[i]

        if i == len(string1)-1 and i <= len(string2):
            new_string += string2[i+1:]


    return new_string

assert 'BHyeello' == merge_strings('Bye', 'Hello')
assert 'HBeylelo' == merge_strings('Hello', 'Bye')
