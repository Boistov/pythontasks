a = int(input())
b = int(input())
if a % 2 == 0:
    i = a
else:
    i = a + 1

while i <= b:
    print(i)
    i += 2
