# Take an integer input from the user
x = int(input())
n = 1

while  x % n == 0:
    if n <= x:
        print(n, end=" ")
        n += 1
