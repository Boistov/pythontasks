a = int(input())
b = int(input())
c = int(input())
d = int(input())

number = a
while number <= b:
    if number % d == c:
        print(number)
    number += 1

