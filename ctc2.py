# CtC #1.2 problem: Check Permutation


'''
Exact Problem Statement

Given two strings, write a method to decide if one is a permutation of the other.
'''

'''
💡 Why It’s Important

This problem tests:

Understanding of string properties

How well you manage character frequency

Use of hash tables, sorting, or arrays

Efficient thinking about anagrams/permutations

Performance vs. simplicity in solution design
'''


def check_permutation1(s1, s2):
    '''
    ✔ Idea:

    If two strings are permutations, they have identical sorted character sequences.

⏱ Time: O(n log n)
💾 Space: O(n) (due to sorted copies)
    '''
    
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)

print(check_permutation1('abc', 'acb'))
print(check_permutation1('abc', 'xab'))


def check_permutation2(s1, s2):
    '''
    Count Characters (Hash Table)
    time: O(n)
    space: O(n)
    '''
    
    if len(s1) != len(s2):
        return False
    
    char_count = {}
    
    for char in s1:
        if char in char_count:
            char_count[char] += 1
        else: 
            char_count[char] = 1
        
    for char in s2:
        if char not in char_count:
            return False
        if char_count[char] < 0:
            return False
        char_count[char] -= 1
    return True
    
print(check_permutation2('abc', 'acb')) 
print(check_permutation2('abc', 'xab'))
    
    