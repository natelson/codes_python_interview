'''
Given an array of names (consisting of lowercase characters) of candidates in an election.
A candidate name in array represents a vote casted to the candidate. Print the name of
candidate that received Max votes. If there is tie, print lexicographically smaller name.

Example 1:

Input:
n = 13
Votes[] = {john,johnny,jackie,johnny,john
jackie,jamie,jamie,john,johnny,jamie,
johnny,john}
Output: john 4
Explanation: john has 4 votes casted for
him, but so does johny. john is
lexicographically smaller, so we print
john and the votes he received.
'''

def select_winner(arr1):
    dict1 = {}
    for item in arr1:
        if item not in dict1:
            dict1[item] = 1
        else:
            dict1[item] += 1

    winner = ['',0]
    for key, value in dict1.items():
        if winner[1] < value:
            winner[0] = key
            winner[1] = value
        elif winner[1] == value and len(winner[0]) > len(key):
            winner[0] = key
            winner[1] = value

    return winner[0],winner[1]

assert ('john', 3) == select_winner(['john', 'johny', 'paul','pam','john', 'john', 'johny','johny'])