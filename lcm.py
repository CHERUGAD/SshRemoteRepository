import math
def lcm(a,b):
    return a*b //math.gcd(a,b)
def lcm_of_three(a,b, c):
    return lcm(lcm(a, b), c)

print(lcm(4,5))
print(lcm_of_three(4,5,40))