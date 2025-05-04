pali = "racecar"
pali = pali.lower()
res = ''
for i in range(len(pali))  :
    res = pali[i] + res
print(res) 
if res == pali:
    print("Palindrome")
else:   
    print("Not a palindrome")


pali = "noon"
if pali == pali[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")


# Using the reversed() function
pali = "level"
pali = pali.lower()
if pali == ''.join(reversed(pali)):   #reversed() returns an iterator, so we need to join it to convert it to a string and ' '. will join the characters
    print("Palindrome")
else:   
    print("Not a palindrome")


pali = "nayana"
left = 0
right = len(pali) - 1   # fixed variable name
is_palindrome = True
while left < right:
    if pali[left] != pali[right]:  # fixed variable name
        is_palindrome = False
        break
    left += 1
    right -= 1

if is_palindrome:
    print("Palindrome")
else:
    print("Not a palindrome")
