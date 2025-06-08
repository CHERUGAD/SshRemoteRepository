def if_palindrome(s):
    s = ''.join(char.lower() for char in s if char.isalnum())
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[:: -1]
s = "A man, a plan, a canal: Panama"
print(if_palindrome(s))



n = 121
s = str(n)
is_palindrome = s == s[::-1] 
print(is_palindrome)

  