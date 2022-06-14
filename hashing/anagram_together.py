'''
Given an array of strings, return all groups of strings that are anagrams.
The groups must be created in order of their appearance in the original array. Look at the sample case for clarification.


Example 1:

Input:
N = 5
words[] = {act,god,cat,dog,tac}
Output:
god dog
act cat tac
Explanation:
There are 2 groups of
anagrams "god", "dog" make group 1.
"act", "cat", "tac" make group 2.
'''

from collections import defaultdict


def anagram(arr):
    dict1 = defaultdict(list)

    for index, key in enumerate(arr):
        key = str(sorted(key))
        dict1[key].append(arr[index])

    ans = []
    for word in dict1.values():
        ans.append(word)

    return ans


assert [['toc', 'cot', 'cto'], ['arg', 'gra', 'rag'], ['ploc']] == anagram(['toc', 'cot', 'cto','arg', 'gra', 'rag', 'ploc'])