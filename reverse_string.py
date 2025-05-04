reversing_string = "Reverse this string"
reversed_string = reversing_string[::-1]
print(reversed_string)

#Second method
print(reversed('hello'))
# Convert to string and join
print(''.join(reversed('hello')))

#Third method
print(''.join(list(reversed('hello'))))

#Fourth method
text = "hello"
reversed_text = ''
for char in text:
    reversed_text = char + reversed_text
print(reversed_text)


#Fifth method
text = "hello"
i = len(text) - 1
reversed_text = ''
while i >= 0:
    reversed_text += text[i]
    i -= 1
print(reversed_text)
