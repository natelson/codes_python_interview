def strstr(string, pattern):
    len_pattern = len(pattern)
    for i in range(0,len(string)):
        if (i + len_pattern) > len(string):
            return -1
        if string[i:len_pattern+i] == pattern:
            return i

    return -1


assert 0 == strstr('ProgramingisGoodForEverwone', 'Pro')
assert 12 == strstr('ProgramingisGoodForEverwone', 'Good')
assert 24 == strstr('ProgramingisGoodForEverwone', 'one')