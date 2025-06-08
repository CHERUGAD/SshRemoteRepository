n = 13
binary_digits = []
while n > 0:
    quot = n%2
    binary_digits.append(quot)
    n = n //2


binary_digits = binary_digits[::-1]
converted_bin = ''.join(str(bit) for bit in binary_digits)
print(converted_bin)
    

    

