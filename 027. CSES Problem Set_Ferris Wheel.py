n, x = map(int, input().split())
p = list(map(int, input().split()))

p.sort()

i = 0
j = n - 1
gondolas = 0

while i <= j:
    if p[i] + p[j] <= x:
        i += 1
        j -= 1
    else:
        j -= 1
    gondolas += 1

print(gondolas)
