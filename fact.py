def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)

n = int(input())
print(fact(n))




n = 2
Fact = 1
i = 2
while i <= n :
    Fact *= i
    i += 1
print(Fact)