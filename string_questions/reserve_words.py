'''
Given a String S, reverse the string without reversing its individual words. Words are separated by dots.

Example 1:

Input:
S = i.like.this.program.very.much
Output: much.very.program.this.like.i
Explanation: After reversing the whole
string(not individual words), the input
string becomes
much.very.program.this.like.i
'''

def reverse_words(string):
    list_string = string.split('.')
    list_string = list_string[::-1]
    return '.'.join(list_string)

assert 'power.the.have.i' == reverse_words('i.have.the.power')
assert 'you.with.be.force.the' == reverse_words('the.force.be.with.you')