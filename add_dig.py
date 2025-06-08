num = 38

while num >= 10:
    s =str(num)
    
    n = 0
    for digits in s:
        print(digits)
        n += int(digits) 
    num = n
print(num)