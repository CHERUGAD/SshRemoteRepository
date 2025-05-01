fib1 = 0
fib2 = 1
print(fib1)
print(fib2)
fibb = 0
for i in range(18):
    fibb = fib1 +fib2
    fib1 = fib2
    fib2 = fibb
    print(fibb)
print("The 18th Fibonacci number is:", fibb)



#using recursion
print(0)
print(1)
count = 2

def fibonacci(prev1, prev2):
    global count
    if count <= 19:
        newFibo = prev1 + prev2
        print(newFibo)
        prev2 = prev1
        prev1 = newFibo
        count += 1
        fibonacci(prev1, prev2)
    else:
        return

fibonacci(1,0)
print("The 18th Fibonacci number is:", fibb)


def F(n):
    if n <=1 :
        return n
    else:
        return F(n-1)+F(n-2)
F(19)
print("The 18th Fibonacci number is:", F(19))