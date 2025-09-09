# cracking the coding #1 problem

'''
Implement an algorithm to determine if a string has all unique characters.

❗ What if you cannot use additional data structures?
'''


def is_unique1(string):
    '''using a set
    time complexity: O(n)
    space complexity: O(n)
    '''
    print(set(string))
    return len(set(string)) == len(string)

print(is_unique1('abca'))


def is_unique2(string):
    '''using a boolean array
    time complexity: O(n)
    space complexity: O(1) # because the boolean array is always 128 long
    '''
    if len(string) > 128:
        return False
    bool_array = [False]*128
    for char in string:
        if bool_array[ord(char)]:
            return False
        bool_array[ord(char)] = True
    return True

print(is_unique2('abca'))



def is_unique3(string):
    '''using a bit vector
    time complexity: O(n)
    space complexity: O(1)
    only works for lowercase letters(a-z)
    '''
    
    checker = 0
    for char in string:
        val = ord(char) - ord('a')
        if val<0 or val > 25:
            print("only a-z allowed")
            return False
        if checker & (1 << val):
            return False
        checker |= (1<<val)
    return True

print(is_unique3('abca'))


def is_unique4(s):
    '''using sort and compare adjacent characters
    no extra data structure needed
    time complexity: O(n log n)
    space complexity: O(1)
    '''
    s = sorted(s)
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return False

    return True

print(is_unique4('abca'))
