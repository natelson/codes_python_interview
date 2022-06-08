def orderString(word):
    charCount = [0]*len(word)

    for i in range(len(word)):
        charCount[i] = ord(word[i])

    charCount = sorted(charCount)

    charCount = charCount[::-1]
    new_string = ''
    for i in range(len(charCount)):
        new_string += chr(charCount[i])

    return new_string

assert 'rofa' == orderString('fora')
assert 'romaa' == orderString('amora')



