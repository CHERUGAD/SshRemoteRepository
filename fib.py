
tot = 0
n = 10
fib = [0, 1]
for i in range(2, n+1):
    fib.append(fib[i -1]+ fib[i  -2])
    tot += fib[i]
print(fib)

print(tot)
print(n)