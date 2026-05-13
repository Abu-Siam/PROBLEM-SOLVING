input_str = input()
input_str= input_str.lower()
l_pointer, r_pointer = 0, len(input_str)-1

while l_pointer < r_pointer:
    if not input_str[l_pointer].isalnum():
        l_pointer+=1
        continue
    if not input_str[r_pointer].isalnum():
        r_pointer-=1
        continue

    if input_str[l_pointer] != input_str[r_pointer]:
        print("not pallindrome")
        exit()
   
    l_pointer+=1
    r_pointer-=1

print("pallindrome")


def isPalindrome(s: str) -> bool:
    s = s.lower()
    l, r = 0, len(s) - 1

    while l < r:
        if not s[l].isalnum():
            l += 1
            continue
        if not s[r].isalnum():
            r -= 1
            continue
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1

    return True

# Time: O(n) — each character is visited at most once
# Space: O(1) — no extra data structures, just two pointers