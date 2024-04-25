import math

x = int(input())

n = 0
i = 1

while i <= math.isqrt(x):
    if x % i == 0:
        n += 2
        if i * i == x:
            n -= 1
    i += 1

print(n)

