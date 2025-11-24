n = int(input())

print(n, end=" ")

while n != 1:
    if n % 2 != 0:
        n = (n * 3) + 1
    else:
        n = n // 2
    print(n, end=" ")
