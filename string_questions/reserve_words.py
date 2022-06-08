def reverse_words(string):
    list_string = string.split('.')
    list_string = list_string[::-1]
    return '.'.join(list_string)

assert 'power.the.have.i' == reverse_words('i.have.the.power')
assert 'you.with.be.force.the' == reverse_words('the.force.be.with.you')