def palindromeIndex(s):
    if s == s[:: -1] :
        return -1
    for i in range(len(s)) :
        print(i)
        t = s[:i]  + s[i + 1 :]
        print(t)
        if t == t[:: -1] :
            return i

s = 'aaab'
print(palindromeIndex(s))


def is_palindrome_range(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def palindromeIndex(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            # Try removing left character
            if is_palindrome_range(s, left + 1, right):
                return left
            # Try removing right character
            elif is_palindrome_range(s, left, right - 1):
                return right
            else:
                return -1
        left += 1
        right -= 1

    return -1  # Already a palindrome

